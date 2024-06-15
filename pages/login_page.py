from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "URL is not correct, there is no login in it"

    def should_be_login_form(self):
        login_is_available = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_is_available, "Login form is not found"

    def should_be_register_form(self):
        register_is_available = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_is_available, "Register form is not found"
