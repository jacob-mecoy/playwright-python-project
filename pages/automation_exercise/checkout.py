from playwright.sync_api import Page


class AutomationExerciseCheckout:
    URL = "https://www.automationexercise.com/checkout"

    def __init__(self, page: Page):
        self.page = page
        self.check_out = page.locator(".check_out")
        self.place_order = page.get_by_role("link", name="Place Order").first
