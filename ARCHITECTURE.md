# ai-prompt-systems-portfolio — Architecture

**Governed by:** [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework)
**Governance compatibility role:** `role.governance-orchestrator` — alignment only; no DGAF authority transfer
**Evidence stewardship alignment:** `role.evidence-verification-reviewer` — alignment only; no DGAF authority transfer
**Last updated:** 2026-09-12 (persona-to-role compatibility migration)

---

## Purpose

A modular library of prompt engineering patterns for multi-agent and governed AI systems.
Each module has a numbered spec (`.md`) and a raw prompt artifact in `prompts/`.

---

## Module Map

```
ai-prompt-systems-portfolio/
├── 01_state_anchor.md              ← Spec: State persistence across agent turns
├── 02_constraint_gate.md           ← Spec: Hard constraint enforcement at inference
├── 03_multi_agent_flow.md          ← Spec: Orchestration handoff patterns
├── 04_parametric_constraint.md     ← Spec: Dynamic constraint injection
├── 05_error_recovery.md            ← Spec: Graceful failure + retry logic
├── prompts/
│   ├── stateanchorprompt.md          ← Raw prompt artifact for 01
│   ├── constraintgateguardrail.md    ← Raw prompt artifact for 02
│   ├── multi-agent-orchestration-pattern.md  ← Raw prompt artifact for 03
│   ├── parametricexample.md          ← Raw prompt artifact for 04
│   └── recoveryrobustness.md         ← Raw prompt artifact for 05
├── specs/                          ← Formal JSON/YAML specs per pattern
├── ARCHITECTURE.md                 ← This file
├── NOTICE                          ← Apache 2.0 + DGAF attribution
└── LICENSE
```

---

## Pattern Taxonomy

The DGAF references below are behavior-derived compatibility alignments, not transferred DGAF authority. Historical names are retained separately in provenance where required.

| Module | Pattern Type | Functional alignment |
|--------|-------------|----------------------|
| 01 State Anchor | Continuity | `cap.continuity.coordinate` — conversational continuity only |
| 02 Constraint Gate | Guardrail | `role.constraint-qa-auditor` / NDR-01 — constraint verification; not security-containment authority |
| 03 Multi-Agent Flow | Orchestration | `role.governance-orchestrator` / P-01 Roster-Sync — orchestration analogue only |
| 04 Parametric Constraint | Adaptive Control | **UNRESOLVED / NO CANONICAL ROLE** — parameterized prompt behavior only |
| 05 Error Recovery | Resilience | **UNRESOLVED / NO CANONICAL ROLE** — conversational self-correction only |

The repository-local compatibility record is `governance/persona_role_compatibility.v1.json`, bound to DGAF registry commit `8bc9f518ba1d8d939cd75d3f5b97d65289c5a0d8`.

---

## DGAF Governance Notice

This repository is a **prompt pattern library** within the DGAF (Dynamic Governance Agentic
Formation Framework) ecosystem. The portfolio documents mappings or compatibility relationships to:

- NIST AI RMF Govern 1.1, Map 1.5
- DGAF AXIS constraints (NDR-01 / IONIAN mode)
- `role.evidence-verification-reviewer` evidence-integrity semantics

These references do not establish external certification, DGAF authorization, or independent validation. Pattern updates remain subject to repository review and the Constraint Gate (Module 02) where that review process is applied.

---

## Relationship to Ecosystem

```
DGAF-Framework (spine)
  └── prompt-optimization-library      ← Prompt versioning + lineage (v0→v1→v2)
  └── ai-prompt-systems-portfolio      ← THIS REPO — structural patterns
  └── ai-prompt-engineering-portfolio  ← Applied portfolio examples
```

See [CROSS_REF.md](https://github.com/ndrorchestration/DGAF-Framework/blob/main/CROSS_REF.md)
for the ecosystem map.
