from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    load_dotenv=True,
    validators=[
        Validator(
          "CHAT_CLIENT_MODEL_ID",
            description="The model identifier to use for the chat client. E.g.: gpt-4o-mini",
            required=True,
        ),
        Validator(
            "CHAT_CLIENT_API_KEY",
            description="The API token for the chat client.",
            default=None,
        ),
        Validator(
            "CHAT_CLIENT_BASE_URL",
            description="Override default base URL for the chat client.",
            default=None,
        ),
        Validator(
            "AGENT_HOST",
            description="The host address for the agent server",
            default="0.0.0.0",
        ),
        Validator(
            "AGENT_PORT",
            description="The port number for the agent server",
            default=8000,
            cast=int,
        ),
        Validator(
            "APP_LOG_LEVEL",
            description="Logging level for your application",
            is_in=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET", None],
            default=None,
        ),
        Validator(
            "WEBSERVER_LOG_LEVEL",
            description="Logging level for the web server",
            is_in=["critical", "error", "warning", "info", "debug", "trace", None],
            default=None,
        ),
    ],
)
