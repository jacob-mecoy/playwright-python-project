from playwright.sync_api import Page

class AutomationExerciseProductDetails:

    def __init__(self, page: Page):
        self.page = page
        self.quantity_dropdown = page.locator("#quantity")
        self.add_to_cart = page.get_by_role("button", name="Add to cart")