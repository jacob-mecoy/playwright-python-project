from playwright.sync_api import Page, expect
from pages.DuckDuckGo.search import DuckDuckGoSearchPage
from pages.DuckDuckGo.results import DuckDuckGoResultsPage

def test_basic_duckduckgo_search(
    page: Page,
    search_page: DuckDuckGoSearchPage,
    results_page: DuckDuckGoResultsPage) -> None:

    #Given I navigate to duckduckgo
    search_page.load()
    
    #And I search for "cheese"
    search_page.search("cheese")
    
    # Then the search result query is the phrase we searched for
    expect(results_page.search_input).to_have_value("cheese")
    
    # And the search result links pertain to the phrase
    assert results_page.check_list_of_links_contains_phrase("cheese")
    
    # And the search result title contains the phrase
    expect(page).to_have_title('cheese at DuckDuckGo')