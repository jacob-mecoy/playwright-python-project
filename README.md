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

To run the tests, run through the "project setup" section above and then run through the bullet points here.

- All the tests are within the `tests` folder, to run all of them run `poetry run pytest tests`. Alternatively to run a subset of the tests you can easily run tests contained within one of the `test_...` files with `poetry run pytest tests/<file_name>`
  - Each `test_...` file imports scenarios from feature files using the `scenarios(...)` line it contains. View this line to understand which scenarios a `test_...` file "contains".
  - `tests` contains one file for ui tests and one file for api tests
- UI tests - By default, pytest runs the tests in headless mode, to run them in headed mode (and so to actually see the tests run in browser) run `poetry run pytest tests --headed`
  - If you want to see the tests run slower to more easily see what they're doing then add the `--slowmo` argument to pause execution for 1 second (1000 ms) after each Playwright call. E.g. `poetry run pytest tests --headed --slowmo 1000`

## Linting and formatting

Currently using ruff as both a linter and formatter. See https://docs.astral.sh/ruff/ for more information. We have a `pyproject.toml` file in the project root that contains some configuration for ruff.

- Run the linter within cmd using the command `poetry run ruff check`
- Run the formatter within cmd using the command `poetry run ruff format`