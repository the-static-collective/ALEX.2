
# MN-CHURCH-AUTHORITY-PATTERN-MAP-001

Status: RESEARCH / HANDOFF
Parent: research/MN-CHURCH-LEGAL-BEDROCK-001.md
Sibling: research/MN-CHURCH-LEGAL-SEARCH-HANDOFF-001.md
Created: 2026-09-18 America/Chicago
Promotion: none
Authority: research only; not legal advice, not a filing instrument, not counsel approval

## Purpose

Preserve the deeper Minnesota church-authority dig that followed MN-CHURCH-LEGAL-BEDROCK-001, especially:

- the Chapter 315 distinction between ecclesiastical society and civil corporation;
- Minnesota case patterns showing that hierarchical ecclesiastical authority can survive local incorporation;
- the separate rule that affiliation/control does not automatically transfer title or collapse entity identity;
- the A/B/C architecture fork for the proposed Nigeria ↔ Minnesota branch;
- the capacity rule: the same human actor may exercise different powers in different offices;
- the statutory-history question around sections 315.03 and 315.05;
- the narrow information bundle now needed from Impact Makers before counsel validation.

This packet does not replace the parent dossier. It records the next layer.

## Compact findings

SOCIETY != CORPORATION

MINNESOTA INCORPORATION != ECCLESIASTICAL INDEPENDENCE

AFFILIATION MAY CARRY ECCLESIASTICAL GOVERNANCE

AFFILIATION != PROPERTY TITLE

CONTROL != OWNERSHIP

CONTROL != ENTITY IDENTITY

APPOINTMENT POWER != APPOINTER'S OWN POWER TO EXERCISE THE OFFICE

ACTOR != CAPACITY

PATH EXISTS != AUTHORITY COMPOSES

CODE ADJACENCY != RULE COMPOSITION

HISTORIC RECODIFICATION != SEMANTIC RESET

General architecture law:

RELATIONSHIP DOES NOT DETERMINE THE TYPE OF AUTHORITY IT CARRIES.

Candidate primitive:

PROVENANCE-GATED-COMPOSITION

A graph path does not itself authorize composition of the relations along that path.

## 1. Statutory hinge — society vs corporation

Minnesota Chapter 315 expressly distinguishes the religious society from the civil corporation.

Minn. Stat. section 315.08 describes the society as the religious body constituted according to its ecclesiastical polity, as distinguished from the corporation itself.

Working architecture:

religious / ecclesiastical society
    !=
Minnesota temporal corporation

This is stronger than a merely conceptual separation between spiritual and fiduciary authority. The statute itself preserves the distinction.

Source:
https://www.revisor.mn.gov/statutes/cite/315/full

## 2. Minnesota case-pattern map

### Russian-Serbian Holy Trinity Church v. Kulik

Citation: Russian-Serbian Holy Trinity Church v. Kulik, 202 Minn. 560 (1938).

Structural pattern:

local Minnesota incorporation
+ local trustee election
+ denominational law requiring episcopal confirmation
= effective trustees only after confirmation

The Minnesota Supreme Court rejected the idea that Minnesota incorporation necessarily made the local parish ecclesiastically independent.

Compact laws:

MINNESOTA INCORPORATION != ECCLESIASTICAL INDEPENDENCE

LOCAL ELECTION MAY REQUIRE UPSTREAM CONFIRMATION

Source:
https://law.justia.com/cases/minnesota/supreme-court/1938/202-minn-560.html

Architectural consequence:

This creates a serious alternative to direct foreign appointment:

Minnesota congregation
    -> elects trustees
local election
    -> confirmation condition
upstream ecclesiastical authority
    -> confirms
trusteeship becomes effective

This is the basis of Route B below.

### Trinity Church of Infinite Science

Case pattern:

Minnesota church affiliation can carry governance consequences without automatically transferring property.

Compact law:

AFFILIATION CAN CARRY GOVERNANCE

AFFILIATION DOES NOT CARRY TITLE

Property rights still require legally cognizable instruments such as deed, trust, charter provision, conveyance, or another recognized civil mechanism.

### Piletich v. Deretich

Citation: Piletich v. Deretich, 328 N.W.2d 696 (Minn. 1982).

The hierarchy involved a Mother Church centered in Belgrade, Yugoslavia.

Minnesota recognized that meaningful ecclesiastical authority could reside in a transnational hierarchy while separately applying neutral principles to property.

Compact law:

FOREIGN MOTHER CHURCH may possess ECCLESIASTICAL AUTHORITY

FOREIGN MOTHER CHURCH does not thereby possess LOCAL PROPERTY AUTHORITY

Neutral-principles loci include deeds, local charter, state statutes, general-church constitution, express trust provisions, and ordinary property law.

