import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import DOWNLOAD_DIR

@pytest.fixture(scope = "function")
def driver():
    options = Options()
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options = options)
    yield driver
    driver.quit()