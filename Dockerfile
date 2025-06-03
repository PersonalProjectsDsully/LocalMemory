FROM node:18

# Set environment variables to prevent prompts during install
ENV DEBIAN_FRONTEND=noninteractive \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable

# Install required tools and dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libxss1 \
    libnss3 \
    libxshmfence1 \
    libu2f-udev \
    libvulkan1 \
    x11-utils \
    xvfb \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install Google Chrome (modern key installation)
RUN mkdir -p /etc/apt/keyrings && \
    wget -q -O /etc/apt/keyrings/google-linux-signing-key.gpg https://dl.google.com/linux/linux_signing_key.pub && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Create init script
RUN cat > /usr/local/bin/init-claude.sh << 'EOF'
#!/bin/bash
set -e

# Install Claude Code globally if missing
if ! command -v claude &> /dev/null; then
    npm install -g @anthropic-ai/claude-code@latest
fi

# Ensure Claude MCP config directory exists
mkdir -p /root/.claude

# Configure Puppeteer MCP server if not already set
if [ ! -f /root/.claude/mcp_servers.json ] || ! grep -q "puppeteer" /root/.claude/mcp_servers.json 2>/dev/null; then
    echo "Configuring Puppeteer MCP server..."
    claude mcp add puppeteer -s user -- npx -y @modelcontextprotocol/server-puppeteer
fi

# Run Claude with passed arguments
exec claude "$@"
EOF

# Make init script executable
RUN chmod +x /usr/local/bin/init-claude.sh

ENTRYPOINT ["/usr/local/bin/init-claude.sh"]
