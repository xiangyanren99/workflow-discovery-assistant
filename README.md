# workflow-discovery-agent
A Python AI application that converts stakeholder interview notes into structured requirements, risks, and solution recommendations.

Who is the user?
What problem do they experience?
How do they handle it today?
What will the proposed solution do?
How will success be measured?
What must the solution not do?

Technical consultants must convert unstructured stakeholder conversations into clear problem statements, requirements, risks and proposed solutions. This analysis is often manual, and important constraints or unanswered questions can be overlooked. This project will demonstrate a Python application that uses an LLM and a validated output schema to transform synthetic stakeholder interview notes into structured discovery documentation. The application will distinguish information explicitly stated by the stakeholder from conclusions inferred by the model and will allow users to review the output before saving any results. Success will be measured through schema-validation tests, comparison against expected outputs and evaluation of whether the assistant identifies the major users, pain points, requirements, constraints and follow-up questions.
