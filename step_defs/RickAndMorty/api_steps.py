import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then

from pages.RickAndMorty.api import RickAndMortyAPI


@pytest.fixture
def api(page: Page) -> RickAndMortyAPI:
    return RickAndMortyAPI(page)


@given("I get all characters using the character API")
def get_all_characters(api: RickAndMortyAPI):
    api.get_all_characters()


@given("I get a single character via id")
def get_one_character(api: RickAndMortyAPI):
    api.get_character_by_id(1)


@given("I get characters that match specific filters")
def get_characters_using_filters(api: RickAndMortyAPI):
    api.get_characters_with_params({"name": "rick", "status": "alive"})


@then("the response is ok")
def verify_response_is_ok(api: RickAndMortyAPI):
    expect(api.response).to_be_ok()


@then(parsers.parse("the response contains only {number_of_characters:d} character"))
@then(parsers.parse("the response contains {number_of_characters:d} characters"))
def verify_character_count(api: RickAndMortyAPI, number_of_characters: int):
    """
    Verifies that the API response contains the expected number of characters.
    - For single characters, expects a dict that doesn't contain 'info'.
    - For multiple characters, expects a paginated response with 'info.count'.
    """
    response_json = api.response.json()
    if number_of_characters == 1:
        assert isinstance(response_json, dict)
        assert "info" not in response_json.keys()
    else:
        response_character_count = response_json.get("info", {}).get("count")
        assert response_character_count == number_of_characters
