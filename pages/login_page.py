from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = 'https://automationexercise.com/login'

    def __init__(self, page):
        super().__init__(page)
        self.login_email = page.get_by_test_id('login-email')
        self.login_password = page.get_by_test_id('login-password')
        self.login_button = page.get_by_test_id('login-button')
        self.delete_account_button = page.locator('.fa.fa-trash-o')

    def login(self, email:str, password:str) -> None:
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def expect_user_logged_in(self) -> None:
        expect(self.delete_account_button).to_be_visible()