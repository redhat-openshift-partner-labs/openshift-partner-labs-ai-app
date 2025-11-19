# MCP Server Setup Guide

This guide explains how to set up and run the openshift-partner-labs-mcp-server required by this application.

## Prerequisites

- Python 3.11+
- uv (Python package installer)
- git

## Installation

1. Clone the MCP server repository:

```bash
git clone https://github.com/redhat-openshift-partner-labs/openshift-partner-labs-mcp-server.git
cd openshift-partner-labs-mcp-server
```

2. Checkout PR #17 (required until merged):

```bash
gh pr checkout 17
```

Or manually fetch the PR:

```bash
git fetch origin pull/17/head:pr-17
git checkout pr-17
```

3. Install dependencies:

```bash
uv sync
```

**Tip**: Use `uv sync --active` to install only active dependencies (faster, smaller environment) instead of all optional dependencies.

## Running the MCP Server

Start the MCP server using one of the following methods:

### Option 1: Using uv run prefix

```bash
uv run python -m openshift_partner_labs_mcp_server.src.main
```

### Option 2: Using uv venv

```bash
source .venv/bin/activate
python -m openshift_partner_labs_mcp_server.src.main
```

The MCP server will start and be accessible at http://localhost:8080/mcp

## Verification

Verify the server is running by checking the endpoint:

```bash
curl http://localhost:8080/mcp
```

Once the MCP server is running, you can start the main application following the instructions in [README.md](README.md).
