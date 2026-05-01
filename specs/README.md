# specs/ — Machine-Readable Evaluation Specifications

> **Governance:** Agent Amethyst / DGAF ecosystem  
> See: https://github.com/ndrorchestration/DGAF-Framework

This directory contains YAML evaluation specs for each prompt artifact in this portfolio.
Each spec defines metrics, scoring rules, and pass/fail logic for programmatic assessment.

## Usage

```bash
python -m portfolio.eval specs/example.yaml --input "<prompt>" --output "<model response>"
```

## Spec Index

| File | Prompt | Pattern Class |
|------|--------|---------------|
| `example.yaml` | Template / reference spec | All |
| `01_state_anchor_eval.yaml` | State Anchor Prompt | State Management |
| `02_constraint_gate_eval.yaml` | Constraint Gate | Safety & Compliance |
| `03_multi_agent_eval.yaml` | Multi-Agent Orchestration | Orchestration |
| `04_parametric_eval.yaml` | Parametric Dial Constraint | Parameterization |
| `05_error_recovery_eval.yaml` | Error Recovery & Robustness | Resilience |

## Spec Format

```yaml
name: "<Eval Name>"
version: "1.0.0"
governance: "DGAF / Agent Amethyst"
pattern_class: "<class>"
ndp_pattern: "<NDR Pattern name>"
metrics:
  - name: "<metric_name>"
    type: "boolean | score"
    description: "<what this measures>"
    weight: <0.0-1.0>
rules:
  - if: "<metric> == <value>"
    then: "pass = false"
passing_threshold: 0.75
```
