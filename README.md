# unicode

A small, typical Python project for exploring Unicode text and code points.

## Setup

Create or activate a virtual environment, then install the project in editable mode:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e . pytest
```

## Usage

```powershell
unicode "Hello, 世界"
```

You can also call the module directly:

```powershell
python -m unicode.cli "é"
```

## Tests

```powershell
pytest
```
