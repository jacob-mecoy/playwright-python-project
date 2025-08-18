from playwright.sync_api import expect
from pytest_bdd import then

from pages.RickAndMorty.homepage import RickAndMortyHomepage


@then("there are 6 characters shown")
def six_characters_shown(homepage_page: RickAndMortyHomepage):
    expect(homepage_page.character_cards).to_have_count(6)


@then("the characters are all unique")
def the_characters_are_all_unique(homepage_page: RickAndMortyHomepage):
    character_id_list = homepage_page.retrieve_character_card_ids()
    if len(set(character_id_list)) != 6:
        raise ValueError("there are fewer than 6 unique characters")
