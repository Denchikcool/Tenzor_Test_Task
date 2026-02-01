import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import DOWNLOAD_DIR

@pytest.fixture(scope = "function")
def driver():
    options = Options()
    prefs = {
        "download.default_directory": DOWNLOAD_DIR
    }
    options.add_experimental_option("prefs", prefs)
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options = options)
    yield driver
    driver.quit()