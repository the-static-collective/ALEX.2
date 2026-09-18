# ALEX COMMONS / LIBRARY-CARD-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a transport-agnostic ALEX contribution intake slice with anonymous and persistent-pseudonymous contributor modes, immutable deposit receipts, rights/publication separation, quarantine state, and no automatic evidentiary promotion.

**Architecture:** Add a small `alex_runtime.commons` evaluator layer for library cards, deposits, permissions, and pseudonymous continuity. Keep the first slice local/test-only; Tor remains a later adapter whose output must be semantically identical to the local transport contract. Use standard-library validation everywhere except pseudonymous continuity, which uses Ed25519 from the established `cryptography` package rather than custom cryptography.

**Tech Stack:** Python 3, `unittest`, JSON-like dictionaries, existing `alex_runtime.digests.sha256_json`, `cryptography` Ed25519 only for continuity proof.

**Spec:** `docs/superpowers/specs/2026-09-17-alex-commons-library-card-dialogic-trace-design.md`

## Global Constraints

- `identity != contribution authority`
- `contributor continuity != civil identity`
- `transport privacy != evidentiary trust`
- `anonymity != source independence`
- `verified identity != verified claim`
- `deposit != admission`
- `deposit != publication`
- `capability != authority`
- No custom cryptography.
- Untrusted deposits are inert on arrival.
- No production Tor endpoint in this slice.
- Publication, quotation, identity disclosure, holding, and processing permissions remain separate.
- Incoming `authority` is never propagated; Commons receipts use `authority: "none"`.

---

## File map

- Create `alex_runtime/commons.py` — card, permission, deposit, quarantine, and continuity evaluators.
- Create `tests/test_commons.py` — unit coverage for anonymous/pseudonymous/rights/quarantine behavior.
- Create `requirements.txt` — only if the repository has no dependency manifest at execution time; add `cryptography` as the single runtime dependency.
- Create `crucible/specimens/commons-*.json` — constitutional hostile fixtures.
- Modify `crucible/README.md` — register Commons fixture family.
- Modify `skills/alex/references/evidence-model.md` — add contributor/card/deposit/rights records.
- Modify `skills/alex/references/research-receipt.md` — add Commons deposit receipt form.
- Create `tools/run_commons_intake.py` — local JSON stdin/file runner; no server/network listener.

---

### Task 1: Document Commons records and receipts

**Files:**
- Modify: `skills/alex/references/evidence-model.md`
- Modify: `skills/alex/references/research-receipt.md`

**Interfaces:**
- Produces record vocabulary used by the runtime:
  - `library_card`
  - `commons_deposit`
  - `rights_statement`
  - `identity_attestation`
  - `contributor`

- [ ] **Step 1: Extend evidence-model records**

Add rows:

```markdown
| `contributor` | A declared contributor identity surface or anonymous state | Civil identity, honesty, independence, or claim truth |
| `identity_attestation` | Bounded support for a claimed identity within a declared scope | Truth of claims made by that identity |
| `library_card` | Capabilities and continuity for one contributor handle/key | Evidentiary authority |
| `commons_deposit` | One received contribution occurrence, transport class, rights state, and digest | Admission, publication, or independent corroboration |
| `rights_statement` | Declared permissions for hold/process/quote/publish/identity disclosure/reply | Ownership beyond the declaration or legal sufficiency outside scope |
```

Add hard boundaries:

```text
identity != contribution authority
contributor continuity != civil identity
transport privacy != evidentiary trust
deposit != admission
deposit != publication
```

- [ ] **Step 2: Add Commons compact receipt**

Add:

```text
DEPOSIT ID:
CONTRIBUTOR MODE:
CARD ID:
TRANSPORT CLASS:
ARTIFACT DIGEST:
RIGHTS TESTIMONY:
HOLD PERMISSION:
PROCESS PERMISSION:
QUOTATION PERMISSION:
PUBLICATION PERMISSION:
IDENTITY DISCLOSURE PERMISSION:
REPLY PERMISSION:
QUARANTINE RESULT:
INGEST RESULT:
INDEPENDENCE STATUS:
AUTHORITY: none
```

- [ ] **Step 3: Run documentation consistency check**

```bash
python - <<'PY'
from pathlib import Path
text = (
    Path("skills/alex/references/evidence-model.md").read_text(encoding="utf-8")
    + Path("skills/alex/references/research-receipt.md").read_text(encoding="utf-8")
)
for item in ["library_card", "commons_deposit", "deposit != admission", "AUTHORITY: none"]:
    assert item in text, item
print("commons docs: OK")
PY
```

