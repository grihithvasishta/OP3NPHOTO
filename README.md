# OpenPhoto

OpenPhoto is a free, open-source alternative to Photoshop built with Python and PyQt6.

## Features
- Modern dark theme UI inspired by industry standards
- Core tools (Move, Marquee, Lasso, Magic Wand, Crop, Brush, Eraser)
- Native Windows Desktop application feel

## Installation

You can install OpenPhoto directly via pip:

```bash
pip install openphoto
```

Once installed, simply run `openphoto` in your terminal to launch the app!

## Testing

To run the automated test suite, you need to install the testing dependencies:

```bash
pip install pytest pytest-qt
pytest
```

## Publishing to PyPI

When you are ready to publish OpenPhoto to the world, follow these steps:

1. Install the build tools:
   ```bash
   pip install build twine
   ```
2. Build the distribution packages:
   ```bash
   python -m build
   ```
3. Upload to PyPI (you will need a PyPI account):
   ```bash
   twine upload dist/*
   ```
