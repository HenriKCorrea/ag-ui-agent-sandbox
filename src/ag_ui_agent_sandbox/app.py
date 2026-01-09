from __future__ import annotations

__all__ = ["create_app"]

from agent_framework._clients import ChatClientProtocol
from agent_framework.openai import OpenAIChatClient
from agent_framework_ag_ui import add_agent_framework_fastapi_endpoint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ag_ui_agent_sandbox.agent import create_agent
from ag_ui_agent_sandbox.config import settings


def _build_chat_client() -> ChatClientProtocol:
    """Builds and returns the appropriate ChatClient based on configuration."""
    
    return OpenAIChatClient(
        model_id=settings.CHAT_CLIENT_MODEL_ID,
        api_key=settings.CHAT_CLIENT_API_KEY,
        base_url=settings.CHAT_CLIENT_BASE_URL,
    )

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
