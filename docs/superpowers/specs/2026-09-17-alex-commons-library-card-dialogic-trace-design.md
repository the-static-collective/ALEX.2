# ALEX COMMONS / LIBRARY-CARD-001 + DIALOGIC TRACE

**Date:** 2026-09-17  
**Status:** approved architecture / implementation not yet claimed / awaiting human review  
**Owner:** ALEX.2  
**Scope:** contributor intake, pseudonymous continuity, living-source dialogue, provenance, privacy, rights, and authority boundaries

## Design sentence

> ALEX may accept attributable or anonymous contributions from living people, including through privacy-preserving transports such as Tor, while keeping contributor identity, transport privacy, source provenance, evidentiary weight, publication rights, and claim authority explicitly separate.

The corresponding living-source research rule is:

> **DO NOT MERELY INTERPRET A REACHABLE SOURCE. BUILD A MODEL PRECISE ENOUGH THAT THEY CAN BREAK IT.**

And the hard correction is:

> **THEIR CORRECTION CHANGES OUR MODEL. IT DOES NOT CHANGE THE PAST.**

---

## 1. Problem

ALEX currently has strong machinery for source witnesses, transformations, PRESSURE, formation trace, and receipts. It does not yet have a first-class model for two related situations:

1. a living contributor wants to add a witness, correction, counterexample, lead, transcription, source pointer, or response to the library without necessarily exposing a civil identity; and
2. the creator, author, researcher, witness, maintainer, or other living source being interpreted is reachable and can directly clarify, dispute, or refine the model ALEX has built.

These are not ordinary account-management problems.

They are provenance problems with identity, privacy, and authority consequences.

ALEX must be able to preserve:

    useful contribution
    without requiring civil identity

and:

    creator response
    without laundering response into universal truth

and:

    persistent continuity
    without requiring deanonymization

and:

    anonymous transport
    without pretending anonymity implies trust

---

## 2. Existing constitutional laws remain in force

This design extends the current floor. It does not replace it.

Existing laws that directly govern this design:

    custody != authority
    public access != redistribution permission
    received premise != admitted premise
    agreement != independent corroboration
    discovery path != evidence path
    breadcrumb != evidence
    access != permission to redistribute
    successful execution != evidentiary correctness

New laws:

    identity != contribution authority
    contributor continuity != civil identity
    transport privacy != evidentiary trust
    anonymity != source independence
    verified identity != verified claim
    creator agreement != independent corroboration
    creator disagreement != automatic falsification
    current stated intent != historical intent
    silence != rejection
    question wording != neutral observation
    deposit != admission
    deposit != publication
    receipt != promotion
    capability != authority

---

## 3. Architecture overview

ALEX COMMONS is the outer contribution architecture.

LIBRARY-CARD-001 is its capability / continuity layer.

DIALOGIC TRACE is a research protocol that can operate through the Commons when a living source is reachable.

    contributor / creator
        |
        v
    transport adapter
      clearnet | onion | local | imported correspondence
        |
        v
    intake envelope
        |
        +--> optional library card / contributor key
        |
        v
    quarantine + rights cut
        |
        v
    immutable deposit receipt
        |
        v
    ALEX witness / question / response records
        |
        v
    PRESSURE / COMPARE / TRACE / DIALOGIC TRACE
        |
        v
    proposal / refusal / model delta
        |
        v
    human or owning-project admission gate

No transport grants semantic privilege.

No contributor role grants claim authority.

No response rewrites a prior artifact.

---

## 4. LIBRARY-CARD-001

### 4.1 Purpose

A library card is a bounded capability and continuity object.

It answers:

> What may this contributor do here, and which prior deposits may they lawfully claim continuity with?

It does **not** answer:

> Who is this person in civil life?

and does not answer:

> Are their claims true?

### 4.2 Contributor modes

ALEX COMMONS should support at least four contributor modes:

#### NAMED

A contributor voluntarily supplies a public identity.

A named identity remains a claim until supported by an appropriate identity-verification record when verification matters.

#### VERIFIED_NAMED

A separate identity-attestation path supports the claimed public identity.

Verification establishes attribution only within the declared verification scope.

    verified person
    !=
    verified interpretation

#### PERSISTENT_PSEUDONYM

A contributor controls a stable pseudonymous key or credential and can prove continuity across deposits without disclosing civil identity.

The exact signature / credential mechanism is an implementation decision and must use established audited cryptographic libraries and standard formats. No custom cryptography.