Expected: `commons docs: OK`

- [ ] **Step 4: Commit**

```bash
git add skills/alex/references/evidence-model.md skills/alex/references/research-receipt.md
git commit -m "docs: define commons contribution records"
```

---

### Task 2: Implement library-card validation

**Files:**
- Create: `alex_runtime/commons.py`
- Create: `tests/test_commons.py`

**Interfaces:**
- Produces:
  - `evaluate_library_card(record: object) -> dict[str, Any]`
- Card modes:
  - `NAMED`
  - `VERIFIED_NAMED`
  - `PERSISTENT_PSEUDONYM`
  - `ONE_SHOT_ANONYMOUS`

- [ ] **Step 1: Write failing card tests**

Create:

```python
import copy
import unittest

from alex_runtime.commons import evaluate_library_card

BASE_CARD = {
    "schema": "alex.library-card/v0",
    "card_id": "card:pseudo:001",
    "mode": "PERSISTENT_PSEUDONYM",
    "public_label": "reader-7",
    "contributor_key_id": "ed25519:reader-7",
    "capabilities": [
        "deposit_source_pointer",
        "deposit_counterexample",
        "retrieve_own_receipts",
        "prove_continuity",
    ],
    "authority": "canon",
}

class LibraryCardTests(unittest.TestCase):
    def test_accepts_pseudonymous_card_without_civil_identity(self):
        result = evaluate_library_card(copy.deepcopy(BASE_CARD))
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["mode"], "PERSISTENT_PSEUDONYM")
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertNotIn("civil_identity", result["receipt"])

    def test_one_shot_anonymous_does_not_require_key(self):
        record = copy.deepcopy(BASE_CARD)
        record["card_id"] = "card:anon:001"
        record["mode"] = "ONE_SHOT_ANONYMOUS"
        record.pop("contributor_key_id")
        result = evaluate_library_card(record)
        self.assertEqual(result["disposition"], "ACCEPT")

    def test_duplicate_capability_refuses(self):
        record = copy.deepcopy(BASE_CARD)
        record["capabilities"].append("deposit_counterexample")
        result = evaluate_library_card(record)
        self.assertEqual(result["reason"], "invalid_capabilities")
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_commons.LibraryCardTests -v
```

Expected: import failure because `alex_runtime.commons` does not yet exist.

- [ ] **Step 3: Implement card evaluator**

Use:

```python
CARD_SCHEMA = "alex.library-card/v0"
CARD_RESULT_SCHEMA = "alex.library-card-result/v0"

CARD_MODES = frozenset({
    "NAMED",
    "VERIFIED_NAMED",
    "PERSISTENT_PSEUDONYM",
    "ONE_SHOT_ANONYMOUS",
})

CAPABILITIES = frozenset({
    "deposit_source_pointer",
    "deposit_bytes",
    "deposit_reading",
    "deposit_correction",
    "deposit_counterexample",
    "deposit_question_response",
    "deposit_rights_statement",
    "retrieve_own_receipts",
    "append_to_own_deposit",
    "prove_continuity",
})
```

Rules:

```text
- card_id and mode required
- capabilities non-empty unique subset of CAPABILITIES
- PERSISTENT_PSEUDONYM requires contributor_key_id
- ONE_SHOT_ANONYMOUS does not require identity/key
- incoming authority discarded
- receipt contains card_digest = sha256_json(record)
```

- [ ] **Step 4: Run GREEN**

```bash
python -m unittest tests.test_commons.LibraryCardTests -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/commons.py tests/test_commons.py
git commit -m "feat: add bounded ALEX library cards"
```

---

### Task 3: Implement separated rights and deposit validation

**Files:**
- Modify: `alex_runtime/commons.py`
- Modify: `tests/test_commons.py`

**Interfaces:**
- Produces:
  - `evaluate_rights_statement(record: object) -> dict[str, Any]`
  - `evaluate_commons_deposit(record: object) -> dict[str, Any]`

- [ ] **Step 1: Write failing rights/deposit tests**

Append:

