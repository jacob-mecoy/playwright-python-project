from playwright.sync_api import Page

class RickAndMortyDocumentationPage:

    """Class containing page interactions for the Documentation page - https://rickandmortyapi.com/documentation"""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.get_by_role("heading", name="Documentation")