#### ONE_SHOT_ANONYMOUS

No durable contributor identity is required.

The deposit receives its own immutable receipt. Optional return capability may allow later follow-up without creating a globally stable identity.

Anonymous contribution is a supported state, not a malformed account.

---

## 5. Card identity and capability

Candidate record:

    library_card
      card_id
      mode
      public_label?
      contributor_key_id?
      identity_attestation_ids[]?
      capabilities[]
      created_at
      expires_at?
      revoked_at?
      continuity_parent?
      authority = none

Candidate capabilities:

    deposit_source_pointer
    deposit_bytes
    deposit_reading
    deposit_correction
    deposit_counterexample
    deposit_question_response
    deposit_rights_statement
    retrieve_own_receipts
    append_to_own_deposit
    prove_continuity

Capabilities are transport / workflow permissions.

They are not evidence classes.

They are not admission rights.

Hard law:

> **THE CARD OPENS DOORS. IT DOES NOT DECIDE WHAT BELONGS ON THE SHELF.**

---

## 6. Deposit envelope

Every contribution enters through an explicit envelope.

Candidate record:

    commons_deposit
      deposit_id
      received_at
      transport_class
      card_id?
      contributor_mode
      contributor_claims[]
      source_locators[]
      held_artifact_ids[]
      proposed_relations[]
      rights_testimony
      privacy_request
      publication_permission
      reply_capability?
      content_digest
      quarantine_status
      ingest_result
      authority = none

Transport classes may include:

    CLEARNET
    ONION_SERVICE
    LOCAL
    IMPORTED_CORRESPONDENCE
    CONNECTOR
    OTHER_DECLARED

The transport class is provenance.

It must never be used as a credibility score.

---

## 7. Tor / onion-service boundary

Tor support belongs in the transport layer only.

An ALEX onion endpoint may provide a privacy-preserving path for:

- one-shot anonymous deposits;
- persistent pseudonymous deposits;
- retrieval of deposit receipts;
- optional reply / follow-up channels.

Tor Project documentation describes onion services as Tor-only services that provide location-hiding properties and end-to-end authenticated / encrypted transport between client and onion service.

References:

- https://support.torproject.org/tor-browser/features/onion-services/
- https://community.torproject.org/onion-services/overview/
- https://community.torproject.org/onion-services/setup/

ALEX must **not** infer from use of Tor:

    contributor identity
    contributor honesty
    source independence
    source ownership
    permission to redistribute
    freedom from endpoint compromise
    freedom from traffic-correlation or operational-security failure
    universal anonymity

### 7.1 Logging rule

For privacy-preserving intake, collect the minimum metadata required to operate the receipt and abuse boundary.

Do not retain transport metadata merely because a web stack exposes it by default.

The implementation must explicitly inventory:

    server logs
    reverse-proxy logs
    application logs
    exception traces
    analytics
    rate-limit state
    uploaded-file metadata
    timestamps
    reply tokens

and declare which are retained, for how long, and why.

### 7.2 No custom anonymity claims

The UI and receipts must not promise “untraceable,” “fully anonymous,” or equivalent absolute guarantees.

Use bounded language describing the actual transport and retained metadata.

### 7.3 Separation of onion identity and contributor identity

The onion service address authenticates the service endpoint.

It does not identify a contributor.

A contributor key authenticates continuity with that key.

It does not identify a civil person.

Keep:

    onion service identity
    !=
    contributor key identity
    !=
    civil identity

---

## 8. Quarantine and hostile-content boundary

Every untrusted deposit is inert on arrival.

ALEX COMMONS must assume submitted files may be malformed, malicious, illegal to redistribute, privacy-sensitive, or evidentially worthless.

Initial quarantine rules:

- never execute uploaded content;
- never load macros or embedded scripts;
- do not trust filenames or declared MIME types;
- hash bytes before further processing;
- inspect file type through bounded tooling;
- separate archive expansion from intake;
- impose size / count / recursion limits;
- preserve rejected-deposit receipts without preserving dangerous bytes when retention would be unsafe or unlawful;
- run extractors and converters under least privilege;
- do not expose internal filesystem paths or credentials in error messages;
- do not make public publication the default consequence of successful intake.

A successful deposit means:

    ALEX received something

not:

    ALEX endorses it

and not:

    ALEX may republish it

---

## 9. Rights, privacy, and publication

A deposit needs separate declarations for:

    may ALEX hold this?
    may ALEX process this?
    may ALEX quote this?
    may ALEX publish this?
    may ALEX reveal contributor identity?
    may ALEX contact / reply?

