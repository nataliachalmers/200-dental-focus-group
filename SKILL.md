---
name: "focus-group"
description: Run an AI focus group — five meaningfully different stakeholder personas, a moderator, forced disagreement and one named trade-off — on any idea, product framing, policy proposal, talk message or one-pager, and return the discussion plus a decision memo. Also keeps the participants: a standing, product-agnostic panel of 200 fictional dental-industry personas in two benches across every dental-relevant role (Bench A mirrors the ADA HPI dentist workforce; Bench B was merged in from a roster built elsewhere), or a product roster of ten per role, and runs role sessions that roll up which roles' objections the next iteration has to answer. Use whenever Natalia asks to run a focus group, pressure-test an idea, asks what payers, DSOs, dentists, state Medicaid or a Hill staffer would think, wants the objections before a meeting or launch, asks how a message will land, asks for personas, participant profiles, a panel or a roster, or wants a roster from another tool merged into the panel — even if she only says 'poke holes in this' or 'who would block this?'.
---

# Focus group

An AI focus group is a rehearsal of the room Natalia is about to walk into: simulated stakeholders react to an idea, argue with each other, and vote. It points at where the objections will come from and which message needs to change — early and cheaply. It is not evidence. Nothing a persona says is ever quotable as stakeholder data, and every run says so in its last line.

The skill has three shapes. A **panel run** (sections 1–6) puts five seats in a room around one idea and ends in a decision memo. A **roster** (section 7) is the participants: by default a standing, product-agnostic panel of 200 personas in two benches across every dental-relevant role, built once and kept; or, when a team wants product-specific profiles, a product roster of ten per role. A **role session** (section 8) binds the panel to one product or idea, runs one role at a time, and rolls the results up by role, which is how a product team decides whose objections the next iteration has to answer. Start with the roster when the request is for personas, profiles, a panel or participants; start with a panel run when the request is to test an idea, a message or a page.

Never name a specific product in this skill's defaults, examples or persona library: the panel is reusable only if it belongs to no product. The product arrives at session time.

This skill is for testing reactions. It is the wrong tool for establishing facts (that is `claim-audit`), for rewriting the text (that is `plain-and-precise` or `talk-prep`), and for thinking an idea through from scratch (that is `critical-thinking-mode`, which can hand off here once there is something to test).

## 1. Intake — three things before anything runs

Do not build the panel until these are on the page. If Natalia gave them, restate them; if not, infer the obvious ones from what she shared and state the inference at the top so she can correct it — ask only when one is truly unknowable.

- **The idea, stated neutrally**, in three sentences or fewer, as the panel will hear it. If what she shared is a pitch, strip the adjectives: personas react to the thing, not to its marketing. Keep her own names for things (product names, tier names, rule names) exactly.
- **The decision this run informs.** Go or no-go, which feature first, which positioning, what to say to whom, what to change before it ships. A focus group with no decision produces opinions; one with a decision produces a memo.
- **The audience she will face next**, because that decides who sits on the panel.

When the request is for the plan or design only (a course deliverable, a proposal for how a focus group would work), stop after section 4 and add a short paragraph on how the group would be used to decide.

## 2. Build the panel — five seats, not five fans

Default seats, each filled by a specific role in a specific situation:

| Seat | Who | What they carry into the room |
|---|---|---|
| Pays | signs the contract, holds the budget, or funds the policy | cost, contracts, defensibility, migration paths |
| Delivers | uses it day to day, or has to present or sell from it | workflow, chair time, clicks, the 90-second pitch |
| Receives | the patient, reader, or member on the other end | trust, burden, "what does this mean for me" |
| Approves | can block it: IT, procurement, regulator, agency, legislature | integration surface, authority, precedent, security |
| Skeptic | has seen this category fail before | the wording that reads as evasive, the claim that will be tested |

For a message test (a one-pager, a talk, an op-ed), the seats map onto the room: "delivers" is whoever presents or sells from it, "receives" is the reader. If Natalia supplies her own personas, use hers; if she supplies four, add the missing seat and say which one. If the standing panel exists (section 7), cast the seats from it — from either bench, naming the seat numbers — with the channel's blocker in the skeptic seat.

Write every persona in one line with four parts — they are what make the arguments differ:

```
**<Seat> — <role, situation in a few words>.** *Goal:* … *Vantage:* … *Concern:* … *Demands:* …
```

