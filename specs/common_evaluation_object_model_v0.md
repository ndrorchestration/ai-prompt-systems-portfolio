# Common Evaluation Object Model v0

Controller: issue #8.

## Purpose

This document defines a deliberately small interoperability vocabulary for evaluation projects that otherwise retain their own scoring models, runtime semantics, evidence boundaries, and governance relationships.

The common model does **not** make the projects one system.

## Shared objects

### EvaluationCase

A bounded unit to be evaluated. A case identifies the subject/input and any expected/reference material without defining the project's scoring semantics.

### EvaluationRun

One execution or assessment over one or more cases under named criteria and provenance. A run may carry replay information when the project supports deterministic or bounded replay.

### CriterionRef

A reference to a project-local criterion. The common core does not redefine the criterion.

Examples:
- ResumeApex may reference Goldcanstaytoday Performance, Reciprocity, or Amethyst/Apogee Meta criteria.
- Driftwatch may reference a drift score, trajectory condition, threshold check, or other local evaluator concept.

### EvidenceArtifact

A retained artifact used by a finding: dataset/fixture identity, output, metric record, trace, observation bundle, or similar evidence.

### Finding

A bounded result tied to a criterion and evidence artifacts. A finding is not automatically a governance decision.

### ClaimCeiling

The allowed interpretation and explicit prohibited promotions for a result.

Every mapped project must provide a claim ceiling.

### ReplayBinding

The inputs required to reproduce or meaningfully replay an evaluation where replay is supported. A project may use seeds, dataset hashes, evaluator versions, configuration hashes, observation-window identifiers, or similar bindings.

### ProvenanceBinding

Source identities required to understand where the evaluated inputs, evaluator semantics, or evidence artifacts came from.

### EvaluationDecision

A reporting/evaluation disposition over findings under a ClaimCeiling.

`EvaluationDecision.authorization_effect` is always `NONE`.

It cannot authorize:
- runtime action;
- repository mutation;
- deployment;
- release;
- governance transition;
- scientific claim promotion.

## Required separations

- observation is not evaluation;
- evaluation is not governance;
- reporting is not authorization;
- evidence in one project does not transfer to another project;
- mapping a project into this model does not validate that project;
- a common object name does not imply common scoring semantics.

## Explicitly non-common concepts

The following stay local to their source systems:

- DGAF authorization state and scientific-state transitions;
- ACP admission/execution authority;
- AOSS assurance state;
- Goldcanstaytoday Performance / Reciprocity / Amethyst-Apogee Meta taxonomy;
- Driftwatch drift functionals, thresholds, trajectory semantics, and calibration claims;
- project-specific statistical estimators, rubrics, weighting schemes, or aggregation formulas.

## Evidence boundary

Conformance to this model demonstrates only that a project can express selected evaluation records through the shared vocabulary without surrendering local meaning. It does not establish model performance, detector efficacy, independent validation, certification/compliance, production readiness, or evidence transfer.
