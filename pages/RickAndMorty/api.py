from typing import Dict

from playwright.sync_api import Page


class RickAndMortyAPI:
    """Class containing api interactions for Rick And Morty website"""

    def __init__(self, page: Page) -> None:
        self.url = "https://rickandmortyapi.com/api/character"
        self.page = page
        self.response = None

    def get_all_characters(self) -> None:
        self.response = self.page.request.get(self.url)

    def get_character_by_id(self, id: int) -> None:
        self.response = self.page.request.get(f"{self.url}/{id}")

    def get_characters_with_params(self, params: Dict) -> None:
        self.response = self.page.request.get(self.url, params=params)
