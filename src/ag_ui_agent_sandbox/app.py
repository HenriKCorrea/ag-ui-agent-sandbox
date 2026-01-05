from __future__ import annotations


__all__ = ["create_app"]

import os

from agent_framework._clients import ChatClientProtocol
from azure.identity import DefaultAzureCredential
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework.openai import OpenAIChatClient
from agent_framework_ag_ui import add_agent_framework_fastapi_endpoint
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ag_ui_agent_sandbox.agent import create_agent


def _build_chat_client() -> ChatClientProtocol:
    try:
        if bool(os.getenv("AZURE_OPENAI_ENDPOINT")):
            # Azure OpenAI setup - uses environment variables by default
            # Optionally can pass deployment_name explicitly
            deployment_name = os.getenv(
                "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "gpt-4o-mini"
            )
            return AzureOpenAIChatClient(
                credential=DefaultAzureCredential(),
                deployment_name=deployment_name,
                endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            )

        if bool(os.getenv("OPENAI_API_KEY")):
            # OpenAI setup - requires explicit model_id and api_key
            return OpenAIChatClient(
                model_id=os.getenv("OPENAI_CHAT_MODEL_ID", "gpt-4o-mini"),
                api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_API_BASE_URL"),
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
    # Ensure env vars are loaded when the app is created
    load_dotenv()

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
