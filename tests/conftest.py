import os
import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from utils.helper import CustomSession
from selenium.webdriver.chrome.options import Options
from utils import attach
import requests


@pytest.fixture(scope='session')
def reqres():
    return CustomSession(base_url=os.getenv("base_url_regres"))


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture()
def web_browser():
    options = Options()

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '100.0',
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    options.capabilities.update(selenoid_capabilities)

    s_login = os.getenv('LOGIN')
    s_password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{s_login}:{s_password}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    browser.config.driver = driver
    browser.config.base_url = os.getenv('base_url')
    browser.open("")

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture()
def request_auth():
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    payload = {'Email': login, 'Password': password}

    response = requests.post(
        url=f"{os.getenv('base_url')}/login",
        params=payload,
        headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
        allow_redirects=False,
    )
    return response


@pytest.fixture()
def auth_through_api(request_auth, web_browser):
    token = request_auth.cookies.get('NOPCOMMERCE.AUTH')
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": token})
    browser.open("")
