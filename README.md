## What is this project?

A test automation web UI & API project using python, playwright & pytest. These tests currently interact with 3 websites - https://rickandmortyapi.com/, https://www.automationexercise.com/ & https://duckduckgo.com. It implements the "page object model" practice for code structure. 

## Project setup

All the commands below are written to be run within cmd.

- Your machine must have Python installed, ideally the latest version. Download the latest version of Python from Python.org.
- Clone the project to your local device e.g. via SSH you can run `git clone git@github.com:jacob-mecoy/playwright-python-project.git` 
- Move into the project directory - `cd playwright-python-project`
- Create a virtual environment to manage the dependency packages locally - `py -m venv venv`
- activate the virtual environment with `venv\Scripts\activate.bat`
- Add required packages to your venv by running `pip install -r requirements.txt`
- To download the browsers that Playwright can run tests with, run `playwright install`

## Running the tests

To run the tests, run through the "project setup" section above and then run through the bullet points here.

- All the tests are within the tests folder, to run all of them run `py -m pytest tests`. Alternatively to run the tests within one of the subfolders just run `py -m pytest tests\<subfolder_name>`
- UI tests - By default, pytest runs the tests in headless mode, to run them in headed mode (and so to actually see the tests run in browser) run `python3 -m pytest tests --headed`
  - If you want to see the tests run slower to more easily see what they're doing then add the `--slowmo` argument to pause execution for 1 second (1000 ms) after each Playwright call. E.g. `python3 -m pytest tests --headed --slowmo 1000`
- `tests\RickAndMorty` contains one file for ui tests and one file for api tests