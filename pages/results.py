from playwright.sync_api import Page
from typing import List

class DuckDuckGoResultsPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input = page.locator("#search_form_input")
        self.results_links = page.locator('a[data-testid="result-title-a"]')

    def return_result_link_titles(self) -> List[str]:
        self.results_links.nth(4).wait_for()
        return self.results_links.all_text_contents()
    
    def check_list_of_links_contains_phrase(self, phrase: str, minimum: int = 1) -> bool:
        titles = self.return_result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()] 
        return len(matches) >= minimum