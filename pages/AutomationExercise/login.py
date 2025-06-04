from playwright.sync_api import Page

class AutomationExerciseLogin:

    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_placeholder("Name")
        self.email = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.signup = page.get_by_role("button", name="Signup")
    
    def enter_signup_info(self, first_name: str, last_name: str, email_address: str):
        full_name = first_name + " " + last_name
        self.name.fill(full_name)
        self.email.fill(email_address)