```python
from alex_runtime.commons import evaluate_rights_statement, evaluate_commons_deposit

BASE_RIGHTS = {
    "schema": "alex.rights-statement/v0",
    "rights_id": "rights-001",
    "hold": "YES",
    "process": "YES",
    "quote": "NO",
    "publish": "NO",
    "identity_disclosure": "NO",
    "reply": "YES",
}

BASE_DEPOSIT = {
    "schema": "alex.commons-deposit/v0",
    "deposit_id": "deposit-001",
    "transport_class": "LOCAL",
    "contributor_mode": "ONE_SHOT_ANONYMOUS",
    "card_id": None,
    "source_locators": ["https://example.invalid/source"],
    "held_artifact_refs": [],
    "proposed_relations": ["contextualizes"],
    "rights_statement_ref": "sha256:" + "b" * 64,
    "privacy_request": "PRIVATE",
    "publication_permission": "NO",
    "content_digest": "sha256:" + "c" * 64,
    "quarantine_status": "INERT",
    "ingest_result": "RECEIVED",
    "independence_status": "UNKNOWN",
}

class RightsTests(unittest.TestCase):
    def test_permissions_remain_separate(self):
        result = evaluate_rights_statement(copy.deepcopy(BASE_RIGHTS))
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["publish"], "NO")
        self.assertEqual(result["receipt"]["process"], "YES")

class DepositTests(unittest.TestCase):
    def test_anonymous_local_deposit_is_not_promoted(self):
        result = evaluate_commons_deposit(copy.deepcopy(BASE_DEPOSIT))
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertEqual(result["receipt"]["independence_status"], "UNKNOWN")

    def test_tor_transport_does_not_change_authority(self):
        record = copy.deepcopy(BASE_DEPOSIT)
        record["transport_class"] = "ONION_SERVICE"
        result = evaluate_commons_deposit(record)
        self.assertEqual(result["receipt"]["transport_class"], "ONION_SERVICE")
        self.assertEqual(result["receipt"]["authority"], "none")
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_commons.RightsTests tests.test_commons.DepositTests -v
```

Expected: missing-function failures.

- [ ] **Step 3: Implement rights evaluator**

Use independent permission values:

```python
PERMISSIONS = frozenset({"YES", "NO", "UNRESOLVED"})
RIGHTS_FIELDS = ("hold", "process", "quote", "publish", "identity_disclosure", "reply")
```

Reject missing or unknown permissions. Do not infer `publish=YES` from any other permission.

- [ ] **Step 4: Implement deposit evaluator**

Use:

```python
TRANSPORT_CLASSES = frozenset({
    "CLEARNET",
    "ONION_SERVICE",
    "LOCAL",
    "IMPORTED_CORRESPONDENCE",
    "CONNECTOR",
    "OTHER_DECLARED",
})
CONTRIBUTOR_MODES = CARD_MODES
QUARANTINE_STATUSES = frozenset({"INERT", "CLEARED_METADATA_ONLY", "CLEARED_FOR_PROCESSING", "REJECTED"})
INGEST_RESULTS = frozenset({"RECEIVED", "REFUSED", "HELD", "PROCESSED"})
INDEPENDENCE_STATUSES = frozenset({"UNKNOWN", "DEPENDENT", "PARTIALLY_RESOLVED", "INDEPENDENT_ESTABLISHED"})
```

Rules:

```text
- ONION_SERVICE is stored as transport metadata only
- contributor mode ONE_SHOT_ANONYMOUS may have card_id null
- all other card-backed modes require card_id
- content_digest and rights_statement_ref must be sha256 refs
- authority always none
- independence defaults must never silently become INDEPENDENT_ESTABLISHED
```

- [ ] **Step 5: Run GREEN**

```bash
python -m unittest tests.test_commons -v
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add alex_runtime/commons.py tests/test_commons.py
git commit -m "feat: preserve commons rights and deposit boundaries"
```

---

### Task 4: Add Ed25519 pseudonymous continuity

**Files:**
- Create: `requirements.txt` only if no dependency manifest exists at execution time.
- Modify: `alex_runtime/commons.py`
- Modify: `tests/test_commons.py`

**Interfaces:**
- Produces:
  - `verify_pseudonym_continuity(proof: object) -> dict[str, Any]`
- Proof schema: `alex.pseudonym-continuity/v0`.

- [ ] **Step 1: Add the dependency explicitly**

If no dependency file exists, create `requirements.txt` containing:

```text
cryptography
```

Do not add a second crypto package and do not implement signing primitives manually.

- [ ] **Step 2: Write failing continuity tests**

Append:

