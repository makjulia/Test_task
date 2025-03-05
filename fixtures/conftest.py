import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
   print("\nstart browser for test..")
   browser = webdriver.Chrome()
   browser.maximize_window()
   yield browser
   print("\nquit browser..")
   time.sleep(30)
   browser.quit()