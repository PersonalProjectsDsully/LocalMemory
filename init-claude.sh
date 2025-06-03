#!/bin/bash
set -e

# Install Claude Code globally if missing
if ! command -v claude &> /dev/null; then
    npm install -g @anthropic-ai/claude-code@latest
fi

mkdir -p /root/.claude

if [ ! -f /root/.claude/mcp_servers.json ] || ! grep -q "puppeteer" /root/.claude/mcp_servers.json 2>/dev/null; then
    echo "Configuring Puppeteer MCP server..."
    claude mcp add puppeteer -s user -- npx -y @modelcontextprotocol/server-puppeteer
fi

exec claude "$@"
