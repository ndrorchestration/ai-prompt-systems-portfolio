#!/usr/bin/env python3
"""Bounded cross-repository Assurance Profiles v0 portability probe."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


def load_upstream(path: Path):
    spec = importlib.util.spec_from_file_location("assurance_profiles_upstream", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load Assurance Profiles upstream module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-core", required=True)
    parser.add_argument("--mapping", required=True)
    parser.add_argument("--consumer-sha", required=True)
    parser.add_argument("--upstream-sha", required=True)
    args = parser.parse_args()

    if len(args.consumer_sha) != 40:
        raise ValueError("consumer SHA must be exact 40-hex identity")
    if len(args.upstream_sha) != 40:
        raise ValueError("upstream SHA must be exact 40-hex identity")

    ap = load_upstream(Path(args.upstream_core))
    mapping_path = Path(args.mapping)
    raw = mapping_path.read_bytes()
    mapping = json.loads(raw)
    canonical = json.dumps(mapping, sort_keys=True, separators=(",", ":")).encode("utf-8")

    assert mapping["authorization_effect"] == "NONE"
    assert mapping["evidence_transfer"] is False

    raw_digest = sha256_bytes(raw)
    canonical_digest = sha256_bytes(canonical)

    source = ap.SourceBinding(
        repository="ndrorchestration/ai-prompt-systems-portfolio",
        revision=args.consumer_sha,
        source_schema="common_evaluation_object_model_v0",
        runtime_identity=f"python-{sys.version_info.major}.{sys.version_info.minor}",
        environment_identity="github-actions",
    )

    measurement = ap.MeasurementContract(
        source=source,
        fields=(
            ap.MeasurementField(
                name="mapped_project",
                derivation=ap.DerivationClass.DIRECT,
                value=mapping["project"],
                source_field="project",
                unit="identifier",
                freshness_state="CURRENT_AT_SOURCE_REVISION",
            ),
            ap.MeasurementField(
                name="mapping_sha256",
                derivation=ap.DerivationClass.DERIVED,
                value=raw_digest,
                unit="sha256",
                freshness_state="CURRENT_AT_SOURCE_REVISION",
            ),
            ap.MeasurementField(
                name="production_authorization",
                derivation=ap.DerivationClass.UNMEASURED,
                freshness_state="NOT_ESTABLISHED",
            ),
        ),
        non_inference_rules=(
            "evaluation mapping does not transfer validation",
            "evaluation mapping does not grant production authorization",
        ),
    )

    profile = ap.AssuranceProfile(
        profile_id="portfolio.common-evaluation-model.assurance.v0",
        measurement=measurement,
        replay=ap.ReplayContract(
            required_digest_roles=("raw_sha256", "canonical_json_sha256"),
            required_verification_fields=("source_identity_match", "canonical_digest_match"),
        ),
        readiness=(
            ap.ReadinessPredicate(
                "mapping_integrity",
                ap.PredicateStatus.PASS,
                (f"sha256:{raw_digest}",),
            ),
            ap.ReadinessPredicate(
                "production_authorization",
                ap.PredicateStatus.NOT_ESTABLISHED,
            ),
        ),
    )

    replay_ok = ap.evaluate_replay(
        profile.replay,
        ap.ReplayReceipt(
            source=source,
            digests={
                "raw_sha256": raw_digest,
                "canonical_json_sha256": canonical_digest,
            },
            verifications={
                "source_identity_match": True,
                "canonical_digest_match": True,
            },
            replay_environment={"runner": "github-actions"},
        ),
    )
    assert replay_ok.status == "PASS"

    replay_blocked = ap.evaluate_replay(
        profile.replay,
        ap.ReplayReceipt(
            source=source,
            digests={"raw_sha256": raw_digest},
            verifications={
                "source_identity_match": True,
                "canonical_digest_match": False,
            },
            replay_environment={"runner": "github-actions"},
        ),
    )
    assert replay_blocked.status == "BLOCKED"
    assert "MISSING_DIGEST:canonical_json_sha256" in replay_blocked.reasons
    assert "VERIFICATION_NOT_TRUE:canonical_digest_match" in replay_blocked.reasons

    readiness = ap.evaluate_readiness(profile.readiness)
    assert readiness.status == "BLOCKED"
    assert readiness.reasons == (
        "READINESS_NOT_ESTABLISHED:production_authorization",
    )

    review = ap.evaluate_external_review(
        ap.ExternalReviewReceipt(
            disclosure=ap.ExternalReviewDisclosure(
                reviewer_identity="bounded-portability-probe",
                relationship_disclosure=(
                    "same-owner automated consumer; not independent external validation"
                ),
                independence_finding=ap.ReviewFinding.VERIFIED,
                limitations=(
                    "same owner",
                    "automated conformance only",
                ),
            ),
            source=source,
            finding=ap.ReviewFinding.VERIFIED,
            retained_evidence_refs=(f"sha256:{raw_digest}",),
        )
    )
    assert review.status == "PASS"

    for decision in (replay_ok, replay_blocked, readiness, review):
        assert decision.authorization_effect == "NONE"
        assert decision.execution_effect == "NONE"
        assert decision.scientific_n_increment == 0
        assert decision.efficacy_effect == "NONE"

    assert profile.measurement.fields[0].derivation is ap.DerivationClass.DIRECT
    assert profile.measurement.fields[1].derivation is ap.DerivationClass.DERIVED
    assert profile.measurement.fields[2].derivation is ap.DerivationClass.UNMEASURED
    assert profile.measurement.fields[2].value is None

    result = {
        "status": "PASS",
        "upstream_assurance_profiles_sha": args.upstream_sha,
        "consumer_sha": args.consumer_sha,
        "consumer_domain": "prompt-and-evaluation-spec-portfolio",
        "measurement_states": ["DIRECT", "DERIVED", "UNMEASURED"],
        "replay_pass": replay_ok.to_dict(),
        "replay_fail_closed": replay_blocked.to_dict(),
        "readiness_blocked": readiness.to_dict(),
        "external_review_non_authorizing": review.to_dict(),
        "authority_transfer": False,
        "validation_transfer": False,
        "independent_validation": False,
        "portability_claim": "bounded cross-repository API/conformance only",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
