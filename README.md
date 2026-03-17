## Quick Overview (In Plain Language)

This repo is my **AI Prompt Engineering Portfolio**.

In simple terms:
- It collects real prompts I’ve designed for different use cases (agents, apps, workflows).
- It shows how I structure system prompts, instructions, and guardrails.
- It includes example tasks and model outputs so you can see how the prompts actually perform.

Right now this is an **active work-in-progress**:
- Some prompts are fully documented with inputs, outputs, and my evaluation notes.
- Others are early drafts or experiments.
- The goal is to make it easy for you to scan how I think about reliability, safety, and clarity in prompt design.

If you’re a recruiter or engineer:
- Start by skimming one or two prompts in the `systems/` or `examples/` folders.
- Look for my comments and evaluation notes to see how I debug and improve prompts.
- Use this repo together with **junior-apogee-app** to see how prompts flow into evaluation.

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
