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

3. Working with the virtual environment:
   
   You have two options:

   a. Run commands directly with poetry:
   ```bash
   poetry run python your_script.py
   ```

   b. If you need an interactive shell, use:
   ```bash
   poetry shell
   ```

   c. Alternative method to activate the virtual environment:
   ```bash
   source $(poetry env info --path)/bin/activate
   ```
   This command directly activates Poetry's virtual environment using its path.
   
4. Deactivating the virtual environment:
   
   If you used `poetry shell`:
   ```bash
   exit
   ```
   
   If you used the direct activation method:
   ```bash
   deactivate
   ```

## Running the Code

To run the string exercises:
```bash
poetry run python src/strings.py
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

