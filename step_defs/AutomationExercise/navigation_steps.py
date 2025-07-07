from pytest_bdd import given, then

from playwright.sync_api import Page

from pages.AutomationExercise.homepage import AutomationExerciseHomepage

@given("I navigate to the homepage")
def navigate_to_homepage(ae_homepage: AutomationExerciseHomepage):
    ae_homepage.load()
    ae_homepage.consent.click()

@given("I navigate to the signup login page")
def navigate_to_signup_login(ae_homepage: AutomationExerciseHomepage):
    ae_homepage.signup_login_link.click()

@given("I navigate to the signup page")
def navigate_to_signup_login(ae_homepage: AutomationExerciseHomepage):
    ae_homepage.signup_login_link.click()

@then("the homepage loads successfully")
@then("I am returned to the homepage")
def verify_we_are_on_the_homepage(ae_homepage: AutomationExerciseHomepage):
    assert ae_homepage.page.title() == "Automation Exercise"

@given("I navigate to the cart")
def navigate_to_cart(page: Page) -> None:
    page.get_by_role("link", name="Cart").click()