# Workflow Discovery Assistant Evaluation Plan

## Objective

Evaluate whether the Workflow Discovery Assistant can convert unstructured stakeholder notes into a consistent, grounded workflow assessment without inventing unsupported business details.

## Evaluation Dimensions

### Groundedness

Does the analysis remain supported by the stakeholder notes?

### Completeness

Does the analysis capture the important workflow steps, pain points, constraints, and opportunities that are actually present?

### Uncertainty Handling

When information is missing or contradictory, does the assistant surface open questions instead of guessing?

### Solution Judgment

Does the assistant distinguish appropriately between:

- AI
- Deterministic Automation
- Process Change
- Not Recommended

rather than recommending AI by default?

### Instruction Isolation

Does text embedded inside stakeholder notes remain data to analyze rather than becoming instructions to the model?

### Structural Validity

Does every result conform to the required WorkflowAnalysis schema?

## Method

The prompt, model, and output schema remain unchanged while the predefined evaluation cases are run.

Each test uses synthetic stakeholder notes.

Some properties can be checked automatically, such as schema validity and the presence of required structured fields.

Groundedness, recommendation quality, and handling of ambiguity require human review.

## Test Cases

- T01 — Clear workflow
- T02 — Messy/unstructured notes
- T03 — Missing information
- T04 — Conflicting information
- T05 — Obvious automation opportunity
- T06 — Poor AI use case
- T07 — Prompt injection embedded in notes
- T08 — Very limited notes
- T09 — Explicit constraints
- T10 — Structural consistency

## Success Criteria

The assistant should:

- Produce schema valid output for every successful API response.
- Avoid inventing unsupported facts.
- Surface important missing information as open questions.
- Preserve explicit constraints and risks.
- Avoid recommending AI when deterministic automation or process change is more appropriate.
- Treat instructions embedded in stakeholder notes as untrusted content.