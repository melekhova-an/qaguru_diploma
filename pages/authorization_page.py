from pages.base_page import BasePage
from selene import browser, have
from allure import step


class AuthorizationPage(BasePage):

    def input_email_and_password(self, email, password):
        with step('Ввести емейл и пароль'):
            self.fill_input('#Email', email)
            self.fill_input('#Password', password)

    @staticmethod
    def click_auth_button():
        with step('Кликнуть кнопку "Log in"'):
            browser.element('.login-button').click()

    def check_success_auth(self, email):
        with step('Проверить, что пользователь авторизировался'):
            browser.element('.header-links .account').should(have.text(email))
