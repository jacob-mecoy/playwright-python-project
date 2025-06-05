from playwright.sync_api import Page

class AutomationExerciseLogin:

    def __init__(self, page: Page):
        self.page = page
        self.signup_name = page.get_by_placeholder("Name")
        self.signup_email = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.signup_button = page.get_by_role("button", name="Signup")
        self.login_email = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.login_password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
    
    def enter_signup_info(self, first_name: str, last_name: str, email_address: str):
        full_name = first_name + " " + last_name
        self.signup_name.fill(full_name)
        self.signup_email.fill(email_address)

    def enter_login_info(self, email_address: str, password: str):
        self.login_email.fill(email_address)
        self.login_password.fill(password)