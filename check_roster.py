#!/usr/bin/env python3
"""Self-check for a focus-group roster or standing panel written in the profile template.

Usage:
    python3 check_roster.py panel.md                       # whole file
    python3 check_roster.py panel.md --seats 1-30          # one range of seats (e.g. the dentist seats)
    python3 check_roster.py panel.md --seats 1-30 --dentists --quota quotas.json
    python3 check_roster.py panel.md --seats 1-30,101-125 --dentists   # the merged dentist seats
    python3 check_roster.py panel.md --max-words 120 --json

The file is Markdown. Each profile starts with a bold header line

    **12. Dr. Hannah Lindqvist · 31 · woman**

followed by the seven template fields, with or without a leading "- ":

    Setting: ... / Tech today: ... / AI stance: ... / Friction: ...
    Says yes if: ... / Walks away if: ... / Influence: ... / In their words: ...

Role groups are the "## " headings above the profiles (a "### " heading also starts a group).

What it checks (the skill's "Self-check before delivering a role"):
  1. every profile has the seven fields, in order, and is at or under the word cap with labels
  2. AI stance is enthusiast / pragmatist / skeptic; skeptics per role group (at least one per group of 3+ seats, three per ten)
  3. no name used twice
  4. repeats within a role group of setting type x career stage x stance x ownership (x specialty)
  5. real organizations (DSOs, plans, vendors of AI products); software and sensor brands are allowed
  6. mentions of percentages, studies or citations inside profiles, to read by hand (a profile is a person, not data); counts [to verify] tags
  7. composition: women/men, age bands, states, rural; optional quotas from a JSON file

Quota JSON (any subset of keys; counts apply to the selected seats):
    {"women": 12, "ages": [5, 8, 7, 6, 4], "specialists": 6, "owners": 22,
     "solo": 10, "medicaid": 12, "dso": 5, "skeptics_min": 9}

Exit status is 1 when any hard check fails (fields, word cap, stance, duplicate names), else 0.
"""
import argparse
import collections
import json
import re
import sys

FIELDS = ["Setting", "Tech today", "AI stance", "Friction", "Says yes if", "Influence", "In their words"]
STANCES = ("enthusiast", "pragmatist", "skeptic")

STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
    "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
    "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming", "DC",
]

# Real organizations that must not appear in a fictional composite (add to taste). Software and sensor
# brands (Dentrix, Eaglesoft, Open Dental, Curve, Denticon, Dexis, Schick, Carestream, Planmeca...) are allowed.
REAL_ORGS = [
    "Aspen Dental", "Heartland Dental", "Pacific Dental", "Smile Brands", "Sonrava", "Western Dental",
    "Dental Care Alliance", "MB2", "Affordable Care", "Great Expressions", "Sage Dental", "Familia Dental",
    "Delta Dental", "Aetna", "Cigna", "MetLife", "Guardian", "Humana", "UnitedHealthcare", "United Healthcare",
    "Anthem", "Elevance", "Blue Cross", "DentaQuest", "Liberty Dental", "MCNA", "Avesis", "Envolve", "Sun Life",
    "Principal", "Ameritas", "Careington", "CareQuest", "Overjet", "Pearl", "VideaHealth", "Denti.AI", "Diagnocat",
    "Dentsply", "Henry Schein", "Patterson", "Benco", "Align", "Invisalign", "SmileDirect", "Kaiser", "Mayo",
    "Cleveland Clinic", "Harvard", "NYU", "UCSF", "UCLA", "Penn Dental", "Tufts", "Columbia",
]

HEADER_RE = re.compile(r"^\*\*(\d+)\.\s+(.+?)\s+·\s+(\d+)\s+·\s+([A-Za-z\-]+)\*\*\s*$")
FIELD_RE = re.compile(r"^(?:[-*]\s+)?(" + "|".join(re.escape(f) for f in FIELDS) + r"):\s*(.*)$")
YEARS_RE = re.compile(r"(\d+)\s+years")


def parse(text):
    """Return a list of profiles: dict(seat, name, age, gender, group, fields{label: text}, order[], text)."""
    profiles, group = [], "(no heading)"
    cur = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("## ") or line.startswith("### "):
            group = line.lstrip("# ").strip()
            continue
        m = HEADER_RE.match(line)
        if m:
            cur = {
                "seat": int(m.group(1)), "name": m.group(2).strip(), "age": int(m.group(3)),
                "gender": m.group(4).lower(), "group": group, "fields": {}, "order": [], "header": line,
            }
            profiles.append(cur)
            continue
        if cur is None:
            continue
        f = FIELD_RE.match(line)
        if f:
            cur["fields"][f.group(1)] = f.group(2).strip()
            cur["order"].append(f.group(1))
    for p in profiles:
        p["text"] = " ".join(f"{k}: {v}" for k, v in p["fields"].items())
    return profiles


