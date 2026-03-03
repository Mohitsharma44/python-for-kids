FROM kasmweb/core-ubuntu-jammy:1.17.0
USER root

# Kasm core image conventions (do not change these)
ENV HOME /home/kasm-default-profile
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

######### Customize Container Here ###########

# System deps: Python, SDL/OpenGL for pygame
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 python3-pip python3-tk \
    git curl wget \
    libgl1 libglu1-mesa \
    libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0 \
    fonts-dejavu fonts-dejavu-extra && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

# --- VS Code ---
# Install VS Code .deb (same approach as Kasm's official kasmweb/vs-code image)
RUN ARCH=$(arch | sed 's/aarch64/arm64/g' | sed 's/x86_64/x64/g') && \
    wget -q "https://update.code.visualstudio.com/latest/linux-deb-${ARCH}/stable" \
         -O /tmp/vs_code.deb && \
    apt-get update && \
    apt-get install -y /tmp/vs_code.deb && \
    rm /tmp/vs_code.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Patch launcher: --no-sandbox is required for Electron apps inside Docker
RUN sed -i 's|/usr/share/code/code|/usr/share/code/code --no-sandbox|g' \
        /usr/share/applications/code.desktop && \
    mkdir -p "$HOME/Desktop" && \
    cp /usr/share/applications/code.desktop "$HOME/Desktop/vscode.desktop" && \
    chmod +x "$HOME/Desktop/vscode.desktop"

# Pre-configure VS Code with beginner-friendly settings
# The Python extension installs on first use via .vscode/extensions.json in the repo
RUN mkdir -p "$HOME/.config/Code/User"
COPY vscode-settings.json $HOME/.config/Code/User/settings.json
RUN chown -R 1000:0 "$HOME/.config/Code"


######### End Customizations ###########

# Kasm-required permissions fixup (copies default profile on first run)
RUN chown 1000:0 $HOME && $STARTUPDIR/set_user_permission.sh $HOME

# Switch HOME to the runtime user (don't write here during build)
ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000
