import pytest

from pages.AutomationExercise.account_confirmation import AutomationExerciseAccountConfirmation
from pages.AutomationExercise.homepage import AutomationExerciseHomepage
from pages.AutomationExercise.login import AutomationExerciseLogin
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