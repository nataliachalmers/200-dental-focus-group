# focus-group

A Claude skill that rehearses the room before you walk into it. It runs an AI focus group — five meaningfully different stakeholder personas, a moderator, forced disagreement and one named trade-off — on any idea, product framing, policy proposal, talk message or one-pager, and returns the discussion plus a decision memo. It also keeps the participants: a standing, product-agnostic panel of 200 fictional dental-industry personas in two benches, and role sessions that roll up which roles' objections the next iteration has to answer.

It is a rehearsal, not evidence. Nothing a persona says is quotable as stakeholder data, and every run says so in its last line.

## What is in this folder

| Path | What it is |
|---|---|
| `SKILL.md` | The skill: intake, the five seats, the moderator, the seven rules, run format, decision memo, follow-ups, roster mode, role sessions, worked examples |
| `panel/standing-panel-200.md` | The standing panel — all 200 profiles in the skill's template, the allocation, the composition check, the blockers by channel and how to use it |
| `panel/quotas-bench-a-dentists.json` | The ADA HPI workforce table scaled to Bench A's 30 dentist seats, for the checker |
| `panel/quotas-merged-55-dentists.json` | The same table scaled to the 55 dentist seats across both benches (documents the gap Bench B introduces; it does not license rewriting personas) |
| `scripts/check_roster.py` | The self-check the skill requires before a roster is delivered: fields and word cap, stances and skeptics per role, duplicate names, repeated combinations, real organizations, figures, composition, quotas |

## The two benches

**Bench A (seats 1–100)** was built to the skill's roster rules from scratch. Its 30 dentist seats mirror the ADA Health Policy Institute workforce table cell by cell (women, age bands, ownership, solo, DSO affiliation, Medicaid participation, specialists); its other splits are informed estimates flagged as such. It carries the panel's buying, installing and explaining depth.

**Bench B (seats 101–200)** was merged in from a 100-row roster built on another platform: six groups (25 providers, 20 office staff, 20 patients, 15 DSO functions, 10 insurance roles, 10 public health), rewritten into the same template. Roles, tenure and stance are the author's; settings, software, friction, conditions and influence were added; 46 names and four organizations were changed to keep everything fictional. It carries breadth: 30 patients across the two benches, 24 DSO functions, 16 payer seats, eleven public-health and academic seats.

The benches are reported side by side, never averaged, because they were built to different rules. Bench A alone is the harder room (35 of the 53 skeptics) and the only one on which the dentist mirror holds.

## Using the skill

- **Test an idea:** "run a focus group on …", "poke holes in this", "who would block this?" → a panel run (five seats, three rounds, a decision memo).
- **Get the participants:** "give me personas / a panel / a roster" → roster mode; the standing panel above is the default.
- **Find whose objections come first:** "run role sessions on …" → one role at a time, rolled up by role and dentist cohort, with the bench named on every row.
- **Follow up:** "re-run with this change", "add a seat", "cross-examine the CFO", "swap the trade-off", "run it on the other bench".
- **Merge a roster from elsewhere:** the skill's "Merging an imported roster" section is the procedure Bench B went through.

## Running the self-check

```
python3 scripts/check_roster.py panel/standing-panel-200.md
python3 scripts/check_roster.py panel/standing-panel-200.md --seats 1-30 --dentists --quota panel/quotas-bench-a-dentists.json
python3 scripts/check_roster.py panel/standing-panel-200.md --seats 1-30,101-125 --dentists --quota panel/quotas-merged-55-dentists.json
python3 scripts/check_roster.py my-new-role.md --max-words 120 --json
```

No dependencies beyond Python 3. The hard checks (missing fields, over the word cap, unrecognised stance, duplicate names) return exit status 1; the soft checks (skeptics per group, repeated combinations, figures, composition, quotas) are printed for a person to read.

## Installing

Copy the `focus-group` folder into your Claude skills directory (for Claude Code, `~/.claude/skills/focus-group/`), or upload the folder as a skill in the Claude app. The skill triggers on requests to run a focus group, pressure-test an idea, ask what a stakeholder group would think, or ask for personas, a panel or a roster.

## Sources

The only sourced figures in the panel are the ADA Health Policy Institute dentist workforce figures (Dentist Workforce page; The U.S. Dentist Workforce, 2025; Dental Care in Medicaid Programs, December 2025) behind Bench A's dentist seats. Every persona is a fictional composite with an invented name; the only real names are practice-management and imaging software brands and public programs.
