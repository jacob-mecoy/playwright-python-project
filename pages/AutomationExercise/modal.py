from playwright.sync_api import Page

class AutomationExerciseModal:

    def __init__(self, page: Page):
        self.page = page
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")
        self.view_cart = page.locator(".modal-dialog").get_by_role("link", name="View Cart")
