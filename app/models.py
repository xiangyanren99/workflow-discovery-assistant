from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class AutomationOpportunity(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(
        description="Short name for the opportunity."
    )

    opportunity_type: Literal[
        "AI",
        "Deterministic Automation",
        "Process Change",
        "Not Recommended",
    ] = Field(
        description="The most appropriate solution type."
    )

    description: str = Field(
        description="What could be improved and how."
    )

    rationale: str = Field(
        description="Why this solution type is appropriate based only on the notes."
    )


class WorkflowAnalysis(BaseModel):
    model_config = ConfigDict(extra="forbid")

    workflow_name: str = Field(
        description="Concise name for the workflow. Use 'Unclear' if the notes do not support one."
    )

    summary: str = Field(
        description="Brief factual summary of the current workflow."
    )

    stakeholders: list[str] = Field(
        description="Stakeholder roles explicitly mentioned or clearly supported by the notes."
    )

    current_process: list[str] = Field(
        description="Ordered steps in the current workflow when supported by the notes."
    )

    pain_points: list[str] = Field(
        description="Problems, inefficiencies, or frustrations supported by the notes."
    )

    automation_opportunities: list[AutomationOpportunity] = Field(
        description="Potential improvements grounded in the stakeholder notes."
    )

    risks: list[str] = Field(
        description="Constraints, dependencies, risks, or concerns supported by the notes."
    )

    open_questions: list[str] = Field(
        description="Important information missing, unclear, or contradictory in the notes."
    )

    recommended_next_steps: list[str] = Field(
        description="Practical next discovery or validation steps."
    )