Source:
https://law.justia.com/cases/minnesota/supreme-court/1982/81-1247-1.html

Consequence for Nigeria:

The material unknown is not whether Minnesota law can conceptually tolerate foreign-centered ecclesiastical authority.

The discriminator is whether the actual Nigerian governing instrument gives the identified Nigerian actor/body the specific appointment, confirmation, or recognition power.

### Presbytery of the Twin Cities Area v. Eden Prairie Presbyterian Church

Case: Minnesota Court of Appeals, 2017.

Important delta:

A general denominational trust clause did not by itself prove that the local church, as settlor, intended to create a Minnesota property trust.

A later local corporate act expressly placing property in trust did create an enforceable trust relationship.

Compact laws:

DENOMINATIONAL RULE != LOCAL PROPERTY INTEREST

AFFILIATION != TRUST

GENERAL-CHURCH DECLARATION != LOCAL SETTLOR ACT

Additional drafting dimensions:

trust existence
+ trust res
+ trustee
+ beneficiary
+ settlor manifestation
+ revocability
+ amendment authority
+ disaffiliation contingency

Source:
https://law.justia.com/cases/minnesota/court-of-appeals/2017/a16-0945.html

### United Islamic Society v. Masjed Abubakr Al-Seddiq

Case: Minnesota Court of Appeals, 2016.

Religious characterization such as waqf did not itself determine the civil property result. Courts could examine deeds, minutes, resolutions, declarations, trust documents, and testimony through neutral principles without deciding theological truth.

Compact law:

SACRED CHARACTERIZATION != CIVIL PROPERTY EFFECT

Or:

ECCLESIASTICAL / RELIGIOUS MEANING does not silently compile into CIVIL TRUST TERMS

Source:
https://law.justia.com/cases/minnesota/court-of-appeals/2016/a16-0140.html

### Eller v. Diocese of St. Cloud

Case: Minnesota Court of Appeals, 2006. Unpublished; persuasive structural evidence, not controlling precedent.

The same human actor could be bishop, corporate president, and corporate board member without the powers of those capacities collapsing together.

The bishop's ecclesiastical authority over priests arose through canon/ecclesiastical law, not merely because he was president of the Minnesota civil corporation.

Compact law:

ACTOR != CAPACITY

Example:

Person P as bishop -> ecclesiastical power X

Person P as corporate president -> civil power Y

X != Y

Source:
https://law.justia.com/cases/minnesota/court-of-appeals/2006/opa050828-0124.html

Suggested AuthorityAct shape:

AuthorityAct {
  human_actor_ref,
  office_ref,
  capacity_ref,
  represented_entity_ref,
  authority_source_ref,
  act_type,
  scope,
  concurrence_required,
  effective_condition,
  affected_person_asset_or_fund_ref,
  evidence_refs,
  receipt_ref,
  residual_fog
}

### Archdiocese bankruptcy / parish entity separation

Case pattern: Eighth Circuit, 2018.

The Archbishop could possess extensive governance/control relations with parish corporations through Minnesota religious-corporation law without all parish entities becoming identical to the Archdiocese or all parish assets collapsing into one estate.

Compact laws:

CONTROL != OWNERSHIP

CONTROL != ENTITY IDENTITY

APPOINTMENT POWER != ALTER EGO

Source:
https://law.justia.com/cases/federal/appellate-courts/ca8/17-1079/17-1079-2018-04-26.html

## 3. Chapter 315 foreign-center fossil

Minn. Stat. section 315.39 historically addressed certain Minnesota religious-property circumstances where the denomination's central or supreme government was in a foreign country.

Its operative fact pattern is narrow and historical; it is not the proposed formation rule.

But its existence establishes a bounded observation:

FOREIGN ECCLESIASTICAL CENTER != ALIEN CONCEPT TO CHAPTER 315

This does not solve F1. It narrows the question.

## 4. Statutory-history seam — sections 315.03 and 315.05

### Section 315.03 recording package

Modern section 315.03 refers to the certificate, acknowledgment, notice of meeting, and posting affidavit.

But section 315.01(3)'s direct-appointment route does not itself require a congregational election meeting.

Historical reconstruction indicates the modern text is the product of consolidation of older incorporation schemes.

The original 1851 Territorial Chapter 36 included an appointment mechanism and directed the appointment certificate to be recorded as provided in the chapter.

The 1985 Chapter 265 legislation was expressly a Revisor's Bill intended to revise language and organization without changing substantive meaning.

Therefore:

1985 WORDING TRANSFORMATION != INTENDED SUBSTANTIVE TRANSFORMATION

Working finding:

section 315.01(3) certificate requirements = observed

foreign/direct appointment route = observed

whether section 315.03 election-specific notice/posting artifacts must also accompany a subdivision-3 appointment certificate = unresolved operative question

