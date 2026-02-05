## What is this project?

A test automation web UI & API project using python, playwright & pytest. These tests currently interact with 2 websites - https://rickandmortyapi.com/ & https://www.automationexercise.com/. It implements the "page object model" practice for code structure. It implements BDD (using `pytest-bdd`).

## Project setup

All the commands below are for Windows:

- Your machine must have Python installed, ideally the latest version. Download the latest version of Python from Python.org.
- Install Poetry by running in PowerShell (as admin):
  ```powershell
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  ```
- Clone the project to your local device e.g. via SSH you can run: 
  ```bash
  git clone git@github.com:jacob-mecoy/playwright-python-project.git
  ```
- Move into the project directory:
  ```bash
  cd playwright-python-project
  ```
- Install dependencies:
  ```bash
  poetry install
  ```
- Activate Poetry shell (virtual environment):
  ```bash
  poetry env activate
  ```
- Install Playwright browsers:
  ```bash
  poetry run playwright install
  ```
- You may need to install Visual C++ Build Tools (for installing the greenlet dependency)
  Download "Build Tools for Visual Studio" from: https://visualstudio.microsoft.com/visual-cpp-build-tools/.
  Run installer, check "C++ build tools" (include MSVC and Windows SDK), install.
- Some of the tests rely on importing environment variables. Therefore you will need to create a `.env` file in the project root with the required key:value pairs

## Dependency Management

### Installing Dependencies
```powershell
# Install dependencies from lock file (recommended)
poetry install
```

### Updating Dependencies
```powershell
# Update specific package to latest version allowed in pyproject.toml
poetry update package-name

# Update all packages (use with caution)
poetry update
```

### Checking Dependencies
```powershell
# Show currently installed versions
poetry show

# Show outdated packages
poetry show --outdated
```

**Note**: Use `poetry install` for day-to-day development to ensure consistent dependencies. Only use `poetry update` when you intentionally want to upgrade packages to newer versions.

## Running the tests

To run the tests, run through the "project setup" section and follow the below:

```bash
# Run all tests
poetry run pytest tests

# Run specific test file
poetry run pytest tests/<file_name>

# Run UI tests in headed mode
poetry run pytest tests --headed

# Run tests with slower execution
poetry run pytest tests --headed --slowmo 1000
```

### About the tests

- All the tests are within the `tests` folder.
  - Each `test_...` file imports scenarios from feature files using the `scenarios(...)` line it contains. View this line to understand which scenarios a `test_...` file "contains".
  - `tests` contains one file for ui tests and one file for api tests.
- UI tests - By default, pytest runs the tests in headless mode.

## Linting and formatting

Currently using ruff as both a linter and formatter. See https://docs.astral.sh/ruff/ for more information. We have a `pyproject.toml` file in the project root that contains some configuration for ruff.

```bash
# Run the linter
poetry run ruff check

# Run the formatter
poetry run ruff format
```