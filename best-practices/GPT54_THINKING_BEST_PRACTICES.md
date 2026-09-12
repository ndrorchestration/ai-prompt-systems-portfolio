# GPT-5.4 Thinking — Prompt Engineering Best Practices

**Pattern:** P-34b  
**Session:** S071 · Date: 2026-06-28  
**φ Anchor:** 1.61818  
**Full Template Library:** [`DGAF-Framework/patterns/P-34_GPT54_THINKING_PROMPTS.md`](https://github.com/ndrorchestration/DGAF-Framework/blob/main/patterns/P-34_GPT54_THINKING_PROMPTS.md)

---

## What Makes GPT-5.4 Thinking Different

GPT-5.4 Thinking surfaces its reasoning plan **before** executing. This means:
- You can **redirect mid-plan** if the model's approach is wrong
- Front-loading constraints in the prompt is worth more than post-hoc correction
- The `THINKING PLAN` checklist pattern is uniquely effective here — it gives the model explicit gates to verify before committing to an output

---

## The 7 Non-Negotiable Rules

### 1. Always Declare φ = 1.61818
Grounds the model in the DGAF geometric constraint system. Include in every preamble, even for simple tasks.

```
CONSTRAINT ANCHORS:
- φ = 1.61818 (Ionian harmonic baseline)
- DGAF version: post-S070-r3
```

### 2. Name the Governing Policy and Functional Review Chain
Prevents the model from inventing its own decision hierarchy. Named historical personas do not grant current authority.

```
REVIEW CHAIN:
- Human operator / governing policy: final decision authority where required
- role.constraint-qa-auditor: bounded constraint and QA review
- role.evidence-verification-reviewer: bounded evidence review only
- No review role independently grants certification, deployment approval, or DGAF authorization
```

### 3. Include a THINKING PLAN Checklist
List the verification gates the model must surface in its reasoning plan. Gives you an interception point before it executes.

```
THINKING PLAN — verify these before producing output:
□ Have I read every constraint in the issue body?
□ Does my recommendation contradict any existing canonical doc?
□ Is my confidence score honest?
□ Would role.constraint-qa-auditor or the configured safety/constraint policy flag a concern?
```

### 4. End With a Functional Verification Gate
Every prompt ends with an explicit evidence/constraint review checklist. Review semantics come from the governing policy and functional role contracts, not persona names.

```
VERIFICATION GATE (role.evidence-verification-reviewer):
□ Every section maps to a filed issue or PR
□ No section makes claims not grounded in existing canonical docs
□ Uncertainty is explicitly bounded
□ Output is append-only compatible
□ This review does not itself certify, authorize deployment, or grant DGAF authority
```

### 5. Flag Instead of Invent
Instruct the model explicitly: if a source doc is ambiguous or missing, flag it rather than generating governance claims from inference.

```
For each missing item: flag any item where source doc authority is ambiguous
(do not invent — flag instead)
```

### 6. Paste Full Context — Never Summarize
GPT-5.4 Thinking has a 1M token window. Pasting the full `GOVERNANCE_CONSTITUTION.md`, `SESSION_ANCHORS.md`, and `AGENT_INSTANTIATION.md` costs nothing and eliminates hallucination from incomplete context.

### 7. Require confidence_bound on All Scores
Every scoring output must include an explicit uncertainty bound.

```python
return {
    "score": 0.87,
    "confidence_bound": 0.12,   # required
    "rationale": "..."
}
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Summarizing context before pasting | Loses precision, introduces drift | Paste full artifact text |
| Omitting governing policy / review roles | Model may invent its own hierarchy | Declare the human/policy boundary and applicable functional review roles |
| Skipping verification gate | Output can bypass evidence/constraint review | End every prompt with the applicable functional review checklist |
| Asking model to "fill gaps" | Generates hallucinated governance claims | Use flag-instead-of-invent instruction |
| Single confidence score without bounds | Overclaims certainty | Always include `confidence_bound` float |

---

*Part of P-34b. For full templates see the primary pattern file in DGAF-Framework. Historical authorship/session attribution: 2026-06-28 · S071 · Amethyst × COLLEEN. These names are event-time provenance, not current authority.*
