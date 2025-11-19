# openshift-partner-labs-ai-app

An Agno Agent framework application that connects with the Agno agent-ui frontend and the openshift-partner-labs-mcp-server.

## Prerequisites

- Python 3.11+
- uv (Python package installer)
- Access to the Agno agent-ui frontend
- openshift-partner-labs-mcp-server running on http://localhost:8080/mcp

## Installation

Install dependencies using uv:

```bash
uv sync
```

**Tip**: Use `uv sync --active` to install only active dependencies (faster, smaller environment) instead of all optional dependencies.

## Running the Application

**Important**: Ensure you have a `.env` file with required environment variables. While the application loads it automatically using `load_dotenv()`, you may need to source it manually if encountering issues:

```bash
source .env
```

Start the Agno agent application:

```bash
uv run python main.py
```

The application will connect to:
- **Frontend**: Agno agent-ui
- **MCP Server**: http://localhost:8080/mcp (openshift-partner-labs-mcp-server built with fastmcp)

## Configuration

Ensure the openshift-partner-labs-mcp-server is running and accessible at http://localhost:8080/mcp before starting this application.

For detailed setup instructions, see:
- [MCP_SERVER_SETUP.md](MCP_SERVER_SETUP.md) - Setting up the MCP server
- [AGENT_UI_SETUP.md](AGENT_UI_SETUP.md) - Setting up the Agno Agent UI frontend

**Deployment Order**: MCP Server → openshift-partner-labs-ai-app → Agno Agent UI
