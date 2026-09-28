import streamlit as st

from app.analyzer import analyze_workflow


st.set_page_config(
    page_title="Workflow Discovery Assistant",
    page_icon="🔎",
    layout="wide",
)


def render_list(title: str, items: list[str]) -> None:
    st.subheader(title)

    if not items:
        st.caption("No supported information identified.")
        return

    for item in items:
        st.markdown(f"- {item}")


st.title("Workflow Discovery Assistant")

st.markdown(
    """
    Turn messy stakeholder interview notes into a structured workflow assessment
    with **pain points, risks, automation opportunities, open questions, and next steps**.
    """
)

feature_one, feature_two, feature_three = st.columns(3)

with feature_one:
    st.markdown("**📋 Structured Analysis**")
    st.caption("Convert unstructured notes into a consistent workflow assessment.")

with feature_two:
    st.markdown("**⚙️ AI vs Automation**")
    st.caption("Distinguish AI opportunities from deterministic automation and process change.")

with feature_three:
    st.markdown("**❓ Discovery Questions**")
    st.caption("Surface missing information instead of guessing.")

st.write("")

with st.container(border=True):
    st.subheader("Stakeholder Notes")

    st.caption(
        "Paste synthetic or non-sensitive stakeholder interview notes below."
    )

    notes = st.text_area(
        "Interview notes",
        height=300,
        placeholder=(
            "Example:\n\n"
            "Scheduling coordinators receive clinician availability by email, "
            "text message, and phone calls...\n\n"
            "Every morning a coordinator manually compares availability..."
        ),
        label_visibility="collapsed",
    )

    analyze_clicked = st.button(
        "Analyze Workflow",
        type="primary",
        use_container_width=True,
    )

st.info(
    "For this portfolio demonstration, use synthetic or non-sensitive information only."
)

if "analysis" not in st.session_state:
    st.session_state.analysis = None


if analyze_clicked:
    if not notes.strip():
        st.warning("Enter stakeholder notes before running the analysis.")

    else:
        try:
            with st.spinner("Analyzing workflow..."):
                st.session_state.analysis = analyze_workflow(notes)

        except Exception as error:
            st.session_state.analysis = None
            st.error(f"Analysis Failed: {error}")


analysis = st.session_state.analysis


if analysis is not None:
    st.divider()

    st.header(analysis.workflow_name)
    st.write(analysis.summary)

    left_column, right_column = st.columns(2)

    with left_column:
        render_list(
            "Stakeholders",
            analysis.stakeholders,
        )

        render_list(
            "Current Process",
            analysis.current_process,
        )

    with right_column:
        render_list(
            "Pain Points",
            analysis.pain_points,
        )

        render_list(
            "Risks",
            analysis.risks,
        )

    st.divider()

    st.subheader("Automation Opportunities")

    if not analysis.automation_opportunities:
        st.caption("No automation opportunities identified.")

    for opportunity in analysis.automation_opportunities:
        with st.expander(
            f"{opportunity.title} — {opportunity.opportunity_type}",
            expanded=True,
        ):
            st.markdown(f"**Type:** {opportunity.opportunity_type}")
            st.write(opportunity.description)

            st.markdown("**Rationale**")
            st.write(opportunity.rationale)

    st.divider()

    bottom_left, bottom_right = st.columns(2)

    with bottom_left:
        render_list(
            "Open Questions",
            analysis.open_questions,
        )

    with bottom_right:
        render_list(
            "Recommended Next Steps",
            analysis.recommended_next_steps,
        )

    st.divider()

    with st.expander("Developer View"):
        st.json(analysis.model_dump())

    st.download_button(
        label="Download Analysis as JSON",
        data=analysis.model_dump_json(indent=2),
        file_name="workflow-analysis.json",
        mime="application/json",
    )