#!/usr/bin/env bash
# Syncs IDE config from the Docker image defaults to the user profile.
# Runs on every login via Xfce autostart so persistent profiles stay current.
set -e

DEFAULT_PROFILE=/home/kasm-default-profile

# Desktop shortcuts: remove legacy Thonny, ensure VS Code
rm -f "$HOME/Desktop/start-here.desktop" "$HOME/Desktop/thonny.desktop"
cp -f "$DEFAULT_PROFILE/Desktop/vscode.desktop" "$HOME/Desktop/vscode.desktop" 2>/dev/null || true
chmod +x "$HOME/Desktop/vscode.desktop" 2>/dev/null || true

# Default file associations (open .py/.txt/etc in VS Code)
mkdir -p "$HOME/.config"
cp -f "$DEFAULT_PROFILE/.config/mimeapps.list" "$HOME/.config/mimeapps.list" 2>/dev/null || true

# VS Code settings
mkdir -p "$HOME/.config/Code/User"
cp -f "$DEFAULT_PROFILE/.config/Code/User/settings.json" "$HOME/.config/Code/User/settings.json" 2>/dev/null || true

# VS Code local .desktop (for mime handler)
mkdir -p "$HOME/.local/share/applications"
cp -f "$DEFAULT_PROFILE/.local/share/applications/code.desktop" \
      "$HOME/.local/share/applications/code.desktop" 2>/dev/null || true

# VS Code extensions: copy any missing extensions from image defaults
if [ -d "$DEFAULT_PROFILE/.vscode/extensions" ]; then
    mkdir -p "$HOME/.vscode/extensions"
    for ext in "$DEFAULT_PROFILE/.vscode/extensions"/ms-python.*; do
        name=$(basename "$ext")
        if [ ! -d "$HOME/.vscode/extensions/$name" ]; then
            cp -r "$ext" "$HOME/.vscode/extensions/$name"
        fi
    done
fi
