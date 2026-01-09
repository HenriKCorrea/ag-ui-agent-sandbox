from __future__ import annotations

__all__ = ["main"]

import logging
import uvicorn
from ag_ui_agent_sandbox.config import settings


def main() -> None:
    """Entry point for the application."""
    
    logging.basicConfig(level=settings.APP_LOG_LEVEL)

    # Use the full package path for reload to work correctly
    uvicorn.run(
        "ag_ui_agent_sandbox.app:create_app",
        host=settings.AGENT_HOST,
        port=settings.AGENT_PORT,
        reload=True,
        factory=True,
        log_level=settings.WEBSERVER_LOG_LEVEL
    )


if __name__ == "__main__":
    main()
