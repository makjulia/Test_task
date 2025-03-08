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

    # Метод для поиска элемента на странице и заполнения поля
    def enter_word(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    # Метод для нажатия на кнопку
    def click_on_the_button(self, locator):
        return self.find_element(locator).click()

    # Метод для поиска элементов списка Automation tools
    def check_tools(self, locator):
        auto_tools = self.find_elements(locator)
        check_bar = [x.text for x in auto_tools if len(x.text) > 0]
        return check_bar

    # Метод для определения кол-ва элементов в Automation tools
    def get_count_elements(self, iterable):
        return len(iterable)

    #Метод для определения max длинной строчки в Automation tools
    def get_elem_with_max_len(self, iterable):
        return max(iterable, key=len)

    # Скроллинг страницы
    def scroll_page(self, t=1):
         scroll = self.driver.execute_script("window.scrollBy(0, 500)")
         time.sleep(t)
         return scroll


