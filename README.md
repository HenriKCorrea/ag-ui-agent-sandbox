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

2. Set up your agent credentials. The backend automatically uses Azure when the Azure env vars below are present; otherwise it falls back to OpenAI. Create a `.env` file with one of the following configurations:

   **OpenAI**
   ```
   OPENAI_API_KEY=sk-...your-openai-key-here...
   OPENAI_CHAT_MODEL_ID=gpt-4o-mini
   # If you want to use another model provider:
   # OPENAI_API_BASE_URL="https://openrouter.ai/api/v1"
   ```

   **Azure OpenAI**
   ```
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
   # If you are not relying on az login:
   # AZURE_OPENAI_API_KEY=...
   ```

3. Run the agent using uv:

   ```bash
   uv run src/main.py
   ```

   This will start the Microsoft Agent Framework server.

## 📚 Documentation

- [Microsoft Agent Framework](https://aka.ms/agent-framework) – Learn more about Microsoft Agent Framework and its features
- [CopilotKit Documentation](https://docs.copilotkit.ai) – Explore CopilotKit’s capabilities

## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
