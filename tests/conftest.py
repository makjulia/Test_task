import pytest
from selenium import webdriver

from pages.main_page import SearchHelper

pytest_plugins = ["fixtures.data_fixtures",
                  "fixtures.open_page_fixtures"]


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
