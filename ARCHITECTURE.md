# ai-prompt-systems-portfolio — Architecture

**Governed by:** [DGAF-Framework](https://github.com/Flickerflash/DGAF-Framework)
**Evidence steward:** Agent Apogee
**Last updated:** 2026-04-29 (BLG-08 rename — raw prompts moved to `prompts/`)

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

| Module | Pattern Type | DGAF Alignment |
|--------|-------------|---------------|
| 01 State Anchor | Continuity | COLLEEN / P-02 COLLEEN-Trigger-Chain |
| 02 Constraint Gate | Guardrail | Sentinel / NDR-01 |
| 03 Multi-Agent Flow | Orchestration | Amethyst-Conductor / P-01 Roster-Sync |
| 04 Parametric Constraint | Adaptive Control | Apogee / P-04 NOTICE-Authority-Chain |
| 05 Error Recovery | Resilience | Reciprocity / P-05 False-Positive-Close |

---

## DGAF Governance Notice

This repository is a **prompt pattern library** within the DGAF (Dynamic Governance Agentic
Formation Framework) ecosystem. All patterns are validated against:

- NIST AI RMF Govern 1.1, Map 1.5
- DGAF AXIS constraints (NDR-01 / IONIAN mode)
- Agent Apogee evidence traceability requirements

Pattern updates must pass the Constraint Gate (Module 02) before merge.

---

## Relationship to Ecosystem

```
DGAF-Framework (spine)
  └── prompt-optimization-library      ← Prompt versioning + lineage (v0→v1→v2)
  └── ai-prompt-systems-portfolio      ← THIS REPO — structural patterns
  └── ai-prompt-engineering-portfolio  ← Applied portfolio examples
```

See [CROSS_REF.md](https://github.com/Flickerflash/DGAF-Framework/blob/main/CROSS_REF.md)
for the full 13-repo ecosystem map.
