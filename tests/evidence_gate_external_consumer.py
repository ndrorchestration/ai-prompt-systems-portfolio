import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deps", "dgaf"))

from components.evidence_gate import EvidenceAdmissionReason, admit_evidence
from components.evidence_gate_adapters import LocalTestArtifact, local_test_artifact_to_gate_inputs


def mapped_inputs():
    return local_test_artifact_to_gate_inputs(
        LocalTestArtifact(
            artifact_id="prompt-portfolio-portability-probe",
            test_name="prompt_portfolio_external_evidence_probe",
            source_revision="consumer-revision-placeholder",
            runtime_identity="python-3.12",
            environment_identity="github-actions-ubuntu-latest",
            output_bytes=b'{"status":"passed","scope":"external-consumer"}\n',
        )
    )


def main():
    mapped = mapped_inputs()

    admitted = admit_evidence(
        mapped.evidence,
        mapped.target,
        mapped.provenance,
        mapped.claim_scope,
        evidence_bytes=mapped.evidence_bytes,
        expected_target=mapped.target,
        required_producer_class="LOCAL_TEST",
    )
    assert admitted.admitted is True
    assert admitted.reason_code is EvidenceAdmissionReason.ADMITTED
    assert admitted.authorization_effect == "NONE"

    tampered = admit_evidence(
        mapped.evidence,
        mapped.target,
        mapped.provenance,
        mapped.claim_scope,
        evidence_bytes=b'{"status":"tampered"}\n',
        expected_target=mapped.target,
        required_producer_class="LOCAL_TEST",
    )
    assert tampered.admitted is False
    assert tampered.reason_code is EvidenceAdmissionReason.DIGEST_MISMATCH
    assert tampered.authorization_effect == "NONE"

    print("EVIDENCE_GATE_EXTERNAL_CONSUMER=PASS")


if __name__ == "__main__":
    main()
