from playwright.sync_api import Page

class RickAndMortyAboutPage:

    """Class containing page interactions for the About page - https://rickandmortyapi.com/about"""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.get_by_role("heading", name="About")