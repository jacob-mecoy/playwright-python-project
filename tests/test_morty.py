# Tests for the Rick & Morty website - https://rickandmortyapi.com/
from playwright.sync_api import Page, expect
# UI Tests

# Homepage navigation and content verification - This task was left intentionally open ended.
# All menu items on the documentation page works correctly

# Test1 - Can navigate to the homepage and the title displays
def test_homepage(page: Page) -> None:
    page.goto("https://rickandmortyapi.com/")
    heading_locator = page.get_by_role("heading", name="The Rick and Morty API")
    expect(heading_locator).to_be_visible()

# Test2 - There are 6 unique characters shown when getting to the homepage
def test_unique_characters(page: Page) -> None:
    page.goto("https://rickandmortyapi.com/")
    character_card_locator = page.get_by_role("article")
    expect(character_card_locator).to_have_count(6)
    #verify the 6 characters have a unique id
    character_card_locator_list = [character_card_locator.nth(x) for x in range(6)]
    character_name_link_list = [x.get_by_role("link").nth(0) for x in character_card_locator_list]
    url_list = [x.get_attribute("href") for x in character_name_link_list]
    #get the id from the url by taking the characters that appear after the final "/"
    character_id_list = [x.split("/")[-1] for x in url_list]
    if len(set(character_id_list)) != 6:
        raise ValueError("there are fewer than 6 unique characters")
    
# Test3 - Docs link works
def test_docs_link(page: Page) -> None:
    page.goto("https://rickandmortyapi.com/")
    page.get_by_role("link", name="Docs").click()
    #verify we are on the correct page by verifying we can see the documentation page header
    page.get_by_role("heading", name="Documentation")

# Test4 - About link works
def test_about_link(page: Page) -> None:
    page.goto("https://rickandmortyapi.com/")
    page.get_by_role("link", name="About").click()
    #verify we are on the correct page by verifying we can see the documentation page header
    page.get_by_role("heading", name="About")


# API Tests

# Characters API: /api/character - Test filters and individual character retrieval
# Location API: /api/location - Test location schema and individual location retrieval
# Episode API: /api/episode - Test episode schema and that there is at least 1 character present

# The following tests can be done for each API - characters, location & episode

# Test1 - Get request is successful and returns expected count of results
def test_api_get_all_characters(page: Page) -> None:
    response = page.request.get("https://rickandmortyapi.com/api/character")
    expect(response).to_be_ok()
    character_count = response.json().get("info").get("count")
    assert character_count == 826

# Test2 - Get request specifying an id is successful and returns one result
def test_api_get_character_by_id(page: Page) -> None:
    response = page.request.get("https://rickandmortyapi.com/api/character/1")
    expect(response).to_be_ok()
    api_response = response.json()
    #verify that multiple characters are not returned by verifying a list is not returned
    assert type(api_response) == dict
    #verify that one characters is returned by verifying the "info" key is not present in the response
    assert "info" not in api_response.keys()

# Test3 - Get request with a filter is successful and returns relevant results 
def test_api_get_character_with_filters(page: Page) -> None:
    response = page.request.get("https://rickandmortyapi.com/api/character", params={"name":"rick", "status":"alive"})
    expect(response).to_be_ok()
    character_count = response.json().get("info").get("count")
    assert character_count == 29