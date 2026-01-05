from __future__ import annotations

__all__ = ["main"]

import os

import uvicorn
from dotenv import load_dotenv


def main() -> None:
    """Entry point for the application."""

    load_dotenv()
    host = os.getenv("AGENT_HOST", "0.0.0.0")
    port = int(os.getenv("AGENT_PORT", "8000"))
    # Use the full package path for reload to work correctly
    uvicorn.run(
        "ag_ui_agent_sandbox.app:create_app",
        host=host,
        port=port,
        reload=True,
        factory=True,
    )


if __name__ == "__main__":
    main()
