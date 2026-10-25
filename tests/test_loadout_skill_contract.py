from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "loadout" / "SKILL.md"
FIELD_GUIDE = ROOT / "skills" / "loadout" / "references" / "plugin-layer-map.md"
EVAL_GUIDE = ROOT / "skills" / "loadout" / "references" / "operator-evals.md"
OPENAI = ROOT / "skills" / "loadout" / "agents" / "openai.yaml"
DEV = ROOT / "evals" / "loadout-discovery-cases.json"
HOLDOUT = ROOT / "evals" / "loadout-holdout-cases.json"

ALLOWED_LAYERS = {
    "reasoning",
    "process",
    "research",
    "workspace",
    "runtime",
    "expression",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("missing YAML frontmatter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


class LoadoutSkillContractTests(unittest.TestCase):
    def test_skill_is_trigger_first_compact_and_routes_to_references(self) -> None:
        text = read(SKILL)
        meta = frontmatter(text)
        description = meta["description"]
        self.assertTrue(description.startswith("Use when "))
        self.assertLessEqual(len(description), 500)

        body = text.split("---\n", 2)[-1]
        self.assertLessEqual(len(body.split()), 500)
        self.assertIn("references/plugin-layer-map.md", text)
        self.assertIn("references/operator-evals.md", text)
        self.assertIn("Bring the smallest world that can do the job.", text)

        for law in (
            "task != tool list",
            "capability availability != authority",
            "discovery != invocation",
            "missing capability != missing task",
        ):
            self.assertIn(law, text)

    def test_skill_keeps_avalanche_as_candidates_not_bindings(self) -> None:
        text = read(SKILL)
        self.assertIn("Candidate lists are candidates", text)
        self.assertIn("LOADOUT may select none", text)
        self.assertIn("Explicit task requirements win", text)
        self.assertIn("leave everything else asleep", text)

    def test_openai_interface_is_short_and_does_not_teach_the_whole_catalog(self) -> None:
        text = read(OPENAI)
        self.assertIn("$loadout", text)
        self.assertIn("smallest sufficient", text)
        self.assertLessEqual(len(text), 700)
        for avalanche_name in ("PostHog", "Twilio", "Supabase", "Canva", "Figma"):
            self.assertNotIn(avalanche_name, text)

    def test_reference_map_has_six_functional_layers_and_runtime_discovery_rule(self) -> None:
        text = read(FIELD_GUIDE)
        for heading in (
            "Reasoning organs",
            "Process disciplines",
            "Research and computation",
            "Workspaces and source systems",
            "Build, runtime, and observability",
            "Output, design, communication, and expression",
        ):
            self.assertIn(heading, text)
        self.assertIn("discover availability", text.lower())
        self.assertIn("do not assume", text.lower())

    def test_eval_guide_preserves_claim_boundary(self) -> None:
        text = read(EVAL_GUIDE)
        self.assertIn("repository checks", text.lower())
        self.assertIn("do not prove", text.lower())
        self.assertIn("automatic invocation", text.lower())
        self.assertIn("authority", text.lower())

    def test_eval_catalogs_are_valid_and_holdouts_are_disjoint(self) -> None:
        dev = json.loads(read(DEV))
        holdout = json.loads(read(HOLDOUT))
        self.assertEqual(dev["schema"], "loadout.operator-eval/v0")
        self.assertEqual(holdout["schema"], "loadout.operator-eval/v0")
        self.assertEqual(dev["set"], "development")
        self.assertEqual(holdout["set"], "holdout")

        dev_prompts = {case["prompt"] for case in dev["cases"]}
        holdout_prompts = {case["prompt"] for case in holdout["cases"]}
        self.assertTrue(dev_prompts.isdisjoint(holdout_prompts))

        ids: set[str] = set()
        for catalog in (dev, holdout):
            for case in catalog["cases"]:
                self.assertNotIn(case["id"], ids)
                ids.add(case["id"])
                self.assertIsInstance(case["expected_bindings"], list)
                self.assertTrue(case["must"])
                self.assertTrue(case["must_not"])
                for binding in case["expected_bindings"]:
                    self.assertIn(binding["layer"], ALLOWED_LAYERS)
                    self.assertTrue(binding["name"])

    def test_holdout_prompts_are_not_copied_into_skill(self) -> None:
        skill = read(SKILL)
        holdout = json.loads(read(HOLDOUT))
        for case in holdout["cases"]:
            self.assertNotIn(case["prompt"], skill)


if __name__ == "__main__":
    unittest.main()
