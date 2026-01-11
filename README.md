# CopilotKit <> Microsoft Agent Framework (Python)

This is a starter template for building CopilotKit experiences using the [Microsoft Agent Framework](https://aka.ms/agent-framework). It ships with a Next.js UI and a FastAPI server that exposes a Microsoft Agent Framework agent over the AG-UI protocol, so you can study and customize both sides of the stack.

For better development experience, frontend and backend were split into separate projects.
This project is the python backend using [Microsoft Agent Framework](https://aka.ms/agent-framework).

## Prerequisites

- OpenAI credentials (for the Microsoft Agent Framework agent)
- [uv](https://docs.astral.sh/uv/) (Python package and project manager)
- [Docker](https://docs.docker.com/engine/install/) (optional for observability)

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

   See [.env.example](.env.example) for complete environment variable usage with example and comments.

3. Run the agent using uv:

   ```bash
   uv run src/main.py
   ```

   This will start the Microsoft Agent Framework server.

## 📊 Optional: Langfuse Observability Backing Service

This project supports integration with [Langfuse](https://langfuse.com/) for advanced observability, tracing, and analytics of your agent's operations. Langfuse provides dashboards and tools to monitor, debug, and analyze LLM application behavior in production or development.

### How to Enable Langfuse

1. **Start the Langfuse stack locally:**
   - Use the provided [observability-compose.yml](backing_services/observability-compose.yml) file to spin up Langfuse and its dependencies using Docker Compose:
     ```bash
     cd backing_services
     docker compose -f observability-compose.yml up
     ```
   - This will start all required services for Langfuse on your local machine. By default, the Langfuse web UI will be available at [http://localhost:3001](http://localhost:3001).

2. **Configure your agent to use Langfuse:**
   - Set the following environment variables in your `.env` file (see [.env.example](.env.example) observability section):
     - `LANGFUSE_SECRET_KEY` – Private API key for server-to-server requests
     - `LANGFUSE_PUBLIC_KEY` – Public API key for client/browser requests
     - `LANGFUSE_BASE_URL` – Base URL of your Langfuse instance (e.g., `http://localhost:3001`)

3. **Access the Langfuse dashboard:**
   - Open [http://localhost:3001](http://localhost:3001) in your browser to view traces, logs, and analytics.

> **Note:** The [observability-compose.yml](backing_services/observability-compose.yml) file contains placeholder secrets and example credentials. For production use, update these values and secure your environment accordingly. Note that your `.env` file shall reflect changes made to `observability-compose.yml`

## 📚 Documentation

- [Microsoft Agent Framework](https://aka.ms/agent-framework) – Learn more about Microsoft Agent Framework and its features
- [CopilotKit Documentation](https://docs.copilotkit.ai) – Explore CopilotKit’s capabilities
- [Dynaconf Documentation](https://www.dynaconf.com/) – Configuration management library used in this project
- [Langfuse Documentation](https://langfuse.com/docs)

## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
