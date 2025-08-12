import pytest

from pages.main_page import SearchHelper


@pytest.fixture(scope="function")
def main_page(browser):
    main_page = SearchHelper(browser)
    main_page.open()
    return main_page
