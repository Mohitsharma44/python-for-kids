# Python for Kids

Learn programming by building small games using Pygame Zero (pgzero).

[![CI](https://github.com/mohitsharma44/python-for-kids/actions/workflows/ci.yml/badge.svg)](https://github.com/mohitsharma44/python-for-kids/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## What you'll find

- Week-by-week exercises (start with `week01/`)
- A complete starter game: `week01/gold_collector_game.py`
- Simple assets (images/sounds) ready to use
- A Docker/Kasm desktop for easy, remote access with Thonny

## Quick start (local)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python week01/gold_collector_game.py
```

## Quick start (Kasm desktop)

- Build the image: `docker build -t python-for-kids .`
- Run a Kasm container (per your lab setup) and open the desktop
- Click "Start Here (Thonny)": it opens `Desktop/Projects`
- Open this repo folder from Thonny and run `week01/gold_collector_game.py`

## A tiny pgzero example

```python
# save as hello_pgzero.py and run: pgzrun hello_pgzero.py
WIDTH = 400
HEIGHT = 300

def draw():
    screen.clear()
    screen.draw.text("Hello, Pygame Zero!", center=(WIDTH/2, HEIGHT/2), fontsize=36)
```

## Development

```bash
pip install -r requirements-dev.txt
black . && isort . && flake8
```

Enable pre-commit (optional):
```bash
pre-commit install
pre-commit run --all-files
```

## Troubleshooting

- Thonny fails to start on Ubuntu: install `python3-tk`
- No audio in browser-based desktop: check Kasm audio settings; visuals still work
- Missing SDL libraries: ensure the container has SDL2 packages installed

## Contributing

See `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.

## License

MIT
