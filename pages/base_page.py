from playwright.sync_api import Page

class BasePage:
    URL = None

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        if not self.URL:
            raise NotImplementedError("Page must define URL")
        self.page.goto(self.URL)