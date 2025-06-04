from playwright.sync_api import Page

class AutomationExerciseSignup:

    def __init__(self, page: Page):
        self.page = page
        self.gender = page.locator("#id_gender1")
        self.name = page.locator("#name")
        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.dob_day = page.locator("#days")
        self.dob_month = page.locator("#months")
        self.dob_year = page.locator("#years")
        self.newsletter = page.locator("#newsletter")
        self.optin = page.locator("#optin")
        # address locators
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.company_name = page.locator("#company")
        self.address_one = page.locator("#address1")
        self.country = page.locator("#country")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile = page.locator("#mobile_number")
        self.create_account = page.get_by_text("Create Account")

    def enter_basic_signup_info(self):
        self.gender.click()
        self.password.fill("password1")
        self.dob_day.select_option("1")
        self.dob_month.select_option("January")
        self.dob_year.select_option("1990")
        self.newsletter.check()
        self.optin.check()

    def enter_address_signup_info(self, first_name: str, last_name: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company_name.fill("CompanyName")

        self.address_one.fill("221B Baker Street")
        self.country.select_option("United States")
        self.state.fill("Florida")
        self.city.fill("London")
        self.zipcode.fill("NW1 6XE")
        self.mobile.fill("11111111111")