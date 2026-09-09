"""CRITERION-NOT-POLICY-001.

Experimental / non-canonical finite witness that one frozen statewise
performance table does not determine a policy ranking until a decision
criterion (and, where consumed, a prior) is declared.

Authority: none.
"""

from fractions import Fraction


_STATES = ("a", "b", "c", "d")
_COSTS = {
    "ADAPTIVE": (1, 3, 3, 3),
    "FIXED": (2, 2, 2, 2),
}
_HEAVY_PRIOR = (Fraction(3, 4), Fraction(1, 12), Fraction(1, 12), Fraction(1, 12))
_UNIFORM_PRIOR = (Fraction(1, 4),) * 4


def _expected(costs: tuple[int, ...], prior: tuple[Fraction, ...]) -> Fraction:
    return sum((weight * cost for weight, cost in zip(prior, costs)), Fraction(0, 1))


def _winner(left_name: str, left_value, right_name: str, right_value) -> str:
    if left_value < right_value:
        return left_name
    if right_value < left_value:
        return right_name
    return "TIE"


def evaluate_frozen_policy_table() -> dict:
    """Evaluate the frozen two-policy table under four declared readings.

    The function reports conditional comparisons only. It does not choose
    which criterion should govern any real decision.
    """

    adaptive = _COSTS["ADAPTIVE"]
    fixed = _COSTS["FIXED"]

    adaptive_worst = max(adaptive)
    fixed_worst = max(fixed)

    adaptive_heavy = _expected(adaptive, _HEAVY_PRIOR)
    fixed_heavy = _expected(fixed, _HEAVY_PRIOR)
    adaptive_uniform = _expected(adaptive, _UNIFORM_PRIOR)
    fixed_uniform = _expected(fixed, _UNIFORM_PRIOR)

    oracle = tuple(min(a, f) for a, f in zip(adaptive, fixed))
    adaptive_regret = tuple(a - o for a, o in zip(adaptive, oracle))
    fixed_regret = tuple(f - o for f, o in zip(fixed, oracle))
    adaptive_max_regret = max(adaptive_regret)
    fixed_max_regret = max(fixed_regret)

    return {
        "experiment": "CRITERION-NOT-POLICY-001",
        "authority": "none",
        "state_space": list(_STATES),
        "costs": {name: list(costs) for name, costs in _COSTS.items()},
        "worst_case": {
            "criterion": "worst_case_cost",
            "ADAPTIVE": adaptive_worst,
            "FIXED": fixed_worst,
            "ranking": _winner("ADAPTIVE", adaptive_worst, "FIXED", fixed_worst),
        },
        "expected_cost_heavy": {
            "criterion": "expected_cost",
            "prior": list(_HEAVY_PRIOR),
            "ADAPTIVE": adaptive_heavy,
            "FIXED": fixed_heavy,
            "ranking": _winner("ADAPTIVE", adaptive_heavy, "FIXED", fixed_heavy),
        },
        "expected_cost_uniform": {
            "criterion": "expected_cost",
            "prior": list(_UNIFORM_PRIOR),
            "ADAPTIVE": adaptive_uniform,
            "FIXED": fixed_uniform,
            "ranking": _winner("ADAPTIVE", adaptive_uniform, "FIXED", fixed_uniform),
        },
        "minimax_regret": {
            "criterion": "minimax_regret",
            "oracle": list(oracle),
            "ADAPTIVE_regret": list(adaptive_regret),
            "FIXED_regret": list(fixed_regret),
            "ADAPTIVE": adaptive_max_regret,
            "FIXED": fixed_max_regret,
            "ranking": _winner(
                "ADAPTIVE", adaptive_max_regret, "FIXED", fixed_max_regret
            ),
        },
        "observation": "STATEWISE_COST_TABLE_DOES_NOT_SELECT_POLICY_WITHOUT_CRITERION",
    }


def evaluate_posthoc_criterion_swap() -> dict:
    """Freeze a later analysis without letting it govern an earlier cut."""

    table = evaluate_frozen_policy_table()
    earlier = table["worst_case"]
    later = table["expected_cost_heavy"]

    return {
        "experiment": "POST-HOC-CRITERION-SWAP-001",
        "authority": "none",
        "decision_cut": "t0",
        "earlier_constitution": {
            "formed_at": "t0",
            "criterion": earlier["criterion"],
            "ranking": earlier["ranking"],
        },
        "later_analysis": {
            "formed_at": "t1",
            "criterion": later["criterion"],
            "prior": later["prior"],
            "ranking": later["ranking"],
        },
        "later_analysis_governs_earlier_decision": False,
        "status": "REFUSE_RETROACTIVE_CRITERION",
        "observation": "LATER_CRITERION_DOES_NOT_REWRITE_EARLIER_DECISION_CONSTITUTION",
    }
