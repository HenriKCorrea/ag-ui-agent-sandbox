from agent_framework_ag_ui import AgentFrameworkAgent
from langfuse import propagate_attributes
from opentelemetry import trace
from contextlib import nullcontext

__all__ = ["TelemetryAgentFrameworkAgent"]

class TelemetryAgentFrameworkAgent(AgentFrameworkAgent):
    """
    An AgentFrameworkAgent subclass that propagates AG-UI telemetry attributes (such as session and run IDs)
    to Langfuse and OpenTelemetry for each agent run.

    This class specifically maps AG-UI semantics:
        - threadId (AG-UI conversation/session) → Langfuse session_id
        - runId (AG-UI request/execution) → Langfuse metadata/run_id

    By tailoring AG-UI's identifiers into Langfuse's observability model, this enables traceability,
    debugging, and analytics that are consistent with AG-UI's conversation and execution concepts.
    """

    async def run_agent(self, input_data):
        """
        Run the agent with AG-UI telemetry context propagation.

        Extracts AG-UI telemetry attributes from the input data (such as threadId, runId),
        maps them to Langfuse observability attributes (session_id, metadata/run_id),
        and propagates them to Langfuse and OpenTelemetry for the duration of the agent run.

        Args:
            input_data (dict): The input data for the agent run, expected to contain AG-UI telemetry keys.

        Yields:
            Agent events as produced by the parent class's run_agent method.
        """
        # Extract telemetry attributes from input_data
        # session_id is the conversation history identifier. Maps to threadId in AG-UI.
        # run_id is the unique identifier for a single request in AG-UI.
        attributes = {
            "session_id": input_data.get("threadId", None),
            "metadata": {
                k: v for k, v in {
                    "run_id": input_data.get("runId", None),
                    # Add more keys here as needed
                }.items() if v is not None
            # Add more top-level attributes here as needed
            } or None,
        }
        # Remove keys with None values
        attributes = {k: v for k, v in attributes.items() if v is not None}

        with propagate_attributes(**attributes) if attributes else nullcontext():
            # Set OpenTelemetry span attribute for conversation id
            current_span = trace.get_current_span()
            if current_span and current_span.is_recording() and attributes.get("session_id"):
                current_span.set_attribute("gen_ai.conversation.id", attributes["session_id"])

            # Delegate to the original run_agent logic
            async for event in super().run_agent(input_data):
                yield event