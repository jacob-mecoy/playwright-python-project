import pytest

from pages.DuckDuckGo.search import DuckDuckGoSearchPage
from pages.DuckDuckGo.results import DuckDuckGoResultsPage
from pages.RickAndMorty.homepage import RickAndMortyHomepage
from pages.RickAndMorty.documentation import RickAndMortyDocumentationPage
from pages.RickAndMorty.about import RickAndMortyAboutPage
from playwright.sync_api import Page

@pytest.fixture
def results_page(page: Page) -> DuckDuckGoResultsPage:
    return DuckDuckGoResultsPage(page)

@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)

@pytest.fixture
def homepage_page(page: Page) -> RickAndMortyHomepage:
    return RickAndMortyHomepage(page)

@pytest.fixture
def documentation_page(page: Page) -> RickAndMortyDocumentationPage:
    return RickAndMortyDocumentationPage(page)

@pytest.fixture
def about_page(page: Page) -> RickAndMortyAboutPage:
    return RickAndMortyAboutPage(page)