from playwright.sync_api import Page


class AutomationExerciseAccountConfirmation:
    def __init__(self, page: Page):
        self.page = page
        self.creation_message = page.get_by_text("Account Created")
        self.continue_button = page.get_by_text("Continue")
