<!--
  Flickerflash AI Prompt Systems Portfolio
  © 2025-2026 Ndr "Ender" Hensel (Flickerflash). Apache License 2.0.
  Governance: Agent Amethyst / DGAF ecosystem
  See: https://github.com/Flickerflash/DGAF-Framework
  Pattern Class: Resilience · NDR Pattern: Recovery Robustness
  Renamed: recoveryrobustness → prompts/recoveryrobustness.md (BLG-08, 2026-04-29)
-->

# 05 – Error Recovery & Robustness

## Goal

Show how I handle errors, bad outputs, or broken conversations.

## Recovery Pattern (Example)

> If you realize your previous answer was incorrect, incomplete, or confusing:  
> 1. Briefly acknowledge the issue ("I realize my previous answer was unclear about X").  
> 2. Summarize the user's goal again in your own words.  
> 3. Provide a corrected or clearer answer.  
> 4. Offer a simple check question ("Does this address what you needed?").

## Example Prompts

- "Review your last response. Identify anything that might be incorrect, vague, or unhelpful, then propose an improved version."  
- "Summarize the conversation so far in 3 bullet points, then ask the user if you missed anything important."

## Evaluation Rubric

- **Self‑awareness:** Did the model correctly identify its own mistake or vagueness?  
- **Clarity of correction:** Is the new answer clearly better and more direct?  
- **User alignment:** Did it re‑state the user goal accurately before correcting?  
- **Politeness:** Acknowledged the error without over‑apologizing.

## Notes

I keep a small log of "before/after" responses where this pattern improved the outcome. Over time, I refine the prompts to make self‑correction more reliable.
