from playwright.sync_api import Page, expect
import random
import string

from pages.AutomationExercise.account_confirmation import AutomationExerciseAccountConfirmation
from pages.AutomationExercise.homepage import AutomationExerciseHomepage
from pages.AutomationExercise.login import AutomationExerciseLogin
from pages.AutomationExercise.signup import AutomationExerciseSignup

def test_load_page(ae_homepage: AutomationExerciseHomepage) -> None:
    ae_homepage.load()
    #Verify we are returned to the homepage
    assert ae_homepage.page.title() == "Automation Exercise"

def test_register_user(ae_homepage: AutomationExerciseHomepage, ae_login_page: AutomationExerciseLogin, ae_signup_page: AutomationExerciseSignup, ae_account_confirm_page: AutomationExerciseAccountConfirmation) -> None:
    #generate random string with letters and digits using the 'random' and 'string' modules
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
    email_address = f"a+{random_string}@a.a"
    first_name = "FirstName"
    last_name = "LastName"
    full_name = first_name + " " + last_name
    
    ae_homepage.load()
    ae_homepage.consent.click() #Chrome - consent to data use
    ae_homepage.signup.click()

    ae_login_page.enter_signup_info(first_name, last_name, email_address)
    ae_login_page.signup.click()

    expect(ae_signup_page.name).to_have_value(full_name)
    expect(ae_signup_page.email).to_have_value(email_address)
    ae_signup_page.enter_basic_signup_info()
    ae_signup_page.enter_address_signup_info(first_name, last_name)
    ae_signup_page.create_account.click()

    expect(ae_account_confirm_page.creation_message).to_be_visible()
    ae_account_confirm_page.continue_button.click()
    #Verify we are returned to the homepage
    assert ae_homepage.page.title() == "Automation Exercise"