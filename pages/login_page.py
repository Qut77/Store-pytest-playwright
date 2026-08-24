from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = 'https://automationexercise.com/login'
        

    def login(self, email:str, password:str) -> None:
        self.page.get_by_test_id(self.locators.LOGIN_EMAIL).fill(email)
        self.page.get_by_test_id(self.locators.LOGIN_PASS).fill(password)
        self.page.get_by_test_id(self.locators.LOGIN_BUTTON).click()

    def expect_user_logged_in(self) -> None:
        expect(self.page.locator(self.locators.DELETE_ACCOUNT_BUTTON)).to_be_visible()