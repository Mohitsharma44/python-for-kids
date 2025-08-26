FROM kasmweb/core-ubuntu-focal:1.16.1-rolling-daily
USER root

# Kasm core image conventions (do not change these)
ENV HOME /home/kasm-default-profile
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

######### Customize Container Here ###########

# System deps: Python, Thonny, SDL/OpenGL for pygame
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 python3-pip \
    thonny python3-tk \
    git curl \
    libgl1 libglu1-mesa \
    libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0 \
    fonts-dejavu fonts-dejavu-extra && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

# Desktop launcher for Thonny (simple)
RUN printf '#!/bin/bash\nexec thonny\n' \
      > /usr/local/bin/launch_thonny && \
    chmod +x /usr/local/bin/launch_thonny && \
    mkdir -p "$HOME/Desktop" && \
    printf '[Desktop Entry]\nType=Application\nName=Thonny (Python IDE)\nComment=Launch Thonny IDE\nExec=/usr/local/bin/launch_thonny\nIcon=thonny\nTerminal=false\nCategories=Development;Education;\nStartupNotify=true\n' \
      > "$HOME/Desktop/thonny.desktop" && \
    chmod +x "$HOME/Desktop/thonny.desktop"


######### End Customizations ###########

# Kasm-required permissions fixup (copies default profile on first run)
RUN chown 1000:0 $HOME && $STARTUPDIR/set_user_permission.sh $HOME

# Switch HOME to the runtime user (don't write here during build)
ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000