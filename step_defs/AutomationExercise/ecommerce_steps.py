from typing import Iterator
from pytest_bdd import given, then, when, parsers

from playwright.sync_api import Page, expect

from pages.AutomationExercise.cart import AutomationExerciseCart
from pages.AutomationExercise.checkout import AutomationExerciseCheckout
from pages.AutomationExercise.homepage import AutomationExerciseHomepage
from pages.AutomationExercise.modal import AutomationExerciseModal
from pages.AutomationExercise.payment import AutomationExercisePayment


@given("I add a product to my basket")
def add_product_to_basket(ae_homepage: AutomationExerciseHomepage, ae_modal: AutomationExerciseModal, scenario_setup_teardown_fixture: Iterator[None]) -> None:
    ae_homepage.add_to_cart_first_product.click()
    ae_modal.continue_shopping.click()

@given(parsers.parse("I add {product_quantity} of the current product to my basket"))
def open_product_details_page(page: Page, product_quantity: int, scenario_setup_teardown_fixture: Iterator[None]) -> None:
    page.locator("#quantity").fill(str(product_quantity))
    page.get_by_role("button", name="Add to cart").click()
    #verify confirmation message shows
    expect(page.get_by_text("Your product has been added to cart.")).to_be_visible()

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
def verify_order_is_placed(ae_payment_page: AutomationExercisePayment, scenario_setup_teardown_fixture: Iterator[None]) -> None:
    expect(ae_payment_page.order_placed).to_be_visible()

@then("I can download an invoice")
def verify_invoice_can_be_downloaded(ae_payment_page: AutomationExercisePayment) -> None:
    dl_info = ae_payment_page.download_invoice()
    assert dl_info.value.suggested_filename == "invoice.txt"

@given(parsers.parse("I search for product '{product_name}'"))
def search_for_product(page: Page, product_name: str) -> None:
    page.locator("#search_product").fill(product_name)
    page.locator("#submit_search").click()
    # ToDo: alternatively we could create a data model for a product, which includes the id of the product 
    # and then use that id to identify that the correct product is displayed
    assert page.locator(".single-products").count() == 1

@given(parsers.parse("I open the product details page for the only available product"))
def open_product_details_page(page: Page) -> None:
    page.get_by_text("View Product").click()

@then(parsers.parse("there are {product_quantity} of '{product_name}' in my basket"))
def confirm_basket_contains_quantity_of_product(page: Page, product_quantity: int, product_name: str) -> None:
    expect(page.locator(".cart_description").get_by_role("link")).to_have_text(product_name)
    expect(page.locator(".cart_quantity").get_by_role("button")).to_have_text(str(product_quantity))