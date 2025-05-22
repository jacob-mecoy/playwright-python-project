import pytest

from pages.DuckDuckGo.search import DuckDuckGoSearchPage
from pages.DuckDuckGo.results import DuckDuckGoResultsPage
from playwright.sync_api import Page

@pytest.fixture
def results_page(page: Page) -> DuckDuckGoResultsPage:
    return DuckDuckGoResultsPage(page)

@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)