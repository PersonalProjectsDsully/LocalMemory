FROM node:18

# Set environment variables to avoid prompts during install and configure Puppeteer
ENV DEBIAN_FRONTEND=noninteractive
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable

# Install required OS packages and Puppeteer dependencies
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
    xvfb \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Add the Google Chrome repository and install Chrome (updated method)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Copy the Claude init script into the image
COPY init-claude.sh /usr/local/bin/init-claude.sh
RUN chmod +x /usr/local/bin/init-claude.sh

# Set the default entrypoint
ENTRYPOINT ["/usr/local/bin/init-claude.sh"]