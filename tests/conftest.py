import pytest

from pages.results import DuckDuckGoResultsPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import Page

@pytest.fixture
def results_page(page: Page) -> DuckDuckGoResultsPage:
    return DuckDuckGoResultsPage(page)

@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)