These must not collapse into one checkbox.

A contributor may, for example:

- permit private research use but forbid public redistribution;
- permit quotation but not file publication;
- allow public attribution under a pseudonym but not a civil identity;
- permit a private response to be used only as a search lead;
- explicitly release a contribution for public redistribution.

Default when unclear:

    hold / process only within the authorized research boundary
    publication permission = unresolved

---

## 10. Source independence and Sybil resistance

ALEX must not convert account count, card count, pseudonym count, or deposit count into independent corroboration.

Hard law:

> **TEN CARDS MAY STILL BE ONE WITNESS.**

If multiple contributions share:

- identical source bytes;
- identical phrasing;
- shared citations;
- known common upstream source;
- cryptographic continuity;
- obvious derivative ancestry;
- unresolved possible common ancestry,

the dependency relation must remain visible.

Unknown identity means:

    independence = unknown

not:

    independence = independent

No reputation or contribution score may become claim truth.

---

## 11. DIALOGIC TRACE

### 11.1 Use

Use DIALOGIC TRACE when:

- a living creator, author, researcher, witness, maintainer, or other relevant source is reachable;
- ALEX has already formed a sufficiently precise reading or model;
- a direct response could discriminate between live interpretations;
- contacting the source is lawful, appropriate, and authorized.

Do not use direct contact as a substitute for reading the public work first.

### 11.2 Core loop

    PUBLIC ARTIFACT
      -> ALEX READING
      -> MODEL / HYPOTHESIS
      -> PRESSURE
      -> QUESTION
      -> SOURCE RESPONSE
      -> RESPONSE CLASSIFICATION
      -> MODEL DELTA
      -> INDEPENDENT RETEST
      -> SURVIVOR / REFUSAL / OPEN

### 11.3 Core law

> **A creator may clarify their present position. They do not retroactively rewrite the artifact already in evidence.**

Keep:

    artifact meaning as evidenced
    !=
    creator current explanation
    !=
    creator historical intent
    !=
    independent truth of external claim

---

## 12. Dialogic records

### QUESTION

    source_question
      question_id
      target_person_or_role
      target_identity_status
      derived_from_claim_ids[]
      exact_question
      framing_notes
      leading-risk
      sent_at?
      channel?
      public_or_private
      publication_permission
      status

Possible status:

    DRAFT
    SENT
    ANSWERED
    DECLINED
    UNANSWERED
    UNDELIVERABLE
    WITHDRAWN

### RESPONSE

    source_response
      response_id
      question_id
      responder_claimed_identity
      responder_identity_status
      received_at
      channel
      public_or_private
      exact_carrier_or_message_ref
      quotation_permission
      publication_permission
      content_digest?
      response_reading
      authority = bounded

### RESPONSE RELATIONS

Useful typed relations:

    clarifies_current_position
    clarifies_current_intent
    disputes_our_reading
    confirms_our_reading
    corrects_factual_claim
    supplies_source
    supplies_counterexample
    opens_discriminator
    refuses_question
    declines_publication
    claims_historical_intent
    claims_authorship
    claims_provenance

These relation labels describe what the response is doing.

They do not determine whether the claim is independently established.

---

## 13. MODEL DELTA

A DIALOGIC TRACE is incomplete if the response is merely appended as an interesting quote.

It must show what changed.

Candidate:

    model_delta
      delta_id
      pre_response_model_id
      response_id
      post_response_model_id
      changed_claims[]
      unchanged_claims[]
      killed_claims[]
      new_questions[]
      new_source_paths[]
      response_dependent_claims[]
      independently_retested_claims[]
      residual_disagreement[]
      created_at

Required questions:

    What did we believe before asking?
    What exactly did they say?
    Which parts of our model changed?
    Which parts did not change?
    Which changes depend only on their testimony?
    Which changes survived independent checking?
    What remains disputed?

This prevents conversational charisma from becoming invisible model drift.

---

## 14. Evidence classes for living-source replies

A living-source response can be strong evidence for some propositions and weak or irrelevant evidence for others.

### Stronger candidates

Subject to identity and carrier verification, a source may bear directly on:

    “This is my current view.”
    “I intended X when I wrote this,” as present testimony about past intent.
    “I authored / did not author this,” as testimony requiring ordinary provenance pressure.
    “This is the source I was relying on.”
    “That wording was an error.”
    “I no longer hold that position.”

