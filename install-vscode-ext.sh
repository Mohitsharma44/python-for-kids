#!/usr/bin/env bash
# Usage: install-vscode-ext.sh <publisher> <extension>
# Downloads a VS Code extension from the marketplace and extracts it.
set -e
PUBLISHER="$1"
EXTENSION="$2"
EXT_DIR="$HOME/.vscode/extensions"
WORK="/tmp/vscode-ext-${PUBLISHER}-${EXTENSION}"

mkdir -p "$EXT_DIR" "$WORK"
wget -q --max-redirect=5 \
     "https://${PUBLISHER}.gallery.vsassets.io/_apis/public/gallery/publisher/${PUBLISHER}/extension/${EXTENSION}/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage" \
     -O "$WORK/ext.vsix"
cd "$WORK"
unzip -q ext.vsix -d extracted
VER=$(python3 -c "import json; print(json.load(open('extracted/extension/package.json'))['version'])")
mv "extracted/extension" "$EXT_DIR/${PUBLISHER}.${EXTENSION}-${VER}"
rm -rf "$WORK"
echo "Installed ${PUBLISHER}.${EXTENSION} v${VER}"
