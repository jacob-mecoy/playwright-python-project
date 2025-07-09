from pytest_bdd import given, then, when

from playwright.sync_api import Page, expect

from pages.AutomationExercise.cart import AutomationExerciseCart
from pages.AutomationExercise.checkout import AutomationExerciseCheckout
from pages.AutomationExercise.homepage import AutomationExerciseHomepage
from pages.AutomationExercise.payment import AutomationExercisePayment


@given("I add a product to my basket")
def add_product_to_basket(page: Page, ae_homepage: AutomationExerciseHomepage) -> None:
    ae_homepage.add_to_cart_first_product.click()
    page.get_by_role("button", name="Continue Shopping").click()

@when("I place the order")
def place_order(ae_cart_page: AutomationExerciseCart, ae_checkout_page: AutomationExerciseCheckout) -> None:
    ae_cart_page.check_out.click()
    ae_checkout_page.place_order.click()
    
@then("I am taken to the Payment Screen")
def verify_we_are_on_payment_screen(page: Page, ae_payment_page: AutomationExercisePayment) -> None:
    expect(ae_payment_page.payment_header).to_be_visible()
    assert page.url == ae_payment_page.URL

@when("I input card details and confirm the order")
def input_card_details_and_confirm_order(ae_payment_page: AutomationExercisePayment) -> None:
    ae_payment_page.card_name.fill("FirstName LastName")
    ae_payment_page.card_number.fill("1111 1111 1111 1111")
    ae_payment_page.card_cvc.fill("111")
    ae_payment_page.card_expiry_month.fill("01")
    ae_payment_page.card_expiry_year.fill("2000")
    ae_payment_page.submit.click()

@then("the order has been placed")
def verify_order_is_placed(ae_payment_page: AutomationExercisePayment) -> None:
    expect(ae_payment_page.order_placed).to_be_visible()

@then("I can download an invoice")
def verify_invoice_can_be_downloaded(ae_payment_page: AutomationExercisePayment) -> None:
    dl_info = ae_payment_page.download_invoice()
    assert dl_info.value.suggested_filename == "invoice.txt"