This remains a recorder/counsel discriminator.

### Section 315.05 minister-compensation seam

Section 315.05 contains the rule that trustees may not fix the minister's salary; the salary is fixed by the relevant voting society.

The difficult interaction is:

appointment polity:
    trustees selected upstream

salary language:
    salary fixed by majority of society
    entitled to vote at trustee elections

If the polity does not elect trustees locally, the phrase becomes structurally awkward.

Historical material does not justify silently declaring the rule inapplicable.

Current status:

REAL COUNSEL QUESTION

## 5. A/B/C architecture

### A — Direct upstream appointment

Candidate statutory route:

Minn. Stat. section 315.01(3)

Shape:

Impact Makers Nigeria
    -> actual governing constitution/rules/usages
identified Nigerian officer/body
    -> chooses Minnesota trustees
appointment certificate
    -> Minnesota religious corporation

What must be true:

The actual Nigerian governing law must supply the appointment authority.

Do not infer appointment power merely from founder status, spiritual leadership, ministry branding, informal deference, or generic branch language.

Required discriminator:

Who, under the actual governing instrument, has authority to choose, appoint, or remove branch trustees?

Remaining legal fog:

- direct Minnesota authority on a Nigerian/foreign selecting body;
- authentication/execution requirements for foreign signatories;
- exact section 315.03 recording package on the subdivision-3 route.

### B — Local election + upstream confirmation

Candidate statutory/case pattern:

Minn. Stat. section 315.01(2)
+
Kulik

Shape:

Minnesota members
    -> elect trustees
trustee election
    -> not yet effective if polity requires confirmation
Impact Makers Nigeria
    -> confirms / recognizes
trusteeship effective

Why B matters:

B preserves real hierarchy without requiring the Nigerian body itself to perform the Minnesota civil election act.

It also fits section 315.03's election/notice/affidavit machinery more naturally.

Critical warning:

B is not merely cleaner paperwork.

It creates a real Minnesota electorate.

Do not choose B if Impact Makers' actual polity says the parent body itself chooses branch trustees rather than merely confirming locally selected people.

### C — Actor / office / capacity separation

C applies regardless of A or B.

Every important act should identify:

WHO acted?
IN WHAT OFFICE?
FOR WHICH ENTITY/BODY?
FROM WHAT SOURCE OF AUTHORITY?
WHAT POWER was exercised?
WHAT concurrence was required?
WHAT condition made it effective?

This prevents the invalid inference:

same human => same authority

## 6. Architecture currently supported by the evidence

This is not final drafting.

IMPACT MAKERS / NIGERIA
|
+-- doctrine
+-- ecclesiastical identity
+-- branch recognition
+-- ministerial / office recognition
+-- trustee appointment OR confirmation
    only where actual governing law supplies it
             |
             v
      MINNESOTA RELIGIOUS SOCIETY
      ecclesiastical body
      see section 315.08 distinction
             |
             | civil membrane
             v
      MINNESOTA CORPORATION
             |
       local trustees
             |
+-- banking
+-- contracts
+-- local liabilities
+-- accounting / records
+-- property title
+-- restricted gifts
+-- foreign grants / domestic charitable control

Separate optional property layer:

PROPERTY TRUST / REVERSION

exists only when deliberately constituted through a legally effective civil instrument.

## 7. New ALEX primitive — PROVENANCE-GATED-COMPOSITION

A graph path is not an authority grant.

Nigeria
    --appoints-->
Trustee

Trustee
    --may sign-->
Bank Account

does not imply:

Nigeria
    --may sign-->
Bank Account

Similarly:

Denomination
    --affiliated-with-->
Local Church

Local Church
    --owns-->
Property

does not imply:

Denomination
    --owns-->
Property

Therefore:

PATH EXISTS != AUTHORITY COMPOSES

Authority composition must be explicitly permitted by the source governing the relation.

This composes with existing Collective laws:

RECEIPT != AUTHORITY
SELECTION != EVIDENCE
APPOINTMENT != OWNERSHIP
OFFICE != BANK AUTHORITY
ECCLESIASTICAL DECISION != PROPERTY TRANSFER
PROPERTY TITLE != DOCTRINAL AUTHORITY
GRANT REQUEST != GRANT APPROVAL

## 8. Information now needed from Impact Makers

The next discriminator is not more abstract Minnesota research.

It is the ministry's real governing corpus.

Request:

