# CopilotKit <> Microsoft Agent Framework (Python)

This is a starter template for building CopilotKit experiences using the [Microsoft Agent Framework](https://aka.ms/agent-framework). It ships with a Next.js UI and a FastAPI server that exposes a Microsoft Agent Framework agent over the AG-UI protocol, so you can study and customize both sides of the stack.

For better development experience, frontend and backend were split into separate projects.
This project is the python backend using [Microsoft Agent Framework](https://aka.ms/agent-framework).

## Prerequisites

- OpenAI or Azure OpenAI credentials (for the Microsoft Agent Framework agent)
- Python 3.12+
- uv

## Getting Started

1. Install dependencies and create virtual environment using uv:

   ```bash
   uv sync
   ```

2. Configure your chat client credentials using environment variables or a `.env` file.

   [Dynaconf](https://www.dynaconf.com/) library is used for configuration management with validators defined in [config.py](src/ag_ui_agent_sandbox/config.py). Check the validators for environment variable names, detailed descriptions, default values, and constraints for each setting.

   **Important:** You must prefix all configuration keys with `DYNACONF_`. For example, `CHAT_CLIENT_MODEL_ID` becomes `DYNACONF_CHAT_CLIENT_MODEL_ID`.

   **Example `.env` file:**
   ```bash
   # Required
   DYNACONF_CHAT_CLIENT_MODEL_ID="gpt-4o-mini"
   
   # Optional - for OpenAI or compatible providers
   DYNACONF_CHAT_CLIENT_API_KEY="your_api_key_here"
   DYNACONF_CHAT_CLIENT_BASE_URL="https://api.openai.com/v1"
   ```

3. Run the agent using uv:

   ```bash
   uv run src/main.py
   ```

   This will start the Microsoft Agent Framework server.

## 📚 Documentation

- [Microsoft Agent Framework](https://aka.ms/agent-framework) – Learn more about Microsoft Agent Framework and its features
- [CopilotKit Documentation](https://docs.copilotkit.ai) – Explore CopilotKit’s capabilities- [Dynaconf Documentation](https://www.dynaconf.com/) – Configuration management library used in this project
## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
