"""Validate Common Evaluation Object Model mapping documents."""

from __future__ import annotations

import json
import sys
from pathlib import Path

COMMON_OBJECTS = {
    "EvaluationCase",
    "EvaluationRun",
    "CriterionRef",
    "EvidenceArtifact",
    "Finding",
    "ClaimCeiling",
    "ReplayBinding",
    "ProvenanceBinding",
    "EvaluationDecision",
}


def validate_mapping(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))

    if data.get("common_model_version") != "v0-candidate":
        raise ValueError(f"{path}: unexpected common_model_version")
    if data.get("authorization_effect") != "NONE":
        raise ValueError(f"{path}: authorization_effect must be NONE")
    if data.get("evidence_transfer") is not False:
        raise ValueError(f"{path}: evidence_transfer must be false")

    objects = data.get("objects")
    if not isinstance(objects, dict):
        raise ValueError(f"{path}: objects must be an object")

    missing = COMMON_OBJECTS - set(objects)
    extra = set(objects) - COMMON_OBJECTS
    if missing or extra:
        raise ValueError(f"{path}: common object mismatch missing={missing} extra={extra}")

    ceiling = objects["ClaimCeiling"]
    if not ceiling.get("allowed_interpretations"):
        raise ValueError(f"{path}: ClaimCeiling.allowed_interpretations required")
    if not ceiling.get("prohibited_promotions"):
        raise ValueError(f"{path}: ClaimCeiling.prohibited_promotions required")

    if not objects["ReplayBinding"].get("local_concepts"):
        raise ValueError(f"{path}: ReplayBinding mapping required")
    if not objects["ProvenanceBinding"].get("local_concepts"):
        raise ValueError(f"{path}: ProvenanceBinding mapping required")

    decision = objects["EvaluationDecision"]
    if decision.get("authorization_effect") != "NONE":
        raise ValueError(f"{path}: EvaluationDecision.authorization_effect must be NONE")

    if not data.get("non_common_concepts"):
        raise ValueError(f"{path}: project-specific non_common_concepts required")


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: validate_common_evaluation_model.py <mapping.json>...")
    for name in sys.argv[1:]:
        validate_mapping(Path(name))
    print("COMMON_EVALUATION_OBJECT_MODEL=PASS")


if __name__ == "__main__":
    main()
