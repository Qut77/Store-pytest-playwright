from playwright.sync_api import expect
from pages.base_page import BasePage

class ProductPage(BasePage):
    URL = 'https://automationexercise.com/products'
    def product(self, index: int = 0):
        return self.page.locator(self.locators.single_products).nth(index)

    def hover_product(self, index: int = 0) -> None:
        self.product(index).hover()

    def expect_overlay_hidden(self, index: int = 0) -> None:
        expect(self.product(index).locator(self.locators.overlay)).not_to_be_visible()

    def expect_overlay_visible(self, index: int = 0) -> None:
        expect(self.product(index).locator(self.locators.overlay)).to_be_visible()
