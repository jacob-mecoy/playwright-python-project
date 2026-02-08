import os
import random
import string

from dotenv import load_dotenv
from playwright.sync_api import expect
from pytest_bdd import given, then, when

from pages.automation_exercise.account_confirmation import AutomationExerciseAccountConfirmation
from pages.automation_exercise.homepage import AutomationExerciseHomepage
from pages.automation_exercise.login import AutomationExerciseLogin
from pages.automation_exercise.signup import AutomationExerciseSignup

first_name = "FirstName"
last_name = "LastName"


@given("I enter initial signup info")
def enter_initial_signup_info(
    ae_login_page: AutomationExerciseLogin, ae_signup_page: AutomationExerciseSignup
):
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    email_address = f"a+{random_string}@a.a"
    full_name = first_name + " " + last_name
    ae_login_page.enter_signup_info(first_name, last_name, email_address)
    ae_login_page.signup_button.click()
    expect(ae_signup_page.name).to_have_value(full_name)
    expect(ae_signup_page.email).to_have_value(email_address)


@given("I enter the remaining signup information")
def enter_remaining_signup_info(ae_signup_page: AutomationExerciseSignup):
    ae_signup_page.enter_basic_signup_info()
    ae_signup_page.enter_address_signup_info(first_name, last_name)


@when("I create the user account")
def create_new_user_account(ae_signup_page: AutomationExerciseSignup):
    ae_signup_page.create_account.click()


@given("I sign in")
@when("I sign in")
def sign_in(ae_login_page: AutomationExerciseLogin):
    load_dotenv()
    ae_login_page.enter_login_info(os.getenv("USER_EMAIL"), os.getenv("USER_PASSWORD"))
    ae_login_page.login_button.click()


@then("I expect a confirmation message to be displayed")
def expect_confirmation_message(ae_account_confirm_page: AutomationExerciseAccountConfirmation):
    expect(ae_account_confirm_page.creation_message).to_be_visible()


@when("I choose to continue")
def choose_to_continue(ae_account_confirm_page: AutomationExerciseAccountConfirmation):
    ae_account_confirm_page.continue_button.click()


@then("the homepage shows I am logged in")
def expect_homepage_shows_logged_in(ae_homepage: AutomationExerciseHomepage):
    load_dotenv()
    expect(ae_homepage.logged_in_message).to_have_text(
        f"Logged in as {os.getenv('USER_FIRST_NAME')}"
    )
