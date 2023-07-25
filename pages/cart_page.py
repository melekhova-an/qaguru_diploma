from pages.base_page import BasePage
from selene import browser
from allure import step


class ShoppingCartPage(BasePage):

    def select_all_product(self):
        with step('Выбрать все продукты на удаление'):
            products = browser.all('.cart [name="removefromcart"]')
            for el in products:
                el.click()

    def click_update_cart(self):
        with step('Кликнуть кнопку сохранения изменений в корзине'):
            browser.element('[name="updatecart"]').click()
