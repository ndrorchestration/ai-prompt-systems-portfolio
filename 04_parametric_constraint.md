<!--
  Flickerflash AI Prompt Systems Portfolio
  © 2025-2026 Ndr "Ender" Hensel (Flickerflash). Apache License 2.0.
  Governance: Agent Amethyst / DGAF ecosystem
  See: https://github.com/Flickerflash/DGAF-Framework
  Pattern Class: Parameterization · NDR Pattern: Dial Constraint
  Canonical filename: 04_parametric_constraint.md
  Legacy alias: parametricexample (retained for back-compat)
-->

# 04 – Parametric (“Dial”) Constraint Example

## Goal

Show that behavior can be tuned along a simple “dial” (e.g., strictness), **without** exposing any proprietary math or modal systems.

## Concept

Use a parameter like `STRICTNESS_LEVEL` with three allowed values:

- 1 = Relaxed
- 2 = Balanced
- 3 = Strict

## Example Instruction

> You have a parameter called STRICTNESS_LEVEL (1, 2, or 3).
>
> - At level 1 (Relaxed): You are more flexible and creative. You may suggest unconventional options as long as they are safe.
> - At level 2 (Balanced): You balance creativity with safety and clarity. You favor practical, realistic options.
> - At level 3 (Strict): You prioritize safety, clarity, and rules over creativity. You avoid any advice that could be misused.
>
> I will tell you the STRICTNESS_LEVEL. Adjust your tone and suggestions accordingly.

## Example Test

- Same user question, run with STRICTNESS_LEVEL = 1, 2, 3.
- Compare outputs on:
  - Risk level
  - Specificity
  - Creativity
  - Clarity

## Evaluation Notes

- If changes between levels are too small, strengthen the descriptions.
- If high strictness still allows risky suggestions, tighten the level‑3 wording.
- This pattern shows the ability to **parameterize behavior** without exposing deeper frameworks.

## Related Spec

See [`specs/04_parametric_eval.yaml`](specs/04_parametric_eval.yaml) for machine-readable evaluation spec.