Give each a concrete situation (office count, practice management system, region, years in the role, what burned them last time) so they argue from circumstances rather than caricature. Roles and situations, never demographics. Meaningfully different means different goals and different top priorities — two personas who would give the same answer are one persona.

### Persona library — the stakeholders Natalia actually faces

Pick from these by lane, or cast from the standing panel, or build bespoke when the idea needs someone not listed.

**Product and positioning (her company's products and her own concepts):** DSO VP of clinical operations (buys; wants one standard across offices and a migration path); private-practice owner dentist (uses; chair time, no PMS switch); office manager or revenue-cycle lead (runs it; claims attachments, workflow); DSO IT or integration director (approves; integration surface, security review); DSO compliance officer (approves; the claim has to match the clearance); dental plan or DBM chief dental officer (reviews the output on claims; consistency, fraud-waste-abuse, "will payers accept it"); plan underwriter or actuary (prices it; findings must behave the same across versions and tiers); AI-cautious clinical director (skeptic; over-call, liability, wording that hides what it is); account executive (sells from the page); patient in the chair (what they are shown); regulatory-minded colleague (cleared indication versus marketing claim).

**Policy proposals and coalition positions (Medicaid, Medicare, coalitions):** state Medicaid dental director (budget, provider participation, federal approval); CMS or HHS career staff (statutory authority, precedent, operational feasibility); Hill staffer (cost estimate, political cover, a constituent story); state dental association lobbyist (reimbursement, scope, autonomy); dental plan or DBM executive (administrability, network adequacy); FQHC dental director (volume, staffing, no-shows); state dental director or oral-health coalition lead (access measures, equity of the rollout order); patient advocate or caregiver (access, out-of-pocket cost, trust); actuary or budget analyst (cost, when savings show up, evidence bar); coalition partner from a medical or public-health organisation (why oral health belongs on their agenda).

**Talks, decks, op-eds and one-pagers (message tests) — the seats are the audience:** payer medical director or dental director; health-system CMO or service-line lead; specialist with a high evidence bar (cardiologist, nephrologist); primary-care clinician or pediatrician (workflow, closing the referral loop); care coordinator; journalist or general reader (op-eds); conference-goer who has heard ten AI talks this year (skeptic).

## 3. The moderator

The moderator's job is to make the disagreement happen and then make sense of it. Keep the moderator's lines short; the personas carry the run.

- Open by stating the idea neutrally (the intake sentence), then ask every seat for a first reaction and a top priority.
- Name the pattern in the room before forcing the split ("three of you want X, but for different reasons"). Put the two most opposed seats head to head on the named trade-off. Pull in the seat that has stayed quiet. Nobody concedes without a reason.
- Ask "what would change your mind?" and take the votes.
- Write the decision memo — the moderator's summary is the only part Natalia will act on.

## 4. Rules of the discussion

Name the trade-off before the run starts (it is usually the decision in disguise: three names or one product; reach or consent burden; speed or accuracy; cost or access). Then hold these, and say in the run header that they are in force:

1. **Each seat argues for a different top priority.** Five voices with one priority is one voice.
2. **Every seat disagrees materially with at least one other.** Agreement is cheap; the splits are where the decision lives.
3. **The named trade-off is argued from both sides**, by the seats with the most to lose on each side.
4. **No "I like it" without a because.** Personas speak from their vantage, not from the pitch — they have not read the talking points.
5. **Every asserted fact gets a [check] tag** — any number, rule, study, system, or product capability a persona states ("[check: which systems the integrated mode supports today]"). Simulated personas invent plausible statistics and regulations with total confidence; the run must never launder them into something that ends up on a page. The memo collects every tag.
6. **Votes come with a flip condition** — pursue / pursue with changes / don't pursue, plus the one thing that would change the vote. That turns opinions into testable conditions.
7. **Personas may push on a choice Natalia has already made** (a name, a rule, a framing). Report it in the memo as "the rule the panel pushed on", say where the seats landed, and leave it as hers to keep or change. Never soften it and never preach it.

## 5. Run format

A full run is three rounds and a memo, about 1,200–1,600 words. Personas get up to 80 words a turn; distinct voices matter more than length.

```
# Focus group: <idea in a few words>
**Idea (as the panel heard it):** …
**Decision this informs:** …
**Audience you'll face next:** …

## Panel
1–5. <one-line persona specs — with bench and seat number when cast from the standing panel>

**Rules for this run:** <the seven rules in one line, with the named trade-off spelled out>

## Round 1 — First reactions and top priority
## Round 2 — The split
## Round 3 — What would change your mind, and votes
## Decision memo
```

**Decision memo sections**, in this order:

- **Where they agreed** — often the part of the idea that is settled and needs no more work.
- **Where they split, and why** — the trade-off, each side's reason, and whether the sides converge on a fix.
- **Objections you'll hear in the room, in order** — the first five questions, as they would be asked.
- **The message that has to change for one stakeholder** — the one seat for whom the current wording is the reason to say no.
- **The rule the panel pushed on** — only when a seat challenged a choice already made.
- **Things this run asserted that need checking** — every [check] tag, as a list; hand to `claim-audit` before anything from the run is reused.
- **Validate with real humans** — the two or three cheapest tests with actual people (show the page for 40 seconds and ask "which one are you?"; have a rep pitch from it and count the follow-up questions).
- **Recommended next step** — one sentence.
- **Caveat** — one line: simulated seats rehearsing the room, not evidence; not quotable as stakeholder data.

**Quick mode** ("quick focus group", or when the idea is small): panel in one line each, one round of reactions with top priority and vote, memo in five lines. Say it was quick mode.

## 6. After the run — the infinite part

The same panel can be reconvened as many times as the idea changes. On a follow-up, do not re-run everything; show only what moved.

- **"Re-run with this change"** — restate the change, then report per seat whether the vote or flip condition moved and why. New [check] tags only.
- **"Add a seat"** ("add a CFO", "add a pediatrician") — write the new persona spec, run them through the three questions (reaction and priority, position on the trade-off, vote with flip condition), and update the memo lines they change.
- **"Cross-examine <seat>"** — the moderator and Natalia question one persona; it stays in character and keeps tagging its facts.
- **"Swap the trade-off"** — same panel, new named trade-off, Round 2 and the memo only.
- **"Run it on the other bench"** — same idea, same ballot, the seats re-cast from the bench not yet used; report the two benches side by side and say where they differ, because the benches were built to different rules and a difference is usually a composition effect before it is a finding.

Handoffs: [check] and [to verify] items go to `claim-audit`; "the message has to change" goes to `plain-and-precise` for writing or `talk-prep` for talks; if the run shows the idea itself is unformed, send it back through `critical-thinking-mode` before convening the panel again.

## 7. Roster mode — the participants

Write as a dental-industry user researcher who has run focus groups for practice software and clinical AI and knows how solo practices, DSOs and dental payers actually decide to buy and adopt technology. Two roster shapes:

- **The standing panel (default):** 200 fictional personas in two benches across every dental-relevant role, product-agnostic, built once and kept in a document the team can open. Any product or idea is run against it in a role session (section 8). Rebuild a bench only when Natalia asks; add to it when she brings a roster from elsewhere (see "Merging an imported roster").
- **A product roster:** ten profiles per role for one named product, with product-specific Friction and Says-yes lines — her original prompt. Build it only when the team wants the profiles themselves to react to that product; even then, keep the product out of this skill.

### Intake

State what was given, infer the rest and say so:

- **What the panel is for and who will use it.** Default: the product and clinical team, deciding which roles' objections the next iteration of whatever they bring has to answer. A product roster also needs the product in three or four plain sentences (what it does, who uses it, how it is sold; public-level detail only), restated at the top as "Product (as the roster heard it)".
- **Market.** Default: United States.
- **Roles and seats.** Default: the standing-panel allocation below. Any role can be deleted, added or resized; a product roster uses the same role list at ten per role.

### The standing panel — 200 seats in two benches

**Bench A (seats 1–100)** was built to the roster rules from scratch: its 30 dentist seats mirror the ADA HPI workforce table cell by cell, its other splits are informed estimates, and it carries most of the panel's buying, installing and explaining depth (owners and associates, the office-manager veto, DSO C-suite, IT, payers, a state board member, a PMS vendor, a supply rep). **Bench B (seats 101–200)** was merged in from a 100-row roster Natalia built on another platform and rewritten into the same template: it carries breadth — 20 more patients, fifteen DSO functions including compliance, HR, facilities, patient experience and analytics, ten insurance roles including underwriting, actuarial and appeals, nine public-health and academic seats, and a specialist-heavy provider group. The two benches are reported side by side, never averaged, because they were built to different rules.

| Role group | Bench A | Bench B | Total | Notes |
|---|---|---|---|---|
| General dentists | 24 | 13 | 37 | A: owners and associates, a new graduate, 20+ years, a community health center. B: mid-career owners, one public-health dentist with a mobile van |
| Dental specialists | 6 | 12 | 18 | A: pediatric 2 · periodontist · orthodontist · oral surgeon · endodontist. B: pediatric 3 · orthodontist 2 · periodontist 2 · endodontist 2 · oral surgeon 2 · prosthodontist |
| Dental hygienists | 12 | 5 | 17 | A: health center, school program, temp agency, specialty office, DSO, new graduate |
| Dental assistants | 8 | 5 | 13 | surgical, pediatric, health center, DSO, cosmetic |
| Front desk and billing | 4 | 4 | 8 | B adds a surgical billing specialist |
| Office and practice managers, operations | 6 | 3 | 9 | A: the spouse-manager veto and a regional manager |
| Treatment and patient care coordinators | 4 | 3 | 7 | |
| DSO leadership and functions | 9 | 15 | 24 | A: CEO 2 · CFO 2 · clinical 3 · IT 2. B: CEO, CFO, COO, CTO, clinical quality, procurement, regional ops, compliance, integration, HR, revenue cycle, acquisitions, facilities, patient experience, analytics |
| Private-equity investors | 2 | 0 | 2 | one DSO investor, one dental-technology investor |
| Payers and public programs | 5 | 11 | 16 | A: plan dental director 2 · claims reviewer 2 · state Medicaid dental director. B: chief dental officer, adjuster, network, underwriting, policy analyst, consultant, fraud investigator, provider relations, actuary, appeals, state dental director |
| Public health and academia | 2 | 9 | 11 | A: dental school faculty, dental therapist. B: FQHC director, federal consultant, policy researcher, community coordinator, mobile-clinic dentist, hygiene program director, association lobbyist, equity manager, epidemiologist |
| Other dental-relevant roles | 8 | 0 | 8 | lab technician, transition broker, PMS integration lead, supply rep, state board member, association policy staff, employer benefits manager, DSO regional operations manager |
| Patients | 10 | 20 | 30 | A: two each of employer coverage, Medicaid, Medicare Advantage, parent or caregiver, uninsured. B: adds a veteran, a student, a teenager, an expectant mother, a dental tourist, cosmetic and concierge patients, an anxious patient, a diabetic in periodontal maintenance |

Geography: 45 states plus DC across the 200 (43 on Bench A), 18 rural or small-town settings. Stance: 96 pragmatists, 51 enthusiasts, 53 skeptics — 35 on Bench A, 18 on Bench B — with at least one skeptic in every role group of three or more seats, assigned independently of gender, ethnicity, age and seniority. Bench A alone is the harder room; Bench B runs younger and less skeptical because its author built it that way.

### Dentist seats — the workforce mirror, at any count

Source: ADA Health Policy Institute (Dentist Workforce page; The U.S. Dentist Workforce, 2025; Dental Care in Medicaid Programs, December 2025), 2024–2025 figures supplied by Natalia in September 2026 and spot-checked against those pages then. Out of 100 professionally active U.S. dentists: 39 women (about half under 35; parity expected around 2040) · ages 17 under 35, 26 aged 35–44, 23 aged 45–54, 19 aged 55–64, 15 aged 65+, average retirement age 68.7 · 67 White, 20 Asian, 6 Hispanic, 4 Black, 3 other or unknown · 79 general dentists, 21 specialists · settings 34 solo, 39 single-location group, 10 in 2–9 locations, 7 in 10–99, 11 in 100+ · 16 DSO-affiliated overall, 27 within 10 years of graduation · 73 own their practice (9 under 30, 33 at 30–34, 71 at 35–44, about 90 at 65+; women trail men at every stage) · 41 participate in Medicaid/CHIP (state range roughly 22 to 76) · rural density about half of urban.

Scale each percentage to the seat count and round so every dimension sums. **For 30 dentist seats** (Bench A): 12 women, 18 men; ages 5 · 8 · 7 · 6 · 4; 20 White, 6 Asian, 2 Hispanic, 1 Black, 1 other, shown through names only; settings 10 solo, 12 single-location group, 3 in 2–9 locations, 2 in 10–99, 3 in 100+; 5 DSO-affiliated; 22 owners, 8 employed; 12 in Medicaid; 6 specialists. **For 10 general dentists** (a product roster): 4 women, 6 men; ages 2 · 3 · 2 · 2 · 1; 7 owners, 3 employed; 3 solo, 4 single-location group, 1 small multi-site, 2 in a 100+ location DSO; 4 in Medicaid; 7 White, 2 Asian, 1 Hispanic or Black.

**The mirror holds on Bench A, not on the merged 55.** Scaled to 55 dentist seats the table would be 21 women; ages 9 · 14 · 13 · 10 · 9; 12 specialists; 40 owners; 19 solo; 23 in Medicaid; 9 DSO-affiliated. The merged 55 are 24 women; ages 9 · 18 · 13 · 11 · 4; 18 specialists; 42 owners; 15 solo; 18 in Medicaid; 5 DSO-affiliated. Every gap comes from Bench B's design — specialist-heavy, owner-heavy, mid-career, suburban, no dentist over 65, none inside a large DSO — and was flagged rather than fixed, because changing a persona's specialty or age to hit a quota makes it someone else. A session that needs a workforce-representative dentist vote runs on Bench A or weights by bench, and says so.

Ownership follows HPI's age curve (the youngest cohort mostly employed, the oldest almost all owners). The required seats fit inside the counts: the new graduate and the community-health-center dentist are employed; DSO seats are a mix of employed associates and partner-owners who kept equity when their practices were acquired, which is how the owner count holds. Two other compositions, chosen by the decision: *next-decade users* (within 10 years of graduation: half women, 18% solo, 44% in 100+ location practices, mostly employed — derived arithmetic, not a published table) and *today's signers* (26+ years out: nearly all owners, about half solo, almost none in large groups). Whichever the roster uses, sessions split the dentists by cohort, because the person who signs the check today and the person who will use the tool for twenty years are different people and a focus group needs both.

### Profile template — exactly these fields, in this order

```
**Name · age · gender**
Setting: role, practice or organization type, size, ownership, location, years in role (patients: coverage, where they get care, location, primary language if not English)
Tech today: practice-management and imaging software; any AI already used (patients: how they book, pay and get dental information)
AI stance: enthusiast, pragmatist or skeptic — and the reason
Friction: the moment in a normal day where a new tool has to earn its place (product roster: where this product would land)
Says yes if: … / Walks away if: … — the persona's conditions for adopting a new clinical or practice technology (product roster: this product)
Influence: who they persuade, and who persuades them, when a purchase or treatment decision is made
In their words: one sentence
```

### Roster rules

1. **Fictional composites with invented names** — never a real person, practice, DSO, plan or investment firm. Real practice-management and imaging software names are fine, because "Tech today" is only useful when it is real; AI already in use is described by category ("an AI overlay at a previous DSO"), never by a vendor's product name, because the roster will circulate.
2. **No statistics, studies or citations inside a profile** — profiles are people, not data. Where a figure is tempting, write [to verify]. Ten or so across a hundred profiles is normal; forty means the profiles have turned into claims. Workforce figures shape the composition; they never appear in a profile.
3. **Within a role, no two profiles share the same specialty, setting type, career stage, AI stance and ownership.** A skeptic in every role with three or more seats; three per ten.
4. **Vary** age, years in role, state and urban/suburban/rural, size and ownership, software and payer mix; patients also vary by age and primary language. Ten profiles from three states are three profiles.
5. **Fill every composition cell independently.** Attitudes, seniority and expertise are assigned independently of gender and ethnicity: no stance, ownership level or setting is concentrated in one gender or ethnicity unless the cell count is 1; women are not all the employed seats. Ethnicity shows through names (and, for patients, primary language), never through stance, expertise or setting.
6. **Plain language, 120 words per profile at most, counting the field labels.** Uncounted labels are where the extra words hide — building the standing panel, about a fifth of the profiles were over on their first pass.
7. **Every profile reads as a person.** Friction is a specific moment ("4:30 on a Tuesday when the internet drops mid-exam"), not a category; "In their words" is a sentence they would say out loud, not a slogan; "Says yes if" and "Walks away if" are conditions someone could actually meet or trip.
8. **Seat numbers are permanent.** A seat keeps its number for the life of the panel so that sessions, votes and blockers can cite it; a bench added later starts where the last one ended.

### Merging an imported roster

When Natalia brings a roster built somewhere else (a spreadsheet, another tool's export), merge it as a new bench rather than rewriting the panel around it:

- **Keep what is the author's:** roles, tenure, stated AI stance and the one-line synthesis. Those are the reason the roster exists.
- **Rewrite into the template:** add the missing fields (setting size and location, software, friction, says-yes and walks-away conditions, influence) so every seat can sit in a session; give related rows a shared fictional employer so colleagues argue from the same building.
- **Rename** every row that carries a real person's name or a fictional character's, and every name that duplicates a seat already on the panel; replace real organizations with fictional ones. Say how many changed.
- **Restore shifted rows** (a column slipped in the source) rather than dropping them, and say which.
- **Run the self-check on the new bench**, then report its composition beside the existing bench cell by cell — women and men, ages, stances, states, the dentist mirror — and flag every deviation instead of fixing it by editing personas.
- **Seat it after the last existing seat** and give it its own heading group in the panel document; update the blockers per channel where the new bench adds a channel or a sharper voice.

### Self-check before delivering a role

Run it and fix before showing anything: count every composition cell against its quota (sex, age band, owners and employed, setting, Medicaid, ethnicity by the names chosen); count skeptics; list specialty × setting type × career stage × stance × ownership within each role and look for repeats; count words per profile with the labels; confirm the role's own requirements (general dentist: owners, associates, a new graduate, 20+ years, a community health center; patients: two per coverage type, languages vary); scan for real organizations; confirm figures were replaced by [to verify]. `scripts/check_roster.py` in this folder does it in seconds on a panel or role file in the profile template (an optional quota JSON adds the cell counts); a roster that fails its own check is a pile.

### Closing table and the blockers

After the last role, one table — role · seats · women/men · ages · stances (the composition columns only where a quota applied), and the dentist quotas matched. Then the blockers. For the standing panel, name **the blocker per channel** — the seat whose no travels furthest when any new technology arrives: private practice purchase and chairside, DSO purchase, adoption, integration and compliance, safety net and Medicaid, payer clinical review and payer underwriting, regulator and policy, hygiene and assisting, patients, public health and equity — each with the objection they raise first and what flips them, with a seat from each bench where both have one, plus the objections ranked by how many seats raise them first (counted by hand, labelled approximate). For a product roster, name **the one profile most likely to block adoption** and the objection they will raise first — the person the focus-group guide gets built to test — and the runner-up in any other channel the product sells through.

### Delivery

The standing panel is about 23,000 words (each bench about 11,000) and a product roster of seventeen roles about 20,000: neither fits in chat. Write them into a document the team can open — one heading per bench and role group, a self-check per group, the composition table and the blockers at the end — and post only the table and the blockers in chat. One or two roles go in chat. When chat is the only option, work through the roles in order, stop at the end of a role, and name the next one.

### From profile to seat

A profile converts to a one-line seat spec: *Goal* ← Friction (what they are trying to get done in that moment); *Vantage* ← Setting + Tech today + Influence; *Concern* ← Walks away if; *Demands* ← Says yes if. Cast the five seats from the panel with the channel's blocker in the skeptic seat; their first objection is the first candidate for the named trade-off.

## 8. Role sessions and the objections-by-role roll-up

A product team's question is not "what does the room think" but "which roles' objections does the next iteration have to answer". For that, bind the panel to the product and run role sessions — one role, all its seats, one round — then roll them up.

Choose the bench by the question before the first session. Bench A alone when the dentist mirror matters (a workforce-representative vote on price, ownership, Medicaid or DSO affiliation) or when the room should be hard. Both benches when the question needs breadth: 30 patients, 24 DSO functions, 16 payer seats, eleven public-health and academic seats. Every session and every roll-up row names its bench; a 200-seat count is reported as two benches side by side, never as one average.

```
# Role session: <role> × <product or idea> — Bench A | Bench B | both
**Product (as heard):** three or four plain sentences  **Decision:** which of this role's objections the next iteration must answer
Each persona (seat number first): first reaction (up to 40 words) · vote (pursue / pursue with changes / don't pursue) · flip condition
**Tally:** yes / with changes / no — per bench when both ran; dentists also by cohort (up to 10 years out / 11–25 / 26+)
**The role's first objection:** the one most personas raised, in their words
**The swing persona:** whose flip condition is cheapest to meet
**[to verify] / [check]:** everything asserted
```

Then the roll-up, one row per role run:

| Role | Bench | Tally (yes / with changes / no) | First objection | Cheapest flip | Answer in the next iteration? |
|---|---|---|---|---|---|

"Answer in the next iteration?" is yes, no or later, with one reason. The row the team argues about is the one that matters. The cohort split is where a buyer-versus-user gap shows: when today's signers vote yes and next-decade users vote no, the roll-up says so in its own line (Bench A shows it more reliably; Bench B has three dentists in the oldest cohort). The single blocker for that product is named here, from the sessions, not in the standing panel. When two or three roles' objections collide (the dentist wants flags private, the payer wants them on the claim), a cross-role panel run (sections 1–6) with those seats is the follow-up. The same rules apply: [to verify] and [check] tags collected, votes with flip conditions, and the caveat line at the end.

## Worked examples, in brief

**Panel run.** Idea: a sales one-pager presenting a clinical product as one shared element available in three deployment modes. Decision: what to change before it ships. Panel: the DSO buyer (pays), the practice owner and the account executive (deliver — one uses it, one sells from it), the DSO IT director (approves), an AI-cautious clinical director (skeptic). Named trade-off: three products with standalone names vs. one product with three ways to deploy. What the run produced: agreement that the shared element worked and every argument was about the modes; a split on names that converged on "keep the names, lay them out as a ladder, add one migration line"; five objections in order, starting with "which one am I?"; one seat (IT) for whom a mode name was a promise that needed a compatibility footnote; one rule the panel pushed on (what to call the shared element), reported and left to Natalia; three [check] items; two human tests; one next step.

**Standing panel, Bench A.** 100 personas across 22 roles, product-agnostic, in a document: the 30 dentist seats matched every HPI-derived quota (12 women and 18 men, ages 5 · 8 · 7 · 6 · 4, 22 owners, 10 solo, 5 DSO-affiliated, 12 in Medicaid, six specialists); 59 women and 41 men overall because the practice team skews that way; 35 skeptics; 43 states; every profile at or under 120 words with labels. The self-check caught about twenty over-length profiles, seven repeated setting-and-stance combinations, one gender cell and two Medicaid seats before anything went in. Blockers named per channel — the office-manager spouse who is the private-practice veto, the DSO CFO who wants the offices that didn't get it, the regional dental director who has to look the associates in the eye, the VP of IT for whom "integrated" is a promise she tests, the Medicaid dental director for whom anything that finds more will be asked to prove it, and the patients whose first objection is the bill — with the objections ranked: minutes and steps first, who pays second, "will it measure me" third.

**Merged panel, Bench B.** A 100-row roster built on another platform (six groups: 25 providers, 20 office staff, 20 patients, 15 DSO, 10 insurance, 10 public health; role, organization, tenure, two AI-sentiment columns and a one-line synthesis per row) merged in as seats 101–200. Kept: every role, tenure and stance. Added: settings, software, friction, conditions and influence. Changed: 46 names (41 real people or fictional characters, 5 duplicates of Bench A), four real organizations, two rows whose columns had shifted. Reported beside Bench A cell by cell: 54 women and 46 men, 18 skeptics, 33 states; the merged dentist mirror off in most cells (24 women against 21, specialists 18 against 12, owners 42 against 40, solo 15 against 19, Medicaid 18 against 23, DSO-affiliated 5 against 9, four dentists over 65 against nine), flagged and left. What the second bench added to the blockers: a compliance officer for whom a name may not imply more than the clearance, an underwriter and an actuary who will price anything that varies by version or tier, an appeals specialist for whom a machine never signs a denial, and public-health seats for whom equity is in the rollout order — and one new ranked objection, "it has to behave the same across versions and tiers", raised first by eight seats.

**Vote on one idea, both benches.** The same three-way ballot on a set of tier names run seat by seat on each bench: Bench A 30 / 23 / 47 and Bench B 37 / 17 / 46 — the same winner and the same runner-up on both, Bench B a little readier to take the proposal as written, and 16 of Bench B's votes resting on the role alone because the source rows carried no friction or conditions (the merge added them). Reported as two benches, not as 67 / 40 / 93.
