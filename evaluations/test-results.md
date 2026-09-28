# Evaluation Results

## Summary

- Total test cases: 10
- Structural/API success: 10/10
- Structural pass rate: 100%
- Human quality success: 10/10
- Human quality pass rate: 100%

## Scope

These results are based on a small, synthetic, manually reviewed evaluation set.

Structural success means:
- the API request completed successfully
- the response conformed to the required `WorkflowAnalysis` schema
- Pydantic validation succeeded

Human quality success means:
- the output remained grounded in the supplied notes
- important workflow details were preserved
- uncertainty and contradictions were surfaced appropriately
- AI was not recommended by default
- prompt injection content remained data rather than instructions