# Python Learning Basics

This project contains basic Python learning exercises organized with Poetry for dependency management.

## Setup

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Running the Code

To run the string exercises:
```bash
poetry run python src/strings.py
```

## Functions

### `reverse_string(text)`
Reverses a string using Python's slice notation.

**Parameters:**
- `text` (str): The string to reverse

**Returns:**
- `str`: The reversed string

**Example:**
```python
from src.strings import reverse_string

result = reverse_string("Hello Python!")
print(result)  # Output: !nohtyP olleH
```

## Testing

Run all tests:
```bash
poetry run pytest
```

Run tests with verbose output:
```bash
poetry run pytest -v
```

Run specific test file:
```bash
poetry run pytest tests/test_strings.py -v
```

## Project Structure

```
├── src/
│   ├── __init__.py
│   └── strings.py          # String manipulation exercises and functions
├── tests/
│   ├── __init__.py
│   └── test_strings.py     # Test cases for string functions
├── pyproject.toml          # Poetry configuration and dependencies
└── README.md              # This file
```

## Development

This project includes development dependencies for code quality:
- `pytest` for testing
- `black` for code formatting
- `flake8` for linting

To format code:
```bash
poetry run black src/ tests/
```

To lint code:
```bash
poetry run flake8 src/ tests/
```
