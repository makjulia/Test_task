import allure
import random

from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from config.config import Url


class SearchLocators:
    NAME_FIELD = (By.ID, "name-input")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[type='password']")
    CHECKBOX_DRINKS_MILK = (By.CSS_SELECTOR, "[value='Milk']")
    CHECKBOX_DRINKS_COFFEE = (By.CSS_SELECTOR, "[value='Coffee']")
    RADIOBUTTON_COLOR = (By.CSS_SELECTOR, "[value='Yellow']")
    DROPDOWN_AUTOMATION = (By.XPATH, "//select[@id='automation']")
    EMAIL_FIELD = (By.ID, "email")
    AUTOMATION_TOOLS = (By.CSS_SELECTOR, "#feedbackForm ul li")
    MESSAGE_FIELD = (By.ID, "message")
    BUTTON_SUBMIT = (By.ID, "submit-btn")


class SearchHelper(BasePage):

    def __init__(self, driver):
        url = Url.BASE_URL
        super().__init__(url, driver)

    @allure.step("Заполнение поля Name")
    def enter_field_name_on_page(self, name: str) -> WebElement:
        """Заполняет поле Name на странице Form Fields
            Args:
                name: Имя пользователя
            Returns:
                WebElement: Объект элемента Name field
        """
        return self.enter_word(SearchLocators.NAME_FIELD, f"{name}")

    @allure.step("Заполнение поля Password")
    def enter_field_password_on_page(self, password: str) -> WebElement:
        """Заполняет поле Password на странице Form Fields
            Args:
                password: Пароль пользователя
            Returns:
                WebElement: Объект элемента Password field
        """
        return self.enter_word(SearchLocators.PASSWORD_FIELD, f"{password}")

    @allure.step("Заполнение поля Email")
    def enter_field_email_on_page(self, email: str) -> WebElement:
        """Заполняет поле Email на странице Form Fields
            Args:
                email: Email пользователя
            Returns:
                WebElement: Объект элемента Email field
        """
        return self.enter_word(SearchLocators.EMAIL_FIELD, f"{email}")

    @allure.step("Выбор из списка двух значений - Milk, Coffee")
    def check_drinks(self) -> tuple[WebElement, WebElement]:
        """Выбирает из списка What is your favorite drink? два варианта ответа - Milk, Coffee
            Returns:
                tuple[WebElement, WebElement]: Кортеж из двух WebElement:
                                    - Первый элемент: чекбокс 'Milk'
                                    - Второй элемент: чекбокс 'Coffee'
        """
        milk = self.check_element_on_checkbox(SearchLocators.CHECKBOX_DRINKS_MILK)
        coffee = self.check_element_on_checkbox(SearchLocators.CHECKBOX_DRINKS_COFFEE)
        return milk, coffee

    @allure.step("Выбор из списка значения Yellow")
    def check_color(self) -> WebElement:
        """Выбирает из списка What is your favorite color? вариант ответа Yellow
            Returns:
                WebElement: Элемент Yellow из списка
        """
        return self.check_element_on_the_radiobutton(SearchLocators.RADIOBUTTON_COLOR)

    @allure.step("Выбор из выпадающего списка случайного значения")
    def select_answer_on_the_dropdown(self) -> WebElement:
        """Выбирает из выпадающего списка Do you like automation? случайный ответ
            Returns:
                WebElement: Случайный элемент из выпадающего списка
        """
        answer = self.select_dropdown(SearchLocators.DROPDOWN_AUTOMATION)
        return random.choice(answer)

    @allure.step("Поиск элементов списка Automation tools")
    def check_tools(self, locator: tuple[str, str]) -> list[str]:
        """Ищет элементы списка Automation tools
            Args:
                locator: Кортеж из двух строк (стратегия поиска, значение локатора)
            Returns:
                list[str]: Список элементов Automation tools
        """
        auto_tools = self.find_elements(locator)
        check_bar = [tools.text for tools in auto_tools if len(tools.text) > 0]
        return check_bar

    @allure.step("Подсчет количества элементов в списке Automation tools")
    def get_count_elements(self, list_tools: list[str]) -> int:
        """Подсчитывает количество элементов в списке Automation tools
            Args:
                list_tools: Список элементов Automation tools
            Returns:
                int: Количество элементов в списке Automation tools
        """
        return len(list_tools)

    @allure.step("Определение самой длинной строки в списке Automation tools")
    def get_elem_with_max_len(self, list_tools: list[str]) -> str:
        """Определяет самую длинную строку в списке Automation tools
            Args:
                list_tools: Список элементов Automation tools
            Returns:
                 str: Самая длинная строка в списке Automation tools
        """
        return str(max(list_tools, key=len))

    @allure.step("Формирование данных для заполнения поля Message")
    def data_for_field_message(self) -> tuple[int, str]:
        """Формирует данные для заполнения поля Message
            Returns:
                tuple[int, str]: Кортеж из двух элементов:
                                    - Количество элементов в списке Automation tools
                                    - Самая длинная строка в списке Automation tools
        """
        list_tools = self.check_tools(SearchLocators.AUTOMATION_TOOLS)
        count_tools = self.get_count_elements(list_tools)
        tools_with_max_len = self.get_elem_with_max_len(list_tools)
        assert count_tools == 5
        assert tools_with_max_len == "Katalon Studio"
        return count_tools, tools_with_max_len

    @allure.step("Заполнение поля Message")
    def enter_field_message(self) -> WebElement:
        """Заполняет поле Message
            Returns:
                WebElement: Объект элемента поле Message
        """
        data = self.data_for_field_message()
        count_tools, tools_with_max_len = data
        return self.enter_word(SearchLocators.MESSAGE_FIELD, f"{count_tools}\n{tools_with_max_len}")

    @allure.step("Нажатие на кнопку Submit")
    def click_on_the_button_submit(self) -> WebElement:
        """Нажимает на кнопку Submit
            Returns:
                WebElement: Объект элемента кнопка Submit
        """
        return self.click_on_the_element(SearchLocators.BUTTON_SUBMIT)

    @allure.step("Заполнение формы на странице Form Fields")
    def filling_out_a_web_form(self, data: tuple[str:3]) -> None:
        """Заполняет форму на странице Form Fields
            Args:
                data: Кортеж из 3 строковых элементов в строгом порядке:
                    - name (str): Имя для поля 'Name'
                    - password (str): Пароль для поля 'Password'
                    - email (str): Email для поля 'Email'
            Returns:
                None: Ничего не возвращает
        """
        name, password, email = data
        self.enter_field_name_on_page(name)
        self.enter_field_password_on_page(password)
        self.scroll_page()
        self.check_drinks()
        self.check_color()
        self.scroll_page()
        self.select_answer_on_the_dropdown()
        self.enter_field_email_on_page(email)
        self.enter_field_message()
        self.click_on_the_button_submit()

    @allure.step("Проверка появления алерта с сообщением об успешном заполнении формы Form Fields")
    def verify_filling_out_a_web_form(self, data: tuple[str:3]) -> None:
        """Проверяет, что форма успешно заполнена
            Args:
                data: Кортеж из 3 строковых элементов в строгом порядке:
                    - name (str): Имя для поля 'Name'
                    - password (str): Пароль для поля 'Password'
                    - email (str): Email для поля 'Email'
            Returns:
                None: Ничего не возвращает
        """
        self.filling_out_a_web_form(data)
        alert = self.driver.switch_to.alert
        msg = alert.text
        alert.accept()
        assert msg == 'Message received!'
