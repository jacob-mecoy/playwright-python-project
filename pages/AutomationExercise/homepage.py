from playwright.sync_api import Page

class AutomationExerciseHomepage:

    URL = "https://www.automationexercise.com/"

    def __init__(self, page: Page):
        self.page = page
        self.consent = page.get_by_role("button", name="Consent")
        self.logged_in_message = page.locator("a").filter(has_text="Logged in as")
        self.add_to_cart_first_product = page.locator(".add-to-cart").first
        # navigation bar elements
        self.signup_login_link = page.get_by_text("Signup / Login")
        self.cart_link = page.get_by_role("link", name="Cart")
        self.product_link = page.get_by_role("link", name="Products")
    
    def load(self):
        self.page.goto(self.URL)