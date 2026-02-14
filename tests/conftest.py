import logging
import os
from collections.abc import Iterator
from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import Browser, Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.automation_exercise.account_confirmation import AutomationExerciseAccountConfirmation
from pages.automation_exercise.cart import AutomationExerciseCart
from pages.automation_exercise.checkout import AutomationExerciseCheckout
from pages.automation_exercise.homepage import AutomationExerciseHomepage
from pages.automation_exercise.login import AutomationExerciseLogin
from pages.automation_exercise.modal import AutomationExerciseModal
from pages.automation_exercise.payment import AutomationExercisePayment
from pages.automation_exercise.product_details import AutomationExerciseProductDetails
from pages.automation_exercise.products import AutomationExerciseProducts
from pages.automation_exercise.signup import AutomationExerciseSignup
from pages.rick_and_morty.about import RickAndMortyAboutPage
from pages.rick_and_morty.documentation import RickAndMortyDocumentationPage
from pages.rick_and_morty.homepage import RickAndMortyHomepage

DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30000"))
TEST_RUN_TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
TEST_ARTIFACT_DIR = Path.cwd().joinpath(f"./test_artifacts/{TEST_RUN_TIMESTAMP}")

logger = logging.getLogger(__name__)
logger.debug("tests/conftest.py loaded")


@pytest.fixture
def homepage_page(page: Page) -> RickAndMortyHomepage:
    return RickAndMortyHomepage(page)


@pytest.fixture
def documentation_page(page: Page) -> RickAndMortyDocumentationPage:
    return RickAndMortyDocumentationPage(page)


@pytest.fixture
def about_page(page: Page) -> RickAndMortyAboutPage:
    return RickAndMortyAboutPage(page)


@pytest.fixture
def ae_homepage(page: Page) -> AutomationExerciseHomepage:
    return AutomationExerciseHomepage(page)


@pytest.fixture
def ae_login_page(page: Page) -> AutomationExerciseLogin:
    return AutomationExerciseLogin(page)


@pytest.fixture
def ae_signup_page(page: Page) -> AutomationExerciseSignup:
    return AutomationExerciseSignup(page)


@pytest.fixture
def ae_account_confirm_page(page: Page) -> AutomationExerciseAccountConfirmation:
    return AutomationExerciseAccountConfirmation(page)


@pytest.fixture
def ae_cart_page(page: Page) -> AutomationExerciseCart:
    return AutomationExerciseCart(page)


@pytest.fixture
def ae_checkout_page(page: Page) -> AutomationExerciseCheckout:
    return AutomationExerciseCheckout(page)


@pytest.fixture
def ae_payment_page(page: Page) -> AutomationExercisePayment:
    return AutomationExercisePayment(page)


@pytest.fixture
def ae_modal(page: Page) -> AutomationExerciseModal:
    return AutomationExerciseModal(page)


@pytest.fixture
def ae_products_page(page: Page) -> AutomationExerciseProducts:
    return AutomationExerciseProducts(page)


@pytest.fixture
def ae_product_details_page(page: Page) -> AutomationExerciseProductDetails:
    return AutomationExerciseProductDetails(page)


@pytest.fixture(autouse=True)
def page(browser: Browser) -> Iterator[Page]:
    """Page fixture defining default page configuration."""
    page = browser.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)
    yield page
    page.close()


def _scenario_setup() -> None:
    """Scenario setup."""
    ...


def _scenario_teardown(ae_cart_page: AutomationExerciseCart) -> None:
    """Scenario teardown. Removes items from the logged in user's cart."""
    ae_cart_page.go_to_page_via_url()
    ae_cart_page.clear_cart()


@pytest.fixture
def scenario_setup_teardown_fixture(ae_cart_page: AutomationExerciseCart) -> Iterator[None]:
    """Teardown after each scenario that includes a step that uses this fixture."""
    _scenario_setup()
    yield
    _scenario_teardown(ae_cart_page)


def pytest_bdd_step_error(request, scenario, step, step_func_args, exception):
    """Called when a step function failed to execute.

    Take screenshot and collect page content if the step function had a page argument or a page
    object (created with POM design) as an argument.
    """
    step_name = getattr(step, "_name", getattr(step, "name", "<unknown-step>"))
    scenario_name = getattr(scenario, "name", "<unknown-scenario>")
    logger.debug(
        "pytest_bdd_step_error called for scenario='%s', step='%s', exception=%r",
        scenario_name,
        step_name,
        exception,
    )
    logger.exception(exception)

    # Try to obtain the Playwright page object:
    # 1. Check if 'page' was passed directly as a step argument.
    # 2. Check if any step argument is a page object (POM) (i.e. it has a .page attribute).
    # 3. Fall back to retrieving 'page' from request fixtures (autouse fixtures, etc.).
    page_obj = None
    if isinstance(step_func_args, dict):
        # Direct page argument
        if "page" in step_func_args:
            page_obj = step_func_args["page"]
        # Search for POM-style classes that have a .page attribute
        else:
            for arg_name, arg_value in step_func_args.items():
                if hasattr(arg_value, "page") and isinstance(
                    getattr(arg_value, "page", None), Page
                ):
                    page_obj = arg_value.page
                    logger.debug(
                        "Extracted page from POM class argument '%s' for scenario=%s",
                        arg_name,
                        scenario_name,
                    )
                    break

    # Fall back to fixture if not found in step args - It can be useful to get this data even if
    # the step that failed doesn't have a page argument.
    if page_obj is None:
        try:
            page_obj = request.getfixturevalue("page")
        except Exception:
            logger.debug(f"No 'page' fixture available via request for scenario={scenario_name}")

    if page_obj is not None:
        # Collect test artifacts for failing scenario/step
        TEST_ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
        scenario_dir = TEST_ARTIFACT_DIR.joinpath(scenario_name)
        scenario_dir.mkdir(parents=True, exist_ok=True)
        screenshot_filepath = scenario_dir.joinpath(f"{step_name}.png")
        try:
            page_obj.screenshot(path=str(screenshot_filepath))
        except PlaywrightTimeoutError:
            logger.warning(f"TimeoutError: Failed to get screenshot for {step_name}")
        else:
            logger.info(f"Wrote screenshot to {screenshot_filepath}")
        html_filepath = scenario_dir.joinpath(f"{step_name}.html")
        try:
            page_content = page_obj.content()
        except PlaywrightTimeoutError:
            logger.warning(f"TimeoutError: Failed to collect page content for {step_name}")
        else:
            with open(html_filepath, "w", encoding="utf-8") as content_file:
                content_file.write(page_content)
            logger.info(f"Wrote page HTML to {html_filepath}")
    else:
        logger.debug(
            "No Playwright page available; skipping artifact collection for scenario=%s step=%s",
            scenario_name,
            step_name,
        )
