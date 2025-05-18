from playwright.sync_api import Page, expect

def test_basic_duckduckgo_search(page: Page) -> None:
    page.goto("https://duckduckgo.com/")
    page.locator("#searchbox_input").fill("cheese")
    # page.locator("#gNO89b").click()
    page.locator(".searchbox_searchButton__LxebD").click()
    # Then the search result query is the phrase
    expect(page.locator("#search_form_input")).to_have_value("cheese")
    # And the search result links pertain to the phrase
    page.locator('a[data-testid="result-title-a"]').nth(4).wait_for()
    titles = page.locator('a[data-testid="result-title-a"]').all_text_contents()
    matches = [t for t in titles if "cheese" in t.lower()] 
    assert len(matches) > 0
    # And the search result title contains the phrase
    expect(page).to_have_title('cheese at DuckDuckGo')
    pass