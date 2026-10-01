import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_common_evaluation_model import validate_mapping

ROOT = Path(__file__).resolve().parents[1]
MAPPINGS = ROOT / "specs" / "mappings"


class CommonEvaluationModelTests(unittest.TestCase):
    def test_resumeapex_mapping(self) -> None:
        validate_mapping(MAPPINGS / "resumeapex_eval_common_model_v0.json")

    def test_driftwatch_mapping(self) -> None:
        validate_mapping(MAPPINGS / "driftwatch_common_model_v0.json")

    def test_authorization_effect_must_remain_none(self) -> None:
        source = json.loads(
            (MAPPINGS / "resumeapex_eval_common_model_v0.json").read_text(
                encoding="utf-8"
            )
        )
        source["authorization_effect"] = "GRANT"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "invalid.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_mapping(path)

    def test_claim_ceiling_is_required(self) -> None:
        source = json.loads(
            (MAPPINGS / "driftwatch_common_model_v0.json").read_text(
                encoding="utf-8"
            )
        )
        source["objects"]["ClaimCeiling"]["prohibited_promotions"] = []
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "invalid.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_mapping(path)


if __name__ == "__main__":
    unittest.main()
