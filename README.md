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

2. Set up your agent credentials. The backend automatically uses Azure when the Azure env vars below are present; otherwise it falls back to OpenAI. Create a `.env` file using [example.env](/example.env) as template (documentation included).

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
