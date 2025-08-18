from typing import List

from playwright.sync_api import Page


class RickAndMortyHomepage:
    """Class containing page interactions for the homepage - https://rickandmortyapi.com/"""

    URL = "https://rickandmortyapi.com/"

    # initialiser method creates a page for each test
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.get_by_role("heading", name="The Rick and Morty API")
        self.character_cards = page.get_by_role("article")
        self.documents_link = page.get_by_role("link", name="Docs")
        self.about_link = page.get_by_role("link", name="About")

    def load(self) -> None:
        self.page.goto(self.URL)

    def retrieve_character_card_ids(self) -> List[str]:
        character_card_locator_list = [self.character_cards.nth(x) for x in range(6)]
        character_name_link_list = [
            x.get_by_role("link").nth(0) for x in character_card_locator_list
        ]
        url_list = [x.get_attribute("href") for x in character_name_link_list]
        # get the id from the url by taking the characters that appear after the final "/"
        return [x.split("/")[-1] for x in url_list]

    def navigate_to_docs(self) -> None:
        self.documents_link.click()
