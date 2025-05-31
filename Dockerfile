FROM node:18

# Install git and other tools that Claude Code might need
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Create a script that installs and runs Claude Code with arguments
RUN echo '#!/bin/sh\nnpm install -g @anthropic-ai/claude-code@latest\nclaude "$@"' > /usr/local/bin/run-claude.sh && \
    chmod +x /usr/local/bin/run-claude.sh

ENTRYPOINT ["/usr/local/bin/run-claude.sh"]