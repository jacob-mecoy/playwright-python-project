from typing import Iterator
import pytest

from pages.AutomationExercise.account_confirmation import AutomationExerciseAccountConfirmation
from pages.AutomationExercise.cart import AutomationExerciseCart
from pages.AutomationExercise.checkout import AutomationExerciseCheckout
from pages.AutomationExercise.homepage import AutomationExerciseHomepage
from pages.AutomationExercise.login import AutomationExerciseLogin
from pages.AutomationExercise.modal import AutomationExerciseModal
from pages.AutomationExercise.payment import AutomationExercisePayment
from pages.AutomationExercise.product_details import AutomationExerciseProductDetails
from pages.AutomationExercise.products import AutomationExerciseProducts
from pages.AutomationExercise.signup import AutomationExerciseSignup
from pages.RickAndMorty.homepage import RickAndMortyHomepage
from pages.RickAndMorty.documentation import RickAndMortyDocumentationPage
from pages.RickAndMorty.about import RickAndMortyAboutPage
from playwright.sync_api import Page

@pytest.fixture
def homepage_page(page: Page) -> RickAndMortyHomepage:
    return RickAndMortyHomepage(page)

@pytest.fixture
def documentation_page(page: Page) -> RickAndMortyDocumentationPage:
    return RickAndMortyDocumentationPage(page)

@pytest.fixture
def about_page(page: Page) -> RickAndMortyAboutPage:
    return RickAndMortyAboutPage(page)

@pytest.fixture
def ae_homepage(page: Page) -> AutomationExerciseHomepage:
    return AutomationExerciseHomepage(page)

@pytest.fixture
def ae_login_page(page: Page) -> AutomationExerciseLogin:
    return AutomationExerciseLogin(page)

@pytest.fixture
def ae_signup_page(page: Page) -> AutomationExerciseSignup:
    return AutomationExerciseSignup(page)

@pytest.fixture
def ae_account_confirm_page(page: Page) -> AutomationExerciseAccountConfirmation:
    return AutomationExerciseAccountConfirmation(page)

@pytest.fixture
def ae_cart_page(page: Page) -> AutomationExerciseCart:
    return AutomationExerciseCart(page)

@pytest.fixture
def ae_checkout_page(page: Page) -> AutomationExerciseCheckout:
    return AutomationExerciseCheckout(page)

@pytest.fixture
def ae_payment_page(page: Page) -> AutomationExercisePayment:
    return AutomationExercisePayment(page)

@pytest.fixture
def ae_modal(page: Page) -> AutomationExerciseModal:
    return AutomationExerciseModal(page)

@pytest.fixture
def ae_products_page(page: Page) -> AutomationExerciseProducts:
    return AutomationExerciseProducts(page)

@pytest.fixture
def ae_product_details_page(page: Page) -> AutomationExerciseProductDetails:
    return AutomationExerciseProductDetails(page)

def _scenario_setup() -> None:
    """Scenario setup."""
    ...

def _scenario_teardown(ae_cart_page: AutomationExerciseCart) -> None:
    """Scenario teardown. Removes items from the logged in user's cart."""
    ae_cart_page.go_to_page_via_url()
    ae_cart_page.clear_cart()
    
@pytest.fixture
def scenario_setup_teardown_fixture(ae_cart_page: AutomationExerciseCart) -> Iterator[None]:
    """Teardown after each scenario that includes a step that uses this fixture."""
    _scenario_setup()
    yield
    _scenario_teardown(ae_cart_page)