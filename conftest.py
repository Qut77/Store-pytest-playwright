import pytest
from playwright.sync_api import Playwright, Page
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import *

@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-qa")

@pytest.fixture
def login_page(page:Page) -> LoginPage:
    return LoginPage(
        page=page,
        locators=LoginPageLocators
    )

@pytest.fixture
def product_page(page:Page) -> ProductPage:
    return ProductPage(
        page=page,
        locators=ProductPageLocators
    )