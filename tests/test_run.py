import allure
import pytest

class TestCases:
    @allure.severity(severity_level="Blocker")
    @allure.epic("Страница Form Fields")
    @allure.feature("Заполнение формы")
    @allure.story("Проверка заполнения всех полей формы валидными данными")
    @pytest.mark.smoke
    def test_filling_out_form(self, browser, main_page, generate_data):
        main_page.verify_filling_out_a_web_form(generate_data)
