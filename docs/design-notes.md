# Design Notes

## Problem

Stakeholder discovery notes are often incomplete, inconsistent, and unstructured. 
The application converts those notes into a repeatable workflow assessment without 
assuming that AI is always the right solution.

## Separation of Concerns

The project separates:

- `models.py` — structured data contract
- `analyzer.py` — AI/API orchestration
- `analysis-instructions.md` — behavioral instructions
- `streamlit_app.py` — presentation layer

This allows the reasoning layer and UI to evolve independently.

## Structured Outputs

Pydantic models define the expected response structure.

The same model is used for:

1. JSON Schema supplied to the model
2. runtime validation of the returned data
3. rendering results in the UI
4. exporting machine-readable JSON

## AI vs. Traditional Automation

The assistant does not assume every workflow should use AI.

It distinguishes among AI, deterministic automation, process changes,
and situations where automation is not recommended.

## Grounding and Uncertainty

When stakeholder notes do not provide enough information, the assistant
surfaces open questions rather than inventing missing workflow details.

Conflicting stakeholder statements are preserved as uncertainty rather
than silently reconciled.

## Prompt Injection

Stakeholder notes are treated as untrusted content.

Instruction like text embedded inside the notes is analyzed as data and
does not override the application's instructions or required output format.

## Data Boundary

The portfolio application is intended for synthetic or non-sensitive information only.