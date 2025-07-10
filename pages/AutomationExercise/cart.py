from playwright.sync_api import Page

class AutomationExerciseCart:

    URL = "https://www.automationexercise.com/view_cart"

    def __init__(self, page: Page):
        self.page = page
        self.check_out = page.locator(".check_out")
        # locators for inspecific products
        self.product_descriptions = page.locator(".cart_description").get_by_role("link")
        self.product_quantities = page.locator(".cart_quantity").get_by_role("button")
    
    def go_to_page_via_url(self):
        self.page.goto(self.URL)

    def clear_cart(self):
        for locator in self.page.locator(".cart_quantity_delete").all():
            locator.click()