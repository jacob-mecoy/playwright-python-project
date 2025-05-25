# API Tests
from playwright.sync_api import Page, expect

# Characters API: /api/character - Test filters and individual character retrieval
# Location API: /api/location - Test location schema and individual location retrieval
# Episode API: /api/episode - Test episode schema and that there is at least 1 character present

# Characters API

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