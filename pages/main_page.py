from .base_page import BasePage
from selenium.webdriver.common.by import By
import time


class SeacrhLocators:
    LOCATOR_NAME = (By.ID, "name-input")
    LOCATOR_PASSWORD = (By.CSS_SELECTOR, "[type='password']")
    LOCATOR_CHECKBOX_1 = (By.CSS_SELECTOR, "[value='Milk']")
    LOCATOR_CHECKBOX_2 = (By.CSS_SELECTOR, "[value='Coffee']")
    LOCATOR_RADIOBUTTON = (By.CSS_SELECTOR, "[value='Yellow']")
    LOCATOR_LIST = (By.XPATH, "//select[@id='automation']")
    LOCATOR_LIST_VARIABLE = (By.CSS_SELECTOR, "option:nth-child(2)")
    LOCATOR_MAIL = (By.ID, "email")
    LOCATOR_LIST_TOOLS = (By.CSS_SELECTOR, "#feedbackForm ul li")
    LOCATOR_MESSAGE = (By.ID, "message")
    LOCATOR_BUTTON = (By.ID, "submit-btn")


class SearchHelper(BasePage):

    def enter_word(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_button(self, locator):
        return self.find_element(locator).click()

    def check_tools(self, locator):
        auto_tools = self.find_elements(locator)
        check_bar = [x.text for x in auto_tools if len(x.text) > 0]
        return check_bar

    # Методы для определения кол-ва инструментов в Automation tools
    def get_count_elements(self, iterable):
        return len(iterable)

    def get_len_max_elem(self, iterable):
        return len(max(iterable, key=len))

    def scroll_page(self, t=2):
         scroll = self.driver.execute_script("window.scrollBy(0, 500)")
         time.sleep(t)
         return scroll


