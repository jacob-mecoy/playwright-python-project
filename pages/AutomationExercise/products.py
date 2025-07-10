from playwright.sync_api import Page

class AutomationExerciseProducts:

    URL = "https://www.automationexercise.com/products"

    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.locator("#search_product")
        self.confirm_search = page.locator("#submit_search")
        # locators for inspecific products
        self.product_items = page.locator(".single-products")
        self.view_product_links = page.get_by_text("View Product")