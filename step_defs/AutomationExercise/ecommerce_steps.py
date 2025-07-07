from pytest_bdd import given, then, when

from playwright.sync_api import Page, expect


@given("I add a product to my basket")
def add_product_to_basket(page: Page) -> None:
    page.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()

@when("I place the order")
def place_order(page: Page) -> None:
    page.locator(".check_out").click()
    page.get_by_role("link", name="Place Order").first.click()
    
@then("I am taken to the Payment Screen")
def verify_we_are_on_payment_screen(page: Page) -> None:
    expect(page.locator(".breadcrumb").get_by_role("list", name="Checkout"))
    assert page.url == "https://www.automationexercise.com/payment"

@when("I input card details and confirm the order")
def input_card_details_and_confirm_order(page: Page) -> None:
    page.locator("input[name='name_on_card']").fill("FirstName LastName")
    page.locator("input[name='card_number']").fill("1111 1111 1111 1111")
    page.locator("input[name='cvc']").fill("111")
    page.locator("input[name='expiry_month']").fill("01")
    page.locator("input[name='expiry_year']").fill("2000")
    page.click("#submit")

@then("the order has been placed")
def verify_order_is_placed(page: Page) -> None:
    page.get_by_role("heading", name="Order Placed!")

@then("I can download an invoice")
def verify_invoice_can_be_downloaded(page: Page) -> None:
    with page.expect_download() as dl_info:
        page.get_by_role("link", name="Download Invoice").click()
    assert dl_info.value.suggested_filename == "invoice.txt"