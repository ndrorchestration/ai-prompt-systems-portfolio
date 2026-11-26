# AI Prompt Systems Portfolio

**Public, IP-safe examples of prompt-system design, evaluation rubrics, multi-agent workflow patterns, and failure-aware instruction engineering.**

> **Status:** Active work-in-progress. This repository demonstrates design artifacts and local evaluation specifications. A prompt spec or rubric is not evidence of general model performance, external certification, or validation of another repository.

## Start here

For a fast review, these three artifacts show the clearest range of the work:

1. **[State Anchor](01_state_anchor.md)** — maintaining role/scope consistency across a long interaction, with explicit failure conditions.
2. **[Multi-Agent Flow](03_multi_agent_flow.md)** — a structured Researcher → Critic → Editor pattern with role boundaries and evaluation notes.
3. **[Error Recovery](05_error_recovery.md)** — fail-safe handling for missing data, tool failure, and ambiguous instructions without fabricating certainty.

Each has a corresponding machine-readable evaluation specification under [`specs/`](specs/).

## What this repository demonstrates

- system/instruction prompt structure;
- explicit constraint gates;
- state anchoring and scope control;
- multi-agent role decomposition;
- tunable/parametric behavior;
- failure and recovery handling;
- artifact-local evaluation rubrics;
- public Needle template specifications;
- evidence-conscious documentation of what has and has not been tested.

## Core artifact set

| Artifact | Primary skill | Evaluation spec |
|---|---|---|
| [State Anchor](01_state_anchor.md) | State/scope consistency | [`specs/01_state_anchor_eval.yaml`](specs/01_state_anchor_eval.yaml) |
| [Constraint Gate](02_constraint_gate.md) | Non-negotiable instruction boundaries | [`specs/02_constraint_gate_eval.yaml`](specs/02_constraint_gate_eval.yaml) |
| [Multi-Agent Flow](03_multi_agent_flow.md) | Role decomposition/orchestration | [`specs/03_multi_agent_eval.yaml`](specs/03_multi_agent_eval.yaml) |
| [Parametric Constraint](04_parametric_constraint.md) | Controlled behavioral tuning | [`specs/04_parametric_eval.yaml`](specs/04_parametric_eval.yaml) |
| [Error Recovery](05_error_recovery.md) | Failure-aware prompting | [`specs/05_error_recovery_eval.yaml`](specs/05_error_recovery_eval.yaml) |

The YAML files are **evaluation specifications/data**, not an executable evaluator by themselves.

## Needle template specifications

[`specs/needle/`](specs/needle/) contains public specifications for Needle.app workflows, including evaluation structure, multi-agent flow, and output constraints where documented.

References to NIST/ISO controls are **mappings**, not evidence of certification, endorsement, or compliance.

Related external-framework mappings are maintained separately in `ai-governance-frameworks`; cross-repository references do not transfer validation.

## Evaluation status

This repository does not currently ship a supported Python evaluation package or CLI. Current evidence consists of:

- checked-in prompt artifacts;
- checked-in evaluation specifications;
- artifact-specific notes and failure modes;
- repository integrity checks that verify advertised public artifacts exist.

Executable benchmarking belongs in a repository that actually contains and tests an evaluation harness, such as `resumeapex-eval`, rather than being implied here.

## Evidence standard

Use the repository-wide distinction:

`DEFINED → IMPLEMENTED → COMPUTED → VERIFIED → ATTESTED → HISTORICAL → HYPOTHESIS → METAPHOR → UNSUPPORTED → DEPRECATED`

Examples:

- a written prompt pattern is **DEFINED**;
- a checked-in prompt artifact/spec is **IMPLEMENTED as an artifact**;
- a rubric result is **COMPUTED** only when an evaluator actually executes it;
- a passing repository-integrity workflow verifies only the files/relationships it checks;
- no local result should be generalized to unrelated models, datasets, tasks, or repositories without separate evidence.

## Repository map

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — organization and design relationships.
- [`specs/`](specs/) — artifact-local evaluation specifications.
- [`best-practices/`](best-practices/) — supporting prompt-engineering guidance.
- [`docs/`](docs/) — additional documentation/evidence notes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution expectations.

## Relationship to other work

- `resumeapex-eval` — separate executable evaluation/benchmark project.
- `Orbit-Driftwatch` — separate observable multi-agent systems showcase.
- [Agentic Governance Orchestrator (proposed successor name for DGAF)](https://github.com/ndrorchestration/DGAF-Framework) — separate governance/evaluation research track.
- `ai-governance-frameworks` — separate framework-mapping repository.

These relationships describe portfolio architecture; they are not mutual validation claims.

## License

Apache-2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

## Maintainer

Ndr / Ender Hensel (`ndrorchestration`).