```python
import base64
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from alex_runtime.commons import verify_pseudonym_continuity

class PseudonymContinuityTests(unittest.TestCase):
    def test_valid_signature_establishes_key_continuity_not_civil_identity(self):
        private_key = Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        public_bytes = public_key.public_bytes_raw()
        message = b"alex-continuity:card:pseudo:001:deposit-002"
        signature = private_key.sign(message)
        proof = {
            "schema": "alex.pseudonym-continuity/v0",
            "card_id": "card:pseudo:001",
            "public_key_b64": base64.b64encode(public_bytes).decode("ascii"),
            "message": message.decode("ascii"),
            "signature_b64": base64.b64encode(signature).decode("ascii"),
        }
        result = verify_pseudonym_continuity(proof)
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["continuity_status"], "VERIFIED_KEY_CONTINUITY")
        self.assertEqual(result["receipt"]["civil_identity_status"], "UNKNOWN")
        self.assertEqual(result["receipt"]["authority"], "none")

    def test_bad_signature_refuses(self):
        private_key = Ed25519PrivateKey.generate()
        other_key = Ed25519PrivateKey.generate()
        public_bytes = private_key.public_key().public_bytes_raw()
        message = b"alex-continuity:card:pseudo:001:deposit-002"
        proof = {
            "schema": "alex.pseudonym-continuity/v0",
            "card_id": "card:pseudo:001",
            "public_key_b64": base64.b64encode(public_bytes).decode("ascii"),
            "message": message.decode("ascii"),
            "signature_b64": base64.b64encode(other_key.sign(message)).decode("ascii"),
        }
        result = verify_pseudonym_continuity(proof)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "signature_verification_failed")
```

If the installed `cryptography` version does not expose `public_bytes_raw()`, use:

```python
from cryptography.hazmat.primitives import serialization
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw,
)
```

and use the same production encoding.

- [ ] **Step 3: Run RED**

```bash
python -m unittest tests.test_commons.PseudonymContinuityTests -v
```

Expected: missing-function failure.

- [ ] **Step 4: Implement verification**

Use only:

```python
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
```

Algorithm:

```text
1. validate schema/card/message/base64 fields
2. decode 32-byte Ed25519 public key and signature
3. Ed25519PublicKey.from_public_bytes(public_key).verify(signature, message_bytes)
4. on InvalidSignature => REFUSE signature_verification_failed
5. on success => receipt:
   continuity_status = VERIFIED_KEY_CONTINUITY
   civil_identity_status = UNKNOWN
   key_fingerprint = sha256 of public key bytes
   authority = none
```

Do not infer that two different keys are independent people.

- [ ] **Step 5: Run GREEN**

```bash
python -m unittest tests.test_commons.PseudonymContinuityTests -v
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add alex_runtime/commons.py tests/test_commons.py requirements.txt
git commit -m "feat: verify pseudonymous key continuity"
```

If a dependency manifest already existed, add only that manifest instead of `requirements.txt`.

---

### Task 5: Add local intake runner with no networking

**Files:**
- Create: `tools/run_commons_intake.py`
- Modify: `tests/test_commons.py`

**Interfaces:**
- CLI:
  - `python tools/run_commons_intake.py deposit.json`
  - reads one JSON object
  - calls `evaluate_commons_deposit`
  - writes one JSON result
  - exit `0` on ACCEPT, `1` on REFUSE, `2` on malformed invocation.

- [ ] **Step 1: Write CLI behavior test**

Add a subprocess test that writes `BASE_DEPOSIT` to a temporary JSON file, invokes the runner, parses stdout, and asserts:

```python
self.assertEqual(payload["disposition"], "ACCEPT")
self.assertEqual(payload["receipt"]["authority"], "none")
```

Add a source scan assertion:

```python
runner = Path("tools/run_commons_intake.py").read_text(encoding="utf-8")
for forbidden in ["socket.", "http.server", "Flask", "FastAPI", "uvicorn", "listen("]:
    self.assertNotIn(forbidden, runner)
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_commons -v
```

Expected: missing runner failure.

- [ ] **Step 3: Implement the runner**

The file should:

