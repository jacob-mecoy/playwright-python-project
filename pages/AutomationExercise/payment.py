from playwright.sync_api import Page

class AutomationExercisePayment:

    URL = "https://www.automationexercise.com/payment"

    def __init__(self, page: Page):
        self.page = page
        self.payment_header = page.get_by_role("heading", name="Payment")
        self.card_name = page.locator("input[name='name_on_card']")
        self.card_number = page.locator("input[name='card_number']")
        self.card_cvc = page.locator("input[name='cvc']")
        self.card_expiry_month = page.locator("input[name='expiry_month']")
        self.card_expiry_year = page.locator("input[name='expiry_year']")
        self.submit = page.locator("#submit")
        self.order_placed = page.get_by_role("heading", name="Order Placed!")

    def download_invoice(self):
        with self.page.expect_download() as dl_info:
            self.page.get_by_role("link", name="Download Invoice").click()
        return dl_info