### Not automatically established

A creator response does not automatically establish:

    that the artifact objectively means what they now say
    that their memory of historical intent is infallible
    that an external factual claim is true
    that a mathematical derivation is valid
    that a historical genealogy is real
    that agreement from the creator is independent corroboration
    that disagreement kills an independently supported reading

ALEX should preserve both the artifact path and response path when they diverge.

---

## 15. Hostile controls

### AGREEABLE-AUTHOR TRAP

Given:

    ALEX interpretation
    -> creator says “yes, exactly”

Attempt:

    therefore interpretation independently proven

Required result:

    refuse independent corroboration
    preserve agreement as creator response
    continue external evidence path where needed

### RETROSPECTIVE-INTENT TRAP

Given a creator’s current recollection of what they meant years earlier, attempt to overwrite the earlier artifact or contemporaneous evidence.

Required result:

    preserve current testimony
    preserve earlier artifact unchanged
    classify historical intent as testimony subject to memory / chronology pressure

### AUTHORITY LAUNDERING

Given a famous or credentialed contributor, attempt to promote every attached claim.

Required result:

    identity / credentials may contextualize expertise
    each claim still requires its appropriate evidence path

### LEADING-QUESTION CONTAMINATION

Given a question that embeds ALEX’s preferred answer, attempt to treat agreement as spontaneous confirmation.

Required result:

    preserve exact question wording
    mark leading-risk
    downgrade what agreement can establish
    prefer a less-leading follow-up discriminator

### SILENCE INFERENCE

Given no reply, attempt:

    silence = rejection
    silence = agreement
    silence = inability to answer

Required result:

    UNANSWERED only

### PRIVATE-CORRESPONDENCE LEAKAGE

Given a private response with no publication permission, attempt to commit quotation or distinctive private content to a public repository.

Required result:

    refuse publication
    preserve restricted receipt / metadata only as authorized
    rebuild public evidence path independently

### PSEUDONYM MULTIPLICITY

Given several pseudonymous cards supporting one claim, attempt to count them as independent witnesses.

Required result:

    independence unknown unless independently established

### TOR TRUST LAUNDERING

Given a Tor-origin deposit, attempt to describe it as safer, more authentic, whistleblower-originated, or more credible because it arrived through Tor.

Required result:

    transport class only
    no semantic promotion

### CREATOR-VETO TRAP

Given a creator who rejects a well-supported interpretation of their published artifact, attempt to delete the interpretation.

Required result:

    preserve disagreement
    distinguish authorial testimony from artifact-based argument
    let evidence paths remain independently inspectable

---

## 16. First laboratories

These are test laboratories, not privileged authorities.

### LAB A — ongoing AI / human-office discourse

Target class:

    living broadcaster / theologian / creator discussing AI

Example research question family:

> When AI can reproduce the surface output of a human creative or ministerial act, what part of the act remains constituted by relationship, responsibility, formation, office, or witness?

Test value:

- public corpus exists over time;
- creator / guests may remain reachable;
- current view may evolve;
- external technical and theological claims can be independently checked;
- creator response is relevant but cannot settle technical AI facts by itself.

### LAB B — unconventional mathematical / ontological claims

Target class:

    living creator proposing nonstandard mathematical or operator claims

Example discriminator:

> Is the claim changing the definition of multiplication, changing the object type, or asserting an additional transformation between the operation and observed result?

Test value:

- forces literalization;
- separates operator semantics from metaphor;
- permits the creator to reject ALEX’s reconstruction;
- mathematical validity remains independently testable after response.

Neither laboratory should be hard-coded into the protocol.

---

## 17. Interaction with PRESSURE

DIALOGIC TRACE normally begins **after** enough PRESSURE has occurred to make the question discriminating.

Preferred relation:

    H0
      -> literalize
      -> attack
      -> corrected live model
      -> DIALOGIC QUESTION
      -> RESPONSE
      -> MODEL DELTA
      -> PRESSURE AGAIN

A source should not be asked to adjudicate an interpretation ALEX has not first made precise.

The source response may:

    strengthen
    weaken
    split
    kill
    redirect
    leave unchanged

the model.

It must never silently rewrite H0.

---

## 18. Interaction with formation trace

The question and response are also formation events.

Preserve:

    public artifact -> our reading
    our reading -> question
    question wording -> response
    response -> model delta

But:

    response caused new search
    !=
    response independently supports what search later found

A creator’s reply can be both:

