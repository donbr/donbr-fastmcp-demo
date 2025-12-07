"""
FastMCP Echo Server

This server demonstrates FastMCP authentication patterns.
When deployed to FastMCP Cloud with Private mode, authentication
is handled automatically by the platform.

For local development with bearer token authentication, set:
    FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.jwt.StaticTokenVerifier
    FASTMCP_SERVER_AUTH_JWT_TOKENS='{"dev-token": {"client_id": "dev-user", "scopes": ["read", "write"]}}'
"""

import os
from fastmcp import FastMCP

# Create server - authentication is configured via environment variables
# or automatically by FastMCP Cloud when deployed with Private mode
mcp = FastMCP("Echo Server")


@mcp.tool
def echo_tool(text: str) -> str:
    """Echo the input text"""
    return text


@mcp.resource("echo://static")
def echo_resource() -> str:
    return "Echo!"


@mcp.resource("echo://{text}")
def echo_template(text: str) -> str:
    """Echo the input text"""
    return f"Echo: {text}"


@mcp.prompt("echo")
def echo_prompt(text: str) -> str:
    return text