def words_with_labels(p):
    n = len(re.sub(r"[*·]", " ", p["header"]).split())
    for k, v in p["fields"].items():
        n += len(k.split()) + len(v.split())
    return n


def stance(p):
    s = p["fields"].get("AI stance", "").lower()
    for st in STANCES:
        if s.startswith(st):
            return st
    return None


def setting_type(s):
    s = s.lower()
    locale = "rural" if re.search(r"\brural\b|small-town|small town", s) else "urban" if "urban" in s and "suburban" not in s else "suburban" if "suburban" in s else ""
    for key, label in [
        ("solo", "solo"), ("community health", "health center"), ("fqhc", "health center"), ("tribal", "health center"),
        ("100+", "large DSO"), ("dso", "DSO"), ("location", "multi-site group"), ("group", "group"),
        ("hospital", "hospital"), ("school", "academic"), ("university", "academic"), ("college", "academic"),
        ("state ", "government"), ("county", "government"), ("federal", "government"), ("insurer", "plan"),
        ("plan", "plan"), ("carrier", "plan"), ("benefit", "plan"), ("practice", "practice"), ("clinic", "clinic"),
    ]:
        if key in s:
            return (locale + " " + label).strip()
    return (locale + " other").strip()


def ownership(s):
    s = s.lower()
    if re.search(r"\b(owner|partner|founder|co-owner|solo practitioner|owns)\b", s):
        return "owner"
    if re.search(r"\b(associate|employed|director|manager|staff|hygienist|assistant|coordinator|reviewer|analyst|specialist)\b", s):
        return "employed"
    return "n/a"


def career_stage(s):
    m = YEARS_RE.search(s)
    if not m:
        m = re.search(r"(\d+)\s+years?\b", s)
    if not m:
        if "new graduate" in s.lower() or "months in" in s.lower():
            return "<=10"
        return "?"
    y = int(m.group(1))
    return "<=10" if y <= 10 else "11-25" if y <= 25 else "26+"


SPECIALTIES = ["pediatric", "orthodont", "periodont", "endodont", "prosthodont", "oral surg", "oral and maxillofacial", "public health"]


def specialty(s):
    s = s.lower()
    for sp in SPECIALTIES:
        if sp in s:
            return sp
    return "general"


DENTIST_WORDS = ["practice", "office", "dentist", "surgeon", "orthodont", "periodont", "endodont", "prosthodont",
                 "health center", "clinic", "dso", "group"]
NOT_DENTIST_WORDS = ["chief clinical officer", "regional dental director", "dental director,", "vp of", "vice president",
                     "claims reviewer", "dental consultant", "professor", "faculty", "board member", "program director",
                     "epidemiologist", "researcher", "consultant,", "chief dental officer"]


def is_dentist(p):
    """Heuristic: a 'Dr.' whose setting reads as a practising dentist's. Use --dentists to force it for a seat range."""
    s = p["fields"].get("Setting", "").lower()
    if not p["name"].startswith("Dr."):
        return False
    if any(w in s for w in NOT_DENTIST_WORDS):
        return False
    return any(w in s for w in DENTIST_WORDS)


def age_band(a):
    return 0 if a < 35 else 1 if a < 45 else 2 if a < 55 else 3 if a < 65 else 4