- evidence for their stated position; and
- a breadcrumb that motivates a new independent evidence path.

Those roles must remain typed separately.

---

## 19. Interaction with ALEX Commons

DIALOGIC TRACE does not require the Commons.

A response may arrive by:

    public interview
    email
    letter
    direct message
    forum post
    repository comment
    recorded conversation
    Commons deposit
    onion-service deposit

The Commons simply gives ALEX a native contribution / reply channel with explicit provenance and privacy semantics.

A living source may choose:

    verified named participation
    named unverified participation
    persistent pseudonym
    one-shot anonymous response

The evidentiary consequence depends on the claim being made.

For example:

    anonymous response may open a discriminator
    but cannot establish “the author says...” without an identity path

---

## 20. Minimal implementation slice

Do not begin with a public social network.

The first implementation should prove only:

1. local / test HTTP deposit envelope;
2. one-shot anonymous and persistent-pseudonymous modes;
3. immutable deposit receipts;
4. quarantine state with inert test fixtures;
5. separate publication / quotation / identity permissions;
6. a DIALOGIC TRACE record set:
   - public artifact reference;
   - model;
   - question;
   - response;
   - model delta;
7. hostile fixtures for the traps in §15;
8. export to inspectable JSON / JSON Lines;
9. no automatic claim admission;
10. no production Tor endpoint yet.

### Why Tor is not gate 1

Tor is valuable, but privacy transport should be attached to a sound intake contract rather than used to discover the contract.

First prove:

    clearnet/local test transport
      -> same deposit semantics
      -> same receipt
      -> same quarantine
      -> same authority boundaries

Then add an onion-service adapter whose semantic output is identical except for declared transport metadata.

Hard law:

> **TRANSPORT MUST BE REPLACEABLE WITHOUT CHANGING EVIDENCE SEMANTICS.**

---

## 21. Later Tor gate

A later Onion Service gate is earned only when:

- the intake endpoint is stateless or has declared state;
- logs and retained metadata have been audited;
- contributor key continuity works without civil identity;
- quarantine is enforced;
- upload limits and abuse controls exist;
- dangerous file handling is isolated;
- rights / publication controls are explicit;
- documentation avoids absolute anonymity promises;
- operator secrets and onion-service keys have a documented storage / rotation / backup policy;
- a threat-model document states what ALEX does and does not protect against.

No Tor deployment should precede this gate merely because the route is easy to expose.

---

## 22. Suggested record additions to the ALEX evidence model

Future implementation may add:

    contributor
    identity_attestation
    library_card
    commons_deposit
    rights_statement
    source_question
    source_response
    model_delta

Candidate relations:

    deposited
    signed_by
    continuity_with
    claims_identity
    identity_supported_by
    asks
    answers
    clarifies_current_position
    clarifies_current_intent
    disputes_our_reading
    confirms_our_reading
    supplies_source
    opens_discriminator
    publication_authorized_by
    quotation_authorized_by

Avoid:

    same_as

unless exact identity is separately established.

---

## 23. Research-receipt additions

A DIALOGIC TRACE receipt should include:

    TARGET:
    TARGET IDENTITY STATUS:
    PUBLIC ARTIFACT:
    PRE-QUESTION MODEL:
    QUESTION:
    LEADING-RISK:
    CHANNEL:
    PRIVACY / PUBLICATION BOUNDARY:
    RESPONSE:
    RESPONSE IDENTITY STATUS:
    RESPONSE CLASS:
    MODEL DELTA:
    WHAT CHANGED:
    WHAT DID NOT CHANGE:
    RESPONSE-DEPENDENT CLAIMS:
    INDEPENDENT RETEST:
    RESIDUAL DISAGREEMENT:
    NEXT DISCRIMINATOR:
    PROMOTION: none unless separately admitted

A Commons deposit receipt should include:

    DEPOSIT ID:
    CONTRIBUTOR MODE:
    CARD ID (optional):
    TRANSPORT CLASS:
    ARTIFACT DIGEST:
    RIGHTS TESTIMONY:
    PUBLICATION PERMISSION:
    IDENTITY DISCLOSURE PERMISSION:
    QUARANTINE RESULT:
    INGEST RESULT:
    INDEPENDENCE STATUS:
    AUTHORITY: none

---

## 24. Crucible specimens

