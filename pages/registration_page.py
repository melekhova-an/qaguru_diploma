from pages.base_page import BasePage
from selene import browser, have, be
from allure import step


class RegistrationPage(BasePage):

    def input_personal_data(self, gender, first_name, last_name, email):
        with step('Заполнить данные'):
            browser.element(f'#gender-{gender}').click()
            self.fill_input('#FirstName', first_name)
            self.fill_input('#LastName', last_name)
            self.fill_input('#Email', email)

    def input_password_user(self, password):
        with step('Ввести пароль'):
            self.fill_input('#Password', password)
            self.fill_input('#ConfirmPassword', password)

    @staticmethod
    def click_register_button():
        with step('Кликнуть кнопку "Register"'):
            browser.element('#register-button').click()

    def check_success_register(self):
        with step('Проверить, что пользователь зарегистрировался'):
            browser.element('div.result').should(have.text('Your registration completed'))
            browser.element('div.result').should(be.clickable)
