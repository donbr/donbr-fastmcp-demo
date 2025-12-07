# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastMCP quickstart example repository demonstrating a simple echo server. FastMCP is a framework for building Model Context Protocol (MCP) servers that can be deployed to FastMCP Cloud.

## Core Architecture

The repository contains a single MCP server (`echo.py`) that demonstrates FastMCP's three main primitives:

- **Tools**: Functions that LLMs can call (decorated with `@mcp.tool`)
- **Resources**: URI-accessible data sources (decorated with `@mcp.resource`)
- **Prompts**: Reusable prompt templates (decorated with `@mcp.prompt`)

The server is instantiated using `mcp = FastMCP("Echo Server")` and all decorated functions are automatically registered.

## Running the Server

To run the MCP server locally:
```bash
python echo.py
```

FastMCP servers use the Model Context Protocol and are designed to be consumed by MCP clients (like Claude Desktop) or deployed to FastMCP Cloud.

## Deployment

This repository is configured for deployment to FastMCP Cloud:
1. Create a FastMCP Cloud account at http://fastmcp.cloud/signup
2. Connect your GitHub account
3. Select this repository for deployment

Committing changes to GitHub will trigger a new deployment automatically.

**Authentication Mode**: Private (FastMCP Cloud organization members only)

### Authentication

This server uses FastMCP's authentication system:

**Production (FastMCP Cloud)**: When deployed with Private mode, FastMCP Cloud automatically handles authentication. Only members of your FastMCP Cloud organization can access the server.

**Local Development**: For local testing with bearer token authentication:
```bash
# Set environment variables for static token verification
export FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.jwt.StaticTokenVerifier
export FASTMCP_SERVER_AUTH_JWT_TOKENS='{"dev-token": {"client_id": "dev-user", "scopes": ["read", "write"]}}'

# Run the server
python echo.py
```

Then connect with bearer token:
```bash
curl -H "Authorization: Bearer dev-token" http://localhost:8000/mcp
```

### Adding the Server to Claude Code

To add this deployed server as an MCP server in Claude Code:
```bash
claude mcp add --scope local --transport http donbr-fastmcp-demo https://donbr-fastmcp-demo.fastmcp.app/mcp
```

**Note**: For private servers, you may need to authenticate. See the [GitHub issue on Claude Code authentication](https://github.com/anthropics/claude-code/issues) for current status of bearer token support.

## Adding New Functionality

When extending this server:
- Add new tools with `@mcp.tool` decorator for LLM-callable functions
- Add new resources with `@mcp.resource("uri://path")` for static resources or `@mcp.resource("uri://{param}")` for dynamic/templated resources
- Add new prompts with `@mcp.prompt("name")` for reusable prompt templates
- All decorated functions should include type hints and docstrings

## Dependencies

The project requires the `fastmcp` package. Installation details are available at https://gofastmcp.com/
