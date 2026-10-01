"""Cross-repository conformance probe for Governed Repo v0.

This file does not vendor the Governed Repo core. The workflow downloads the
candidate module from a pinned DGAF commit and passes its local path here.
Success demonstrates only bounded API/conformance portability for this
consumer repository.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("governed_repo_upstream", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import upstream module at {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def make_identity(gr):
    return gr.ChangeIdentity(
        repository="ndrorchestration/ai-prompt-systems-portfolio",
        change_id="portability-probe",
        base_sha="portfolio-base",
        head_sha="portfolio-head",
        observed_base_sha="portfolio-base",
        observed_head_sha="portfolio-head",
        observed_at="2026-10-01T16:00:00Z",
    )


def make_policy(gr):
    return gr.PromotionPolicy(
        required_gates=(
            gr.GateRequirement(
                gate_id="portfolio-integrity",
                gate_class="quality",
                require_head_binding=True,
                require_base_binding=True,
            ),
        )
    )


def success_gate(gr):
    return gr.GateReceipt(
        gate_id="portfolio-integrity",
        status="completed",
        conclusion="success",
        observed_at="2026-10-01T16:01:00Z",
        head_sha="portfolio-head",
        base_sha="portfolio-base",
    )


def assert_non_effects(receipt):
    assert receipt.merge_executed is False
    assert receipt.mutation_executed is False
    assert receipt.authorization_effect == "NONE"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: governed_repo_portability_probe.py <upstream-module>")

    gr = load_module(Path(sys.argv[1]))

    eligible = gr.assess_promotion(
        make_identity(gr),
        make_policy(gr),
        [success_gate(gr)],
    )
    assert eligible.eligible is True
    assert eligible.reason_code is gr.PromotionReason.ELIGIBLE_FOR_PROMOTION
    assert_non_effects(eligible)

    stale = gr.assess_promotion(
        gr.ChangeIdentity(
            repository="ndrorchestration/ai-prompt-systems-portfolio",
            change_id="portability-probe",
            base_sha="portfolio-base",
            head_sha="portfolio-head",
            observed_base_sha="newer-base",
            observed_head_sha="portfolio-head",
            observed_at="2026-10-01T16:02:00Z",
        ),
        make_policy(gr),
        [success_gate(gr)],
    )
    assert stale.eligible is False
    assert stale.reason_code is gr.PromotionReason.STALE_BASE
    assert_non_effects(stale)

    missing = gr.assess_promotion(
        make_identity(gr),
        make_policy(gr),
        [],
    )
    assert missing.eligible is False
    assert missing.reason_code is gr.PromotionReason.REQUIRED_CHECK_MISSING
    assert missing.missing_gate_ids == ("portfolio-integrity",)
    assert_non_effects(missing)

    failed = gr.assess_promotion(
        make_identity(gr),
        make_policy(gr),
        [
            gr.GateReceipt(
                gate_id="portfolio-integrity",
                status="completed",
                conclusion="failure",
                observed_at="2026-10-01T16:03:00Z",
                head_sha="portfolio-head",
                base_sha="portfolio-base",
            )
        ],
    )
    assert failed.eligible is False
    assert failed.reason_code is gr.PromotionReason.REQUIRED_CHECK_FAILED
    assert_non_effects(failed)

    print("Governed Repo v0 portability probe: PASS")
    print("consumer=ndrorchestration/ai-prompt-systems-portfolio")
    print("cases=eligible,stale-base,missing-check,failed-check")
    print("authority_transfer=false")
    print("validation_transfer=false")


if __name__ == "__main__":
    main()
