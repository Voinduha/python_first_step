from selene.support.shared import browser
import pytest


@pytest.fixture(autouse=True)
def screen_config():
    browser.open('https://google.com').driver.maximize_window()
