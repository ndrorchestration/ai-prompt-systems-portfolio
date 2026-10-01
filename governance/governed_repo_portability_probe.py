"""Cross-repository installed-package conformance probe for Governed Repo v0.

The workflow builds a wheel from an exact pinned DGAF P0 candidate, installs
that wheel, changes outside both repository source trees, and then runs this
probe through the public governed_repo import.
"""

from __future__ import annotations

import governed_repo as gr


def make_identity(**overrides):
    values = {
        "repository": "ndrorchestration/ai-prompt-systems-portfolio",
        "change_id": "portability-probe",
        "base_sha": "portfolio-base",
        "head_sha": "portfolio-head",
        "observed_base_sha": "portfolio-base",
        "observed_head_sha": "portfolio-head",
        "observed_at": "2026-10-01T16:00:00Z",
    }
    values.update(overrides)
    return gr.ChangeIdentity(**values)


def make_policy():
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


def success_gate(**overrides):
    values = {
        "gate_id": "portfolio-integrity",
        "status": "completed",
        "conclusion": "success",
        "observed_at": "2026-10-01T16:01:00Z",
        "head_sha": "portfolio-head",
        "base_sha": "portfolio-base",
    }
    values.update(overrides)
    return gr.GateReceipt(**values)


def assert_non_effects(receipt):
    assert receipt.merge_executed is False
    assert receipt.mutation_executed is False
    assert receipt.authorization_effect == "NONE"


def main() -> None:
    eligible = gr.assess_promotion(make_identity(), make_policy(), [success_gate()])
    assert eligible.eligible is True
    assert eligible.reason_code is gr.PromotionReason.ELIGIBLE_FOR_PROMOTION
    assert_non_effects(eligible)

    stale = gr.assess_promotion(
        make_identity(observed_base_sha="newer-base"),
        make_policy(),
        [success_gate()],
    )
    assert stale.eligible is False
    assert stale.reason_code is gr.PromotionReason.STALE_BASE
    assert_non_effects(stale)

    missing = gr.assess_promotion(make_identity(), make_policy(), [])
    assert missing.eligible is False
    assert missing.reason_code is gr.PromotionReason.REQUIRED_CHECK_MISSING
    assert missing.missing_gate_ids == ("portfolio-integrity",)
    assert_non_effects(missing)

    failed = gr.assess_promotion(
        make_identity(),
        make_policy(),
        [success_gate(conclusion="failure")],
    )
    assert failed.eligible is False
    assert failed.reason_code is gr.PromotionReason.REQUIRED_CHECK_FAILED
    assert_non_effects(failed)

    print("Governed Repo v0 installed-package portability probe: PASS")
    print("consumer=ndrorchestration/ai-prompt-systems-portfolio")
    print("package_transport=wheel")
    print("package_version=0.0.0.dev0")
    print("cases=eligible,stale-base,missing-check,failed-check")
    print("authority_transfer=false")
    print("validation_transfer=false")


if __name__ == "__main__":
    main()
