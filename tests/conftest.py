import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
   print("\nstart browser for test..")
   browser = webdriver.Chrome()
   yield browser
   alert_obj = browser.switch_to.alert
   msg = alert_obj.text
   assert msg == 'Message received!'
   print(f'\nПоявился алерт с текстом {msg}\nВ поле Message выводится количество инструментов = 5 и название '
         f'инструмента max длиной Katalon Studio')
   time.sleep(10)
   print("\nquit browser..")
   browser.quit()