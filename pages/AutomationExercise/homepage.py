from playwright.sync_api import Page

class AutomationExerciseHomepage:

    URL = "https://www.automationexercise.com/"

    def __init__(self, page: Page):
        self.page = page
        self.consent = page.get_by_role("button", name="Consent")
        self.signup_login_link = page.get_by_text("Signup / Login")
        self.logged_in_message = page.locator("a").filter(has_text="Logged in as")
        self.add_to_cart_first_product = page.locator(".add-to-cart").first
    
    def load(self):
        self.page.goto(self.URL)