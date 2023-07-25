import os
import pytest

import allure

from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
from pages.authorization_page import AuthorizationPage
from pages.cart_page import ShoppingCartPage

from utils.helper import generate_last_name, generate_first_name, generate_email

reg_page = RegistrationPage()
auth_page = AuthorizationPage()
cart_page = ShoppingCartPage()
start_page = BasePage()


class TestWebShopUI:

    USER_DATA = [
        ('female', generate_first_name(), generate_last_name(), generate_email(), '123456')
    ]

    @allure.label('owner', 'An')
    @allure.feature('WebShop')
    @allure.title('Registration user')
    @pytest.mark.parametrize('gender, first_name, last_name, email, password', USER_DATA)
    def test_registration_user(self, web_browser, gender, first_name, last_name, email, password):
        reg_page.open_registration_page()
        reg_page.input_personal_data(gender, first_name, last_name, email)
        reg_page.input_password_user(password)
        reg_page.click_register_button()

        reg_page.check_success_register()

    @allure.label('owner', 'An')
    @allure.feature('WebShop')
    @allure.title('Login user')
    def test_auth_user(self, web_browser):
        email = os.getenv('user_login')
        password = os.getenv('user_password')

        auth_page.open_login_page()
        auth_page.input_email_and_password(email, password)
        auth_page.click_auth_button()

        auth_page.check_success_auth(email)

    @allure.label('owner', 'An')
    @allure.feature('WebShop')
    @allure.title('Search product')
    @pytest.mark.parametrize('product', ('Blue Jeans', '14.1-inch Laptop'))
    def test_search_product(self, auth_through_api, product):
        start_page.product_search(product)

        start_page.check_found_item(product)

    @allure.label('owner', 'An')
    @allure.feature('WebShop')
    @allure.title('Add product to card')
    @pytest.mark.parametrize('category', ['books', 'digital-downloads'])
    def test_add_product_to_cart(self, auth_through_api, category):
        auth_page.add_product_to_cart(category)

        auth_page.check_quantity_product_to_cart()

    @allure.label('owner', 'An')
    @allure.feature('WebShop')
    @allure.title('Delete product from cart')
    @pytest.mark.parametrize('category', [
        'books',
        'digital-downloads'])
    def test_delete_product_from_cart(self, auth_through_api, category):
        cart_page.add_product_to_cart(category)
        auth_page.open_shopping_cart()
        cart_page.select_all_product()
        cart_page.click_update_cart()

        cart_page.check_empty_cart()
