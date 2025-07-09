from playwright.sync_api import Page

class AutomationExerciseCart:

    URL = "https://www.automationexercise.com/view_cart"

    def __init__(self, page: Page):
        self.page = page
        self.check_out = page.locator(".check_out")
    