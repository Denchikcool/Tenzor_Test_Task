import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope = "function")
def driver():
    #options = Options()
    #options.add_argument("--headless")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()