Add machine-readable hostile specimens before claiming the mode is implemented:

    dialogic-agreeable-author
    dialogic-retrospective-intent
    dialogic-authority-laundering
    dialogic-leading-question
    dialogic-silence
    dialogic-private-leakage
    dialogic-creator-veto
    commons-pseudonym-multiplicity
    commons-tor-trust-laundering
    commons-deposit-is-not-admission
    commons-deposit-is-not-publication
    commons-verified-identity-is-not-verified-claim

Expected dispositions should include ACCEPT / REFUSE / UNRESOLVED / INSUFFICIENT_TO_TEST following the existing Crucible contract.

---

## 25. Non-goals

This design does not create:

- a social network;
- a public reputation economy;
- anonymous voting on truth;
- contributor tokens or financial rewards;
- a decentralized blockchain;
- a moderation-free upload dump;
- a guarantee of anonymity;
- a whistleblower publication platform;
- automatic publication;
- automatic source verification;
- creator veto over interpretation;
- creator supremacy over independent evidence;
- civil-identity requirements for ordinary contribution;
- a universal ontology of authorship.

Future systems may build on these receipts. They do not belong in the first slice.

---

## 26. Acceptance tests for the architecture

The design is coherent only if all of these can be true simultaneously:

### Anonymous useful deposit

A one-shot anonymous contributor deposits a valid page pointer.

Expected:

    deposit accepted
    identity unknown
    source pointer independently verified
    contributor identity remains unnecessary
    finding may become evidence through source verification

### Anonymous bad claim

A Tor-origin anonymous contributor deposits an unsupported interpretation.

Expected:

    deposit preserved as attributable occurrence
    interpretation not admitted
    Tor origin grants no credibility

### Persistent pseudonym

A pseudonymous contributor proves continuity with two earlier deposits.

Expected:

    continuity established
    civil identity remains unknown
    independence between those three deposits is not claimed

### Verified creator response

A verified creator says ALEX misunderstood their current position.

Expected:

    creator response admitted as evidence of current stated position
    prior public artifact remains unchanged
    model delta recorded
    artifact interpretation re-evaluated rather than erased

### Creator agrees

A creator strongly agrees with ALEX’s interpretation.

Expected:

    agreement preserved
    independent corroboration not claimed
    external factual claims remain independently testable

### Creator disputes mathematics

A living creator rejects ALEX’s reconstruction of a mathematical claim.

Expected:

    reconstruction updated if it misrepresented the claim
    mathematical validity still tested independently

### Private source

A private correspondent supplies a high-value source lead but forbids quotation.

Expected:

    private message not published
    lead preserved as discovery path only
    public evidence rebuilt from the supplied source if accessible

### Rights mismatch

A contributor uploads a copyrighted scan while allowing research but not redistribution.

Expected:

    acquisition / processing may proceed within authorized boundary
    public file publication refused
    citations / quotations follow separate permission and legal boundaries

---

## 27. Implementation order after spec approval

1. Extend evidence-model and research-receipt schemas in prose.
2. Add DIALOGIC TRACE reference mode.
3. Add Crucible fixtures.
4. Implement minimal local/test Commons deposit contract.
5. Implement persistent-pseudonym continuity with established cryptographic tooling.
6. Implement quarantine / rights state machine.
7. Add DIALOGIC TRACE machine-readable records and model-delta validation.
8. Run hostile fixtures.
9. Only then design and audit the Tor Onion Service transport adapter.
10. Treat any public deployment as a separate operational-security gate.

---

## 28. Seal

    ANYONE MAY BRING A BOOK TO THE DOOR.
    THE DOOR DOES NOT HAVE TO PRETEND IT KNOWS WHO BROUGHT IT.
    THE SHELF STILL HAS TO KNOW WHAT THE BOOK IS.

    IDENTITY != CONTRIBUTION AUTHORITY
    CONTRIBUTOR CONTINUITY != CIVIL IDENTITY
    TRANSPORT PRIVACY != EVIDENTIARY TRUST
    DEPOSIT != ADMISSION
    DEPOSIT != PUBLICATION
    VERIFIED IDENTITY != VERIFIED CLAIM

    DO NOT MERELY INTERPRET A REACHABLE SOURCE.
    BUILD A MODEL PRECISE ENOUGH THAT THEY CAN BREAK IT.

    CREATOR RESPONSE != RETROACTIVE PROOF
    CURRENT INTENT != PAST INTENT
    AGREEMENT != INDEPENDENT CORROBORATION
    SILENCE != REJECTION

    THEIR CORRECTION CHANGES OUR MODEL.
    IT DOES NOT CHANGE THE PAST.
