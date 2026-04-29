<!--
  Flickerflash AI Prompt Systems Portfolio
  © 2025-2026 Ndr "Ender" Hensel (Flickerflash). Apache License 2.0.
  Governance: Agent Amethyst / DGAF ecosystem
  See: https://github.com/Flickerflash/DGAF-Framework
  Pattern Class: Parameterization · NDR Pattern: Dial Constraint
  Renamed: parametricexample → prompts/parametricexample.md (BLG-08, 2026-04-29)
-->

# 04 – Parametric ("Dial") Constraint Example

## Goal

Show that behavior can be tuned along a simple "dial" (e.g., strictness), **without** exposing any proprietary math or modal systems.

## Concept

I use a parameter like `STRICTNESS_LEVEL` with three allowed values:

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
- I compare outputs on:
  - Risk level  
  - Specificity  
  - Creativity  
  - Clarity

## Evaluation Notes

- If changes between levels are too small, I strengthen the descriptions.  
- If high strictness still allows risky suggestions, I tighten the level‑3 wording.  
- This pattern shows I can **parameterize behavior** without exposing deeper frameworks.
