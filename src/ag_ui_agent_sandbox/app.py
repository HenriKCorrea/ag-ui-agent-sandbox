from __future__ import annotations

__all__ = ["create_app"]

from agent_framework._clients import ChatClientProtocol
from azure.identity import DefaultAzureCredential
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework.openai import OpenAIChatClient
from agent_framework_ag_ui import add_agent_framework_fastapi_endpoint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ag_ui_agent_sandbox.agent import create_agent
from ag_ui_agent_sandbox.config import settings


def _build_chat_client() -> ChatClientProtocol:
    try:
        if bool(getattr(settings, "AZURE_OPENAI_ENDPOINT", None)):
            return AzureOpenAIChatClient(
                credential=DefaultAzureCredential(),
                deployment_name=getattr(
                    settings, "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "gpt-4o-mini"
                ),
                endpoint=settings.AZURE_OPENAI_ENDPOINT,
            )

        if bool(getattr(settings, "OPENAI_API_KEY", None)):
            # OpenAI setup - requires explicit model_id and api_key
            return OpenAIChatClient(
                model_id=getattr(settings, "OPENAI_CHAT_MODEL_ID", "gpt-4o-mini"),
                api_key=settings.OPENAI_API_KEY,
                base_url=getattr(settings, "OPENAI_API_BASE_URL", None),
            )

        raise ValueError(
            "Either AZURE_OPENAI_ENDPOINT or OPENAI_API_KEY environment variable is required"
        )

    except Exception as exc:  # pragma: no cover
        raise RuntimeError(
            "Unable to initialize the chat client. Double-check your API credentials as documented in README.md."
        ) from exc


def create_app() -> FastAPI:
    """Factory function to create and configure the FastAPI application."""

    chat_client = _build_chat_client()
    my_agent = create_agent(chat_client)

    app = FastAPI(title="CopilotKit + Microsoft Agent Framework (Python)")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    add_agent_framework_fastapi_endpoint(
        app=app,
        agent=my_agent,
        path="/",
    )

    return app
