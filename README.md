> **Governance:** DGAF / Agent Amethyst — Curated under DGAF evaluation standards. IP-safe samples only. Governed by [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework).

> **Status: Stable — actively maintained.** Commit gaps reflect curation cadence, not abandonment. New samples added when eval-validated.

> **Lineage:** This is the **public-facing IP-safe portfolio** — a curated selection of prompt patterns safe for public display. It is distinct from the private `ai-prompt-engineering-portfolio` (full benchmark + Gold Star certification archive) and `AI-Prompt-Engineer` (historical archive with benchmark lineage). See [Prompt-Engineering Repo Map](#prompt-engineering-repo-map) below.

## Quick Overview (In Plain Language)

This repo is my **AI Prompt Engineering Portfolio**.

In simple terms:
- It collects real prompts I've designed for different use cases (agents, apps, workflows).
- It shows how I structure system prompts, instructions, and guardrails.
- It includes example tasks and model outputs so you can see how the prompts actually perform.

Right now this is an **active work-in-progress**:
- Some prompts are fully documented with inputs, outputs, and my evaluation notes.
- Others are early drafts or experiments.
- The goal is to make it easy for you to scan how I think about reliability, safety, and clarity in prompt design.

If you're a recruiter or engineer:
- Start by skimming one or two prompts in the `systems/` or `examples/` folders.
- Look for my comments and evaluation notes to see how I debug and improve prompts.
- Use this repo together with **junior-apogee-app** to see how prompts flow into evaluation.

---

## Prompt-Engineering Repo Map

| Repo | Visibility | Purpose | Status |
|------|-----------|---------|--------|
| **`ai-prompt-systems-portfolio`** (this repo) | Public | IP-safe curated samples — recruiter/engineer entry point | Active |
| `ai-prompt-engineering-portfolio` | Private | Full benchmark archive, Gold Star certification records, DGAF-governed master set | Active |
| `AI-Prompt-Engineer` | Private | Historical benchmark lineage — origin archive, pre-DGAF era | Archive/Reference |

---

# AI Prompt Systems Portfolio (IP‑Safe Samples)

This repository contains a small set of **public, IP‑safe examples** of my AI prompt systems work.

My private work includes more detailed frameworks (governance, frequency‑aware constraints, multi‑agent orchestration). Those are kept **private** to protect intellectual property and any future patentability. This repo is meant to show how I think and work, without exposing sensitive internals.

## Structure

Each entry lives in its own markdown file in this repo:

1. `01_state_anchor.md`
2. `02_constraint_gate.md`
3. `03_multi_agent_flow.md`
4. `04_parametric_constraint.md`
5. `05_error_recovery.md`

Each file follows the same format:
- Goal
- Example prompt or system message (simplified)
- Evaluation rubric (how I judge outputs)
- Notes on iteration and failure modes

---

## 1. State Anchor Prompt

**File:** `01_state_anchor.md`

**Goal:** Keep an assistant consistently “on persona” and in scope across a long conversation.
- Shows how I define role, boundaries, and what to ignore.
- Includes a short checklist I use to check if the assistant stayed anchored.

## 2. Constraint Gate (Guardrail)

**File:** `02_constraint_gate.md`

**Goal:** Enforce a small set of **non‑negotiable rules** (e.g., no legal advice, no internal tool names).
- Shows how I structure constraints in plain language.
- Includes a simple pass/fail rubric for whether the model respected constraints.

## 3. Multi‑Agent Orchestration Pattern

**File:** `03_multi_agent_flow.md`

**Goal:** Show how multiple AI “roles” can cooperate (e.g., Researcher → Critic → Editor).
- High‑level description of the roles and their responsibilities.
- Example of a review loop where one agent checks another against a rubric.

## 4. Parametric (“Dial”) Constraint Example

**File:** `04_parametric_constraint.md`

**Goal:** Demonstrate that I can tune behavior along a “dial” (e.g., strictness), **without** exposing proprietary math or full methodology.
- Describes a parameter like “strictness” and how it changes outputs.
- Shows how I would document and test different parameter settings.

## 5. Error Recovery & Robustness Prompt

**File:** `05_error_recovery.md`

**Goal:** Handle failures gracefully (bad tools, missing data, unclear instructions) instead of crashing or hallucinating.
- Outlines how the assistant should admit uncertainty and ask for clarification.
- Includes examples of “good” vs “bad” recovery behavior.

## How to Review This Repo in 3 Minutes

- 1 minute: Skim the top of this README to see what the portfolio covers.
- 1 minute: Open `01_state_anchor.md` and skim the goal, example, and notes.
- 1 minute: Open any other file (e.g., `03_multi_agent_flow.md`) to see how I think about multi‑agent prompts and evaluation.

## Taxonomy: Patterns & Workflows

This portfolio organizes prompts into four semantic categories:

### Patterns
- **State Anchor Prompt** (`01_state_anchor.md`): Maintain role consistency
- **Constraint Gate** (`02_constraint_gate.md`): Enforce non-negotiable rules
- **Parametric Constraints** (`04_parametric_constraint.md`): Tune behavior along a dial

### Workflows
- **Multi-Agent Orchestration** (`03_multi_agent_flow.md`): Sequential agent cooperation
- **Error Recovery** (`05_error_recovery.md`): Graceful failure handling

### Rubrics
Each prompt includes a **pass/fail evaluation rubric**:
- Does the output respect constraints?
- Does the output stay on-topic and in-role?
- Is uncertainty handled gracefully?

### Playbooks
See `specs/` folder for machine-readable evaluation specifications (YAML/JSON) that can be used to assess prompt outputs programmatically.

---

## Evaluation Specs & CLI

To evaluate a prompt output against a rubric:

```bash
python -m portfolio.eval specs/example.yaml --input "<prompt>" --output "<model response>"
```

Specs live in `specs/` and follow this structure:

```yaml
name: "State Anchor Evaluation"
metrics:
  - name: "role_consistency"
    type: "boolean"
    description: "Did the assistant stay in role?"
  - name: "scope_adherence"
    type: "boolean"
    description: "Did the assistant respect boundaries?"
  - name: "helpfulness"
    type: "score"
    min: 0
    max: 5
rules:
  - if: "role_consistency == false"
    then: "pass = false"
```

See `specs/example.yaml` for a complete example.

## Related Projects

- [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) — governance spine
- [junior-apogee-app](https://github.com/ndrorchestration/junior-apogee-app) — primary agent evaluation platform
- [resumeapex-eval](https://github.com/ndrorchestration/resumeapex-eval) — flagship benchmark
- [Gold-star-standards](https://github.com/ndrorchestration/Gold-star-standards) — certification rubrics (private)
- [sentinel-governance](https://github.com/ndrorchestration/sentinel-governance) — CI/CD governance enforcement
