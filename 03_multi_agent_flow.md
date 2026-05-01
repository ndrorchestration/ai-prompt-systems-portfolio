<!--
  ndrorchestration AI Prompt Systems Portfolio
  © 2025-2026 Njineer (ndrorchestration). Apache License 2.0.
  Governance: Agent Amethyst / DGAF ecosystem
  See: https://github.com/ndrorchestration/DGAF-Framework
  Pattern Class: Orchestration · NDR Pattern: Multi-Agent Conductor
  Canonical filename: 03_multi_agent_flow.md
  Legacy alias: multi-agent-orchestration-pattern (retained for back-compat)
-->

# 03 – Multi‑Agent Orchestration Pattern

## Goal

Show how multiple AI “roles” can cooperate to improve reliability and quality.

## Roles (Example)

- **Researcher:** Gathers raw options or ideas.
- **Critic:** Evaluates the Researcher’s output against a rubric.
- **Editor:** Produces final user‑facing text based on Critic feedback.

## Example Flow (High‑Level)

1. **Researcher Prompt:**
   “Generate 3 possible approaches to solve [USER PROBLEM]. Focus on high‑level steps, not code.”

2. **Critic Prompt:**
   “You are a careful reviewer. Given these 3 approaches, evaluate each on:
   - Clarity (1–5)
   - Safety / Risk (1–5)
   - Effort / Complexity (1–5)
   - Alignment with the user’s goal (1–5)
   Then recommend 1 approach and explain why.”

3. **Editor Prompt:**
   “You are an editor writing for the user. Take the Critic’s recommended approach and:
   - Explain it in clear, step‑by‑step language.
   - Include any warnings or caveats mentioned by the Critic.
   - Keep the tone calm and supportive.”

## Evaluation

Check:

- Did the Critic actually use the rubric, or just pick randomly?
- Did the Editor faithfully follow the Critic’s recommendation and warnings?
- Does the final answer reflect the user’s original goal?

Keep a few example flows in a simple table (Researcher → Critic → Editor) with comments on where the chain broke and how to adjust prompts.

## Related Spec

See [`specs/03_multi_agent_eval.yaml`](specs/03_multi_agent_eval.yaml) for machine-readable evaluation spec.
