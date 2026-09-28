import json
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from app.models import WorkflowAnalysis


load_dotenv()

client = OpenAI()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROMPT_PATH = PROJECT_ROOT / "prompts" / "analysis-instructions.md"


def load_instructions() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


def analyze_workflow(notes: str) -> WorkflowAnalysis:
    if not notes.strip():
        raise ValueError("Stakeholder notes cannot be empty.")

    instructions = load_instructions()

    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions=instructions,
        input=notes,
        text={
            "format": {
                "type": "json_schema",
                "name": "workflow_analysis",
                "schema": WorkflowAnalysis.model_json_schema(),
                "strict": True,
            }
        },
        store=False,
    )

    raw_data = json.loads(response.output_text)

    return WorkflowAnalysis.model_validate(raw_data)


if __name__ == "__main__":
    sample_notes = """
    Scheduling coordinators receive clinician availability by email,
    text message, and sometimes phone calls.

    Every morning a coordinator manually compares availability against
    unassigned home visits and updates a shared spreadsheet.

    The coordinator said this usually takes about an hour and mistakes
    happen when availability changes after the spreadsheet is updated.

    Managers want fewer scheduling errors but have not decided whether
    clinicians should update availability directly in another system.
    """

    analysis = analyze_workflow(sample_notes)

    print(analysis.model_dump_json(indent=2))