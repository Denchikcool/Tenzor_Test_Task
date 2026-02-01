import os
import time
import requests
from .base_page import BasePage
from config import DOWNLOAD_DIR
from logger import logger

class SabyDownloadPage(BasePage):
    PLUGIN_TAB = ("xpath", "//div[contains(@data-id,'plugin')]")
    DOWNLOAD_BUTTON = ("xpath", "//a[contains(@title, 'Скачать')]")
    FILE_NAME = "saby-setup.exe"

    def click_on_correct_tab(self):
        self.click(self.PLUGIN_TAB)

    def download_plugin(self):
        self.click(self.DOWNLOAD_BUTTON)

    def get_expected_file_size(self):
        url = self.find_element(self.DOWNLOAD_BUTTON).get_attribute("href")
        logger.info(f"LOGGER URL: {url}")
        req = requests.head(url, allow_redirects = True)
        size = round(int(req.headers["Content-Length"]) / 1024 / 1024, 2)
        logger.info(f"EXPECTED SIZE: {size} Mb")
        return size
    
    def wait_file(self, timeout = 60):
        path = os.path.join(DOWNLOAD_DIR, self.FILE_NAME)
        logger.info(f"WAIT FILE: {path}")

        for _ in range(timeout):
            if os.path.exists(path) and not os.path.exists(path + ".crdownload"):
                logger.info("FILE DOWNLOADED")
                return path
            time.sleep(1)
        
        logger.info("DOWNLOAD TIMEOUT")
        raise TimeoutError("Файл не скачался")
    
    def get_real_file_size(self, path):
        size = round(os.path.getsize(path) / 1024 / 1024, 2)
        logger.info(f"REAL SIZE: {size} Mb")
        return size