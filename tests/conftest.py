import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
   print("\nstart browser for test..")
   options = Options()
   options.add_argument('--ignore-certificate-errors')
   browser = webdriver.Chrome(options=options)
   #browser = webdriver.Chrome()
   yield browser
   alert_obj = browser.switch_to.alert
   msg = alert_obj.text
   print(msg)
   assert msg == 'Message received!'
   print("\nquit browser..")
   browser.quit()