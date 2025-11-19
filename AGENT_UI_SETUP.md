# Agno Agent UI Setup Guide

This guide explains how to set up and run the Agno agent-ui frontend.

## Deployment Order

**Important**: Deploy components in this order:

1. MCP Server (see [MCP_SERVER_SETUP.md](MCP_SERVER_SETUP.md))
2. openshift-partner-labs-ai-app (this application - see [README.md](README.md))
3. Agno Agent UI (this guide)

## Prerequisites

- Node.js >= 22
- pnpm
- git

## Installation

1. Install pnpm if not already installed:

```bash
npm install -g pnpm
```

2. Clone the Agno agent-ui repository:

```bash
git clone https://github.com/agno-agi/agent-ui.git
cd agent-ui
```

3. Install dependencies:

```bash
pnpm install
```

## Running the Agent UI

Start the development server:

```bash
pnpm dev
```

The agent UI will start and connect to the openshift-partner-labs-ai-app backend.

## Verification

Access the UI in your browser at the URL provided by the dev server (typically http://localhost:3000 or similar).

Ensure all three components are running:
- MCP Server at http://localhost:8080/mcp
- openshift-partner-labs-ai-app backend
- Agno Agent UI frontend
