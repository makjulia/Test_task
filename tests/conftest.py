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
   print(msg)
   assert msg == 'Message received!'
   time.sleep(10)
   print("\nquit browser..")
   browser.quit()