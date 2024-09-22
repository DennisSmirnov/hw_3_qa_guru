import pytest
from selene import browser
from selenium.webdriver import Firefox


@pytest.fixture(scope='session')
def browser_controller():
    browser.config.driver = Firefox()
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open('https://google.com/ncr')
    yield
    browser.quit()


@pytest.fixture(autouse=True)
def reset_browser():
    yield
    browser.open('https://google.com/ncr')