```python
from pathlib import Path
import json
import sys

from alex_runtime.commons import evaluate_commons_deposit

def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(json.dumps({"disposition": "REFUSE", "reason": "usage"}))
        return 2
    try:
        record = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print(json.dumps({"disposition": "REFUSE", "reason": "invalid_input"}))
        return 2
    result = evaluate_commons_deposit(record)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["disposition"] == "ACCEPT" else 1

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

No network imports.

- [ ] **Step 4: Run GREEN**

```bash
python -m unittest tests.test_commons -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/run_commons_intake.py tests/test_commons.py
git commit -m "feat: add local commons intake runner"
```

---

### Task 6: Add Commons hostile Crucible specimens

**Files:**
- Create:
  - `crucible/specimens/commons-pseudonym-multiplicity.json`
  - `crucible/specimens/commons-tor-trust-laundering.json`
  - `crucible/specimens/commons-deposit-is-not-admission.json`
  - `crucible/specimens/commons-deposit-is-not-publication.json`
  - `crucible/specimens/commons-verified-identity-is-not-verified-claim.json`
- Modify: `crucible/README.md`

**Interfaces:**
- Consumes: existing specimen schema.
- Produces: five schema-valid refusal fixtures.

- [ ] **Step 1: Create pseudonym-multiplicity fixture**

Attempt:

```text
five pseudonymous cards support claim C
-> therefore five independent witnesses support C
```

Expected: `REFUSE`; required survivor: `independence_unknown`.

- [ ] **Step 2: Create Tor trust-laundering fixture**

Attempt:

```text
deposit arrived through ONION_SERVICE
-> therefore contributor is a whistleblower / source is more authentic / claim deserves more trust
```

Expected: `REFUSE`; required survivor: `transport_class_only`.

- [ ] **Step 3: Create admission/publication/identity fixtures**

Attempts:

```text
deposit accepted -> claim admitted
deposit accepted -> artifact publishable
verified identity -> attached claim verified
```

All expected: `REFUSE`.

- [ ] **Step 4: Validate fixtures**

```bash
python tools/crucible.py
```

Expected: specimen validation succeeds.

- [ ] **Step 5: Update README**

Add the family law:

```text
Commons preserves contribution occurrence and continuity without converting identity, transport, or deposit count into evidence authority.
```

- [ ] **Step 6: Commit**

```bash
git add crucible/specimens/commons-*.json crucible/README.md
git commit -m "test: add commons constitutional specimens"
```

---

### Task 7: Whole-slice verification and Tor gate proof

**Files:**
- No new transport/network files.

**Interfaces:**
- Produces: verified local Commons contract and explicit proof that Tor has not been prematurely implemented.

- [ ] **Step 1: Run Commons tests**

```bash
python -m unittest tests.test_commons -v
```

Expected: PASS.

- [ ] **Step 2: Run full ALEX tests**

```bash
python -m unittest discover -s tests -v
```

Expected: all ordinary tests PASS; pre-existing environment-dependent Chronobody tests may SKIP for their declared materialization requirement.

- [ ] **Step 3: Run Crucible validation**

```bash
python tools/crucible.py
```

Expected: PASS/schema-valid suite.

- [ ] **Step 4: Prove there is no production Tor/server implementation**

Run:

```bash
git grep -n -E 'HiddenService|onion_service|stem\.control|http\.server|uvicorn|FastAPI|Flask' -- alex_runtime tools || true
```

Expected: no production endpoint implementation. Mentions in documentation/tests are acceptable and must be inspected manually if returned.

- [ ] **Step 5: Run whitespace/status checks**

```bash
git diff --check
git status --short
```

Expected: no whitespace errors; only intended Commons changes.

- [ ] **Step 6: Final scoped fix commit only if needed**

If verification required fixes:

```bash
git add <exact-fixed-files>
git commit -m "fix: harden commons intake boundary"
```

Do not create an empty commit.

## Completion receipt

The slice is complete when all of these are demonstrable:

```text
ONE_SHOT_ANONYMOUS deposits can be represented without fake identity
PERSISTENT_PSEUDONYM continuity can be cryptographically verified without civil identity
different pseudonym keys are not assumed to be independent people
ONION_SERVICE is representable as transport metadata but grants no trust
rights permissions remain independent fields
deposit acceptance grants neither claim admission nor publication
all untrusted deposits begin INERT
all receipts freeze authority at none
no network listener or Tor deployment exists in the first slice
```

## Deferred Gate: Onion Service adapter

Do not implement in this plan.

The next plan may begin only after this slice is green and must include:

```text
- threat model
- log-retention inventory
- upload/abuse limits
- isolated file processing
- onion-service key storage/rotation/backup policy
- explicit non-guarantee language around anonymity
- semantic equivalence test: LOCAL deposit and ONION_SERVICE deposit differ only in declared transport metadata
```
