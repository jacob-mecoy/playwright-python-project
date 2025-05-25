# Tests for the Rick & Morty website - https://rickandmortyapi.com/
from playwright.sync_api import expect
from pages.RickAndMorty.homepage import RickAndMortyHomepage
from pages.RickAndMorty.documentation import RickAndMortyDocumentationPage
from pages.RickAndMorty.about import RickAndMortyAboutPage
# UI Tests

# Homepage navigation and content verification - This task was left intentionally open ended.
# All menu items on the documentation page works correctly

# Test1 - Can navigate to the homepage and the title displays
def test_homepage(homepage_page: RickAndMortyHomepage) -> None:
    homepage_page.load()
    expect(homepage_page.title).to_be_visible()

# Test2 - There are 6 unique characters shown when getting to the homepage
def test_unique_characters(homepage_page: RickAndMortyHomepage) -> None:
    homepage_page.load()
    expect(homepage_page.character_cards).to_have_count(6)
    #verify the 6 characters have a unique id
    character_id_list = homepage_page.retrieve_character_card_ids()
    if len(set(character_id_list)) != 6:
        raise ValueError("there are fewer than 6 unique characters")
    
# Test3 - Docs link works
def test_docs_link(homepage_page: RickAndMortyHomepage, documentation_page: RickAndMortyDocumentationPage) -> None:
    homepage_page.load()
    homepage_page.navigate_to_docs()
    #verify we are on the correct page by verifying we can see the documentation page header
    expect(documentation_page.title).to_be_visible()

# Test4 - About link works
def test_about_link(homepage_page: RickAndMortyHomepage, about_page: RickAndMortyAboutPage) -> None:
    homepage_page.load()
    homepage_page.about_link.click()
    #verify we are on the correct page by verifying we can see the documentation page header
    expect(about_page.title).to_be_visible()
