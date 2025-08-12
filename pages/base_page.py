import time
from typing import Optional, Any

from selenium.common import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, url, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.driver.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.driver, timeout)
        self.url = url

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator),
                                                              message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator),
                                                              message=f"Can't find elements by locator {locator}")

    def open(self):
        """Открывает указанный URL в веб-браузере и разворачивает окно на весь экран
        """
        self.driver.maximize_window()
        return self.driver.get(self.url)

    def click_on_the_element(self, locator: tuple[str, str]) -> WebElement:
        """Нажимает на элемент на странице
            Args:
                locator: Кортеж из двух строк (стратегия поиска, значение локатора)
            Returns:
                WebElement: Объект найденного и кликнутого элемента
        """
        element = self.find_element(locator)
        element.click()
        return element

    def enter_word(self, locator: tuple[str, str], word: str) -> WebElement:
        """Ищет элемент на странице и заполняет поле ввода
            Args:
                locator: Кортеж из двух строк (стратегия поиска, значение локатора)
                word: Текст для ввода в поле
            Returns:
                WebElement: Объект элемента, в который был введен текст
        """
        search_field = self.click_on_the_element(locator)
        search_field.send_keys(word)
        return search_field

    def scroll_page(self, pixels: int = 500, delay_after: float = 0.5, behavior: str = "smooth") -> Optional[Any]:
        """Выполняет плавную прокрутку страницы
            Args:
                pixels(int = 500): Значение, на которое должна скроллиться страница
                delay_after(float = 0.5): Задержка после прокрутки в секундах
                behavior(str = "smooth"): Тип прокрутки
            Returns:
                Optional[Any]:  Результат выполнения JavaScript
        """
        try:
            result = self.driver.execute_script("""window.scrollBy({top: arguments[0],behavior: arguments[1]});""",
                                                pixels, behavior)
            if delay_after > 0:
                time.sleep(delay_after)
            return result
        except Exception as e:
            raise WebDriverException(f"Smooth scroll failed: {str(e)}")

    def check_element_on_checkbox(self, locator: tuple[str, str]) -> WebElement:
        """Выбирает элемент из checkbox
            Args:
                locator: Кортеж из двух строк (стратегия поиска, значение локатора)
            Returns:
                WebElement: Объект элемента Checkbox
        """
        return self.click_on_the_element(locator)

    def check_element_on_the_radiobutton(self, locator: tuple[str, str]) -> WebElement:
        """Выбирает элемент из radiobutton
            Args:
                locator: Кортеж из двух строк (стратегия поиска, значение локатора)
            Returns:
                WebElement: Объект элемента Radiobutton
        """
        return self.click_on_the_element(locator)

    def select_dropdown(self, locator: tuple[str, str]) -> list[WebElement]:
        """Выбирает элемент из dropdown
            Args:
                locator: Кортеж из двух строк (стратегия поиска, значение локатора)
            Returns:
                list[WebElement]: Список объектов элемента Dropdown
        """
        dropdown = Select(self.find_element(locator)).options
        return dropdown