1. Exact official/legal name of the Nigerian ministry.
2. Official registration certificate / registered-trustee document / registry extract.
3. Current constitution, bylaws, charter, canon, rules, or usages.
4. Provisions governing creation/recognition of branches outside Nigeria.
5. Identity of the actor/body authorized to establish a branch.
6. Identity of the actor/body authorized to choose branch trustees/officers.
7. Whether local members choose leaders subject to upstream confirmation.
8. Authority to remove or replace branch trustees/officers.
9. Titles of the relevant offices.
10. Succession rules for those offices.
11. Acts requiring joint concurrence or multiple signatories.
12. Existing allocation of doctrine, ministry credentials, branch recognition, discipline, use of name, trustee appointment/confirmation, and temporal/property/financial management.
13. Existing rule concerning ownership, trust, reversion, or retention of branch property.
14. Existing branch charter, appointment letter, affiliation covenant, or equivalent specimen.

Highest-value evidence:

official registration
+ actual governing constitution
+ branch-establishment authority
+ trustee appointment / confirmation authority
+ office succession rules

## 9. Ready-to-send handoff

We've been researching how to establish the Minnesota branch in a way that faithfully preserves Impact Makers' actual ecclesiastical relationship with the ministry in Nigeria while keeping the Minnesota civil/property structure clear.

Minnesota law appears capable of supporting genuine denominational hierarchy without treating ecclesiastical authority, corporate authority, and property ownership as the same thing.

We found two especially plausible structures:

A. Direct appointment. If Impact Makers' existing constitution, rules, or established usages give an identified leader, board, council, or other governing body authority to appoint trustees or officers of branches, Minnesota has a religious-corporation formation route specifically designed for trustees selected by a minister, officers, or denominational body.

B. Local election with parent confirmation. Minnesota precedent also recognizes a structure where the local congregation elects trustees, but the election does not become effective until it is confirmed by the appropriate higher church authority.

We do not want to choose a Minnesota structure first and then rewrite Impact Makers to fit it. We want the Minnesota structure to reflect how the ministry is actually governed.

Could you help us establish that by sending or explaining:

1. the exact official/legal name of the Nigerian ministry and its registration document, if available;
2. the current constitution, bylaws, charter, canon, rules, or other governing instrument;
3. any provisions dealing with branches, churches, missions, campuses, or ministries outside Nigeria;
4. who has authority to establish or recognize a branch;
5. who has authority to choose, appoint, approve, confirm, remove, or replace branch leaders/trustees;
6. whether local members choose leaders subject to parent approval/confirmation;
7. if the parent chooses leaders directly, which specific person/body performs the appointment;
8. the official titles of the relevant offices and how succession works;
9. whether important acts require joint action or multiple signatories;
10. which matters belong to the parent ministry ecclesiastically and which are handled locally;
11. whether any rule already addresses branch property ownership, trust, reversion, or retention; and
12. whether Impact Makers already uses a branch charter, appointment letter, affiliation covenant, or similar instrument.

One distinction has become especially important: the same person can act in several capacities without those capacities becoming legally identical. So it helps if we know not only who exercises a power, but in what office/capacity and under what source of authority.

Existing documents and an explanation of actual ministry practice are preferable to creating new documents at this stage.

Once those are in hand, the next task is to map the real Impact Makers polity against A/B/C and give Minnesota church/nonprofit counsel a narrow architecture to validate/redline rather than a blank-sheet question.

## 10. Next stop condition

Do not choose A or B until the Nigerian governing corpus is obtained or explicitly unavailable.

After receipt:

source document
    -> authority extraction
    -> actor / office / capacity graph
    -> A vs B vs bounded hybrid
    -> Minnesota statutory fit
    -> property / fiduciary separation
    -> counsel validation

If documents contradict the current model, preserve the contradiction. Do not repair the polity by inference.

## Source loci

- Minnesota Chapter 315: https://www.revisor.mn.gov/statutes/cite/315/full
- Section 315.01: https://www.revisor.mn.gov/statutes/cite/315.01
- Russian-Serbian Holy Trinity Church v. Kulik: https://law.justia.com/cases/minnesota/supreme-court/1938/202-minn-560.html
- Piletich v. Deretich: https://law.justia.com/cases/minnesota/supreme-court/1982/81-1247-1.html
- Presbytery of the Twin Cities Area v. Eden Prairie Presbyterian Church: https://law.justia.com/cases/minnesota/court-of-appeals/2017/a16-0945.html
- United Islamic Society v. Masjed Abubakr Al-Seddiq: https://law.justia.com/cases/minnesota/court-of-appeals/2016/a16-0140.html
- Eller v. Diocese of St. Cloud: https://law.justia.com/cases/minnesota/court-of-appeals/2006/opa050828-0124.html
- Archdiocese bankruptcy appeal: https://law.justia.com/cases/federal/appellate-courts/ca8/17-1079/17-1079-2018-04-26.html

## Receipt

Created: 2026-09-18
Research context: follow-on deep dig from MN-CHURCH-LEGAL-BEDROCK-001
Durable target: ALEX.2 research branch
Promotion: none
Open frontier: actual Impact Makers governing documents determine A/B/C