def states_in(s):
    found = [st for st in STATES if re.search(r"\b" + re.escape(st) + r"\b", s)]
    if "DC" in found and "Washington" in found and "Washington, DC" in s:
        found.remove("Washington")
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--seats", help="seat numbers to check: a range or a comma-separated list of ranges, e.g. 1-30 or 1-30,101-125")
    ap.add_argument("--quota", help="JSON file of quotas for the selected seats")
    ap.add_argument("--max-words", type=int, default=120)
    ap.add_argument("--dentists", action="store_true", help="treat every selected seat as a dentist seat (use with --seats)")
    ap.add_argument("--json", action="store_true", help="print the report as JSON")
    args = ap.parse_args()

    text = open(args.file, encoding="utf-8").read()
    profiles = parse(text)
    if args.seats:
        keep = set()
        for part in args.seats.split(","):
            lo, hi = (int(x) for x in part.strip().split("-")) if "-" in part else (int(part), int(part))
            keep.update(range(lo, hi + 1))
        profiles = [p for p in profiles if p["seat"] in keep]
    if not profiles:
        print("No profiles found. Headers must look like: **12. Name · 31 · woman**")
        return 2

    report, hard_fail = collections.OrderedDict(), False
    report["profiles"] = len(profiles)

    # 1. fields and word cap
    missing = {p["seat"]: [f for f in FIELDS if f not in p["fields"]] for p in profiles}
    missing = {k: v for k, v in missing.items() if v}
    misordered = [p["seat"] for p in profiles if p["order"] != [f for f in FIELDS if f in p["fields"]]]
    over = {p["seat"]: words_with_labels(p) for p in profiles if words_with_labels(p) > args.max_words}
    report["missing_fields"] = missing
    report["fields_out_of_order"] = misordered
    report["over_word_cap"] = over
    report["longest_profile_words"] = max(words_with_labels(p) for p in profiles)
    hard_fail |= bool(missing or over)

    # 2. stances and skeptics per group
    bad_stance = [p["seat"] for p in profiles if stance(p) is None]
    report["stance_not_recognised"] = bad_stance
    hard_fail |= bool(bad_stance)
    report["stances"] = dict(collections.Counter(stance(p) for p in profiles))
    groups = collections.OrderedDict()
    for p in profiles:
        g = groups.setdefault(p["group"], {"seats": 0, "skeptics": 0})
        g["seats"] += 1
        g["skeptics"] += stance(p) == "skeptic"
    report["skeptics_by_group"] = groups
    report["groups_of_3_plus_without_a_skeptic"] = [g for g, v in groups.items() if v["seats"] >= 3 and v["skeptics"] == 0]
    report["groups_under_three_per_ten"] = [g for g, v in groups.items() if v["seats"] >= 10 and v["skeptics"] * 10 < v["seats"] * 3]

    # 3. duplicate names
    names = collections.Counter(p["name"] for p in profiles)
    report["duplicate_names"] = [n for n, c in names.items() if c > 1]
    hard_fail |= bool(report["duplicate_names"])

    # 4. repeats within a group
    combos = collections.defaultdict(list)
    for p in profiles:
        s = p["fields"].get("Setting", "")
        key = (p["group"], specialty(s), setting_type(s), career_stage(s), stance(p), ownership(s))
        combos[key].append(p["seat"])
    report["repeated_combinations"] = [{"group": k[0], "specialty": k[1], "setting": k[2], "stage": k[3], "stance": k[4], "ownership": k[5], "seats": v} for k, v in combos.items() if len(v) > 1]

    # 5. real organizations
    hits = []
    for p in profiles:
        for org in REAL_ORGS:
            if re.search(r"\b" + re.escape(org) + r"\b", p["text"]):
                hits.append({"seat": p["seat"], "org": org})
    report["real_organizations"] = hits

    # 6. figures
    figures = []
    for p in profiles:
        if re.search(r"\d+\s?%|\bpercent\b|\bstud(y|ies)\b(?![\s-]+club)|\bsurvey (found|shows)\b|\bcited\b", p["text"], re.I):
            figures.append(p["seat"])
    report["profiles_with_figures"] = figures
    report["to_verify_tags"] = sum(p["text"].count("[to verify]") for p in profiles)

    # 7. composition
    comp = collections.OrderedDict()
    genders = collections.Counter(p["gender"] for p in profiles)
    comp["women"] = genders.get("woman", 0) + genders.get("girl", 0) + genders.get("female", 0)
    comp["men"] = genders.get("man", 0) + genders.get("boy", 0) + genders.get("male", 0)
    comp["other_gender_labels"] = {k: v for k, v in genders.items() if k not in ("woman", "girl", "female", "man", "boy", "male")}
    bands = [0] * 5
    for p in profiles:
        bands[age_band(p["age"])] += 1
    comp["ages_under35_35_44_45_54_55_64_65plus"] = bands
    st = collections.Counter()
    for p in profiles:
        for s in states_in(p["fields"].get("Setting", "")):
            st[s] += 1
    comp["states"] = len(st)
    comp["states_missing"] = [s for s in STATES if s not in st and s != "DC"]
    comp["rural_or_small_town"] = sum(bool(re.search(r"\brural\b|small-town|small town", p["fields"].get("Setting", ""), re.I)) for p in profiles)
    dentists = profiles if args.dentists else [p for p in profiles if is_dentist(p)]
    if dentists:
        d = collections.OrderedDict()
        d["seats"] = len(dentists)
        d["women"] = sum(p["gender"] in ("woman", "female") for p in dentists)
        db = [0] * 5
        for p in dentists:
            db[age_band(p["age"])] += 1
        d["ages"] = db
        d["specialists"] = sum(specialty(p["fields"]["Setting"]) not in ("general", "public health") for p in dentists)
        d["owners"] = sum(ownership(p["fields"]["Setting"]) == "owner" for p in dentists)
        d["solo"] = sum("solo" in p["fields"]["Setting"].lower() for p in dentists)
        d["medicaid"] = sum(bool(re.search(r"medicaid|chip\b", p["fields"]["Setting"], re.I)) for p in dentists)
        d["dso"] = sum(bool(re.search(r"\bDSO\b", p["fields"]["Setting"])) and "preparing to sell" not in p["fields"]["Setting"] for p in dentists)
        d["cohorts_le10_11to25_26plus"] = [sum(career_stage(p["fields"]["Setting"]) == c for p in dentists) for c in ("<=10", "11-25", "26+")]
        comp["dentists"] = d
    report["composition"] = comp

    # quotas
    if args.quota:
        q = json.load(open(args.quota))
        checks = collections.OrderedDict()
        d = comp.get("dentists", {})
        for key, actual in [("women", d.get("women", comp["women"])), ("ages", d.get("ages", bands)), ("specialists", d.get("specialists")),
                            ("owners", d.get("owners")), ("solo", d.get("solo")), ("medicaid", d.get("medicaid")), ("dso", d.get("dso"))]:
            if key in q:
                checks[key] = {"quota": q[key], "actual": actual, "ok": q[key] == actual}
        if "skeptics_min" in q:
            n = report["stances"].get("skeptic", 0)
            checks["skeptics_min"] = {"quota": q["skeptics_min"], "actual": n, "ok": n >= q["skeptics_min"]}
        report["quota_checks"] = checks

    report["hard_fail"] = hard_fail

    if args.json:
        print(json.dumps(report, indent=1))
    else:
        print(f"Profiles checked: {report['profiles']}   longest: {report['longest_profile_words']} words with labels (cap {args.max_words})")
        print(f"Missing fields: {missing or 'none'}")
        print(f"Fields out of order: {misordered or 'none'}")
        print(f"Over the word cap: {over or 'none'}")
        print(f"Stance not recognised: {bad_stance or 'none'}   stances: {report['stances']}")
        print("Skeptics by group:")
        for g, v in groups.items():
            print(f"  {v['skeptics']:2} of {v['seats']:3}  {g}")
        print(f"Groups of 3+ seats with no skeptic: {report['groups_of_3_plus_without_a_skeptic'] or 'none'}")
        print(f"Groups of 10+ seats under three skeptics per ten: {report['groups_under_three_per_ten'] or 'none'}")
        print(f"Duplicate names: {report['duplicate_names'] or 'none'}")
        rc = report["repeated_combinations"]
        print(f"Repeated setting x stage x stance x ownership combinations within a group: {len(rc)}")
        for r in rc:
            print(f"  {r['group']}: {r['specialty']} / {r['setting']} / {r['stage']} / {r['stance']} / {r['ownership']} -> seats {r['seats']}")
        print(f"Real organizations: {hits or 'none'}")
        print(f"Profiles mentioning percentages, studies or citations (read by hand): {figures or 'none'}   [to verify] tags: {report['to_verify_tags']}")
        print(f"Composition: women {comp['women']} / men {comp['men']}  ages {comp['ages_under35_35_44_45_54_55_64_65plus']}  states {comp['states']}  rural/small-town {comp['rural_or_small_town']}")
        if comp.get("other_gender_labels"):
            print(f"  other gender labels: {comp['other_gender_labels']}")
        if "dentists" in comp:
            print(f"  dentists: {json.dumps(comp['dentists'])}")
        if "quota_checks" in report:
            print("Quotas:")
            for k, v in report["quota_checks"].items():
                print(f"  {'OK ' if v['ok'] else 'OFF'} {k}: quota {v['quota']} actual {v['actual']}")
        print("RESULT:", "FAIL — fix before delivering" if hard_fail else "pass on the hard checks; read the soft ones above")
    return 1 if hard_fail else 0


if __name__ == "__main__":
    sys.exit(main())
