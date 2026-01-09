from __future__ import annotations

__all__ = ["main"]

import uvicorn
from ag_ui_agent_sandbox.config import settings


def main() -> None:
    """Entry point for the application."""

    host = getattr(settings, "AGENT_HOST", "0.0.0.0")
    port = int(getattr(settings, "AGENT_PORT", 8000))
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
