from alex_runtime import DERIVATION_M0_PROFILE

MECHANICAL_PREDICATES = {
    "caused_by",
    "input_of",
    "output_of",
    "derived_from",
    "exact_transform_of",
    "targets",
    "acquired_from",
}
SEMANTIC_PREDICATES = {"SUPPORTS"}

MINTING_MECHANICAL = "MECHANICAL_WITNESSED"
MINTING_SEMANTIC = "SEMANTIC_EVALUATED"


def predicate_minting_class(predicate: str) -> str | None:
    if predicate in MECHANICAL_PREDICATES:
        return MINTING_MECHANICAL
    if predicate in SEMANTIC_PREDICATES:
        return MINTING_SEMANTIC
    return None


def semantic_predicate_allowed(profile: str, predicate: str) -> bool:
    return profile == DERIVATION_M0_PROFILE and predicate == "SUPPORTS"
