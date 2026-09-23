# Software Construction Lab

This repository contains laboratory exercises and assignments for the **Software Construction & Development** course.

## Project Structure

```text
software-construction-lab/
├── .venv/               # Virtual environment (ignored by Git)
├── src/                 # Application source code
│   └── hello.py         # Sample greeting module
├── tests/               # Automated test suites
│   └── test_hello.py    # Unit tests for hello module
├── .gitignore           # Git ignore patterns
├── pyproject.toml       # Pytest and tool configurations
├── README.md            # Project documentation
└── requirements.txt     # Locked project dependencies
```

## Setup & Environment

1. **Activate Virtual Environment**:
   - Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     source .venv/bin/activate
     ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set PYTHONPATH** (Windows PowerShell):
   ```powershell
   $env:PYTHONPATH = "."
   ```

## Running Quality Tools

- **Run Automated Tests**:
  ```bash
  pytest
  ```

- **Run Code Linter and Formatter Check**:
  ```bash
  ruff check .
  ```

- **Run Static Type Checker**:
  ```bash
  mypy src/
  ```
