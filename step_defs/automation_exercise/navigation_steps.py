import contextlib

from pytest_bdd import given, then, when

from pages.automation_exercise.homepage import AutomationExerciseHomepage
from pages.automation_exercise.modal import AutomationExerciseModal


@given("I navigate to the homepage")
def navigate_to_homepage(ae_homepage: AutomationExerciseHomepage):
    ae_homepage.load()
    # Consent button may not always be present; wait short timeout and ignore if not found
    with contextlib.suppress(TimeoutError):
        ae_homepage.consent.click(timeout=5000)  # short timeout to avoid long waits


@given("I navigate to the signup login page")
def navigate_to_signup_login(ae_homepage: AutomationExerciseHomepage):
    ae_homepage.signup_login_link.click()


@then("the homepage loads successfully")
@then("I am returned to the homepage")
def verify_we_are_on_the_homepage(ae_homepage: AutomationExerciseHomepage):
    assert ae_homepage.page.title() == "Automation Exercise"


@given("I navigate to the cart")
def navigate_to_cart(ae_homepage: AutomationExerciseHomepage) -> None:
    ae_homepage.cart_link.click()


@given("I navigate to the products page")
def navigate_to_products(ae_homepage: AutomationExerciseHomepage) -> None:
    ae_homepage.product_link.click()


@when("I navigate to the cart via the modal")
def navigate_to_cart_via_modal(ae_modal: AutomationExerciseModal) -> None:
    ae_modal.view_cart.click()
