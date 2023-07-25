from selene import browser, have
from allure import step


class BasePage:

    @staticmethod
    def open_registration_page():
        with step('Открыть страницу регистрации'):
            browser.element('.ico-register').press_enter()

    @staticmethod
    def open_login_page():
        with step('Открыть страницу авторизации'):
            browser.element('.ico-login').press_enter()

    def fill_input(self, locator, text):
        browser.element(locator).send_keys(text)

    def product_search(self, product):
        with step('Найти товар по названию'):
            self.fill_input('input#small-searchterms', product)
            browser.element('.search-box-button').click()

    def check_found_item(self, product):
        with step('Проверить товар'):
            browser.element('.product-item').should(have.text(f'{product}'))

    def add_product_to_cart(self, category_name):
        with step(f'Добавить товар из категории: {category_name}'):
            browser.element(f'.top-menu [href="/{category_name}"]').click()
            self.count_before_add = self.count_product_to_cart()
            item_for_add = browser.all('.page .button-2')
            self.count_product = len(item_for_add)
            for element in item_for_add:
                element.click()
                browser.with_(timeout=1).wait_until(have.text('product has been added'))
                browser.element('#bar-notification .close').click()

    def count_product_to_cart(self):
        quantity = browser.element('span.cart-qty').locate().text
        return int(''.join(filter(str.isdigit, quantity)))

    def check_quantity_product_to_cart(self):
        with step('Проверить количество товара в корзине'):
            quantity = browser.element('span.cart-qty').locate().text
            count_after_add = int(''.join(filter(str.isdigit, quantity)))
            assert (count_after_add - self.count_before_add) == self.count_product

    def open_shopping_cart(self):
        with step('Открыть страницу с выбранным товаром'):
            browser.element('.header-links .ico-cart').click()

    def check_empty_cart(self):
        with step('Проверить, что корзина пустая'):
            quantity = browser.element('span.cart-qty').locate().text
            count = int(''.join(filter(str.isdigit, quantity)))
            browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))
            assert count == 0
