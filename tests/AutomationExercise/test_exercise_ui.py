from playwright.sync_api import Page, expect
import random
import string

def test_load_page(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    #Verify we are returned to the homepage
    assert page.title() == "Automation Exercise"

def test_register_user(page: Page) -> None:
    #generate random string with letters and digits using the 'random' and 'string' modules
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
    email_address = f"a+{random_string}@a.a"
    first_name = "FirstName"
    last_name = "LastName"
    full_name = first_name + " " + last_name
    
    page.goto("https://www.automationexercise.com/")
    # homepage actions
    page.get_by_role("button", name="Consent").click() #Chrome - consent to data use
    page.get_by_text("Signup / Login").click()
    # login page actions
    page.get_by_placeholder("Name").fill(full_name)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(email_address) #needs to be a unique email, so add some random string
    page.get_by_role("button", name="Signup").click()
    # signup page actions
    page.locator("#id_gender1").click()
    expect(page.locator("#name")).to_have_value(full_name)
    expect(page.locator("#email")).to_have_value(email_address)
    page.locator("#password").fill("password1")
    page.locator("#days").select_option("1")
    page.locator("#months").select_option("January")
    page.locator("#years").select_option("1990")
    page.locator("#newsletter").check()
    page.locator("#optin").check()
    ##address info
    page.locator("#first_name").fill(first_name)
    page.locator("#last_name").fill(last_name)
    page.locator("#company").fill("CompanyName")

    page.locator("#address1").fill("221B Baker Street")
    page.locator("#country").select_option("United States")
    page.locator("#state").fill("Florida")
    page.locator("#city").fill("London")
    page.locator("#zipcode").fill("NW1 6XE")
    page.locator("#mobile_number").fill("11111111111")

    page.get_by_text("Create Account").click()

    #Account Created page
    expect(page.get_by_text("Account Created")).to_be_visible()
    page.get_by_text("Continue").click()
    # homepage actions
    #Verify we are returned to the homepage
    assert page.title() == "Automation Exercise"