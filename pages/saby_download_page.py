import os
import time
import requests
from .base_page import BasePage
from config import DOWNLOAD_DIR

class SabyDownloadPage(BasePage):
    PLUGIN_TAB = ("xpath", "//div[contains(@data-id,'plugin')]")
    DOWNLOAD_BUTTON = ("xpath", "//span[contains(@name, 'DownloadNewButton')]//span[contains(text(), 'Скачать')]")
    FILE_NAME = "saby-setup.exe"

    def download_plugin(self):
        self.click(self.DOWNLOAD_BUTTON)

    def get_expected_file_size(self):
        url = self.find_element(self.DOWNLOAD_BUTTON).get_attribute("href")
        req = requests.head(url, allow_redirects = True)
        return round(int(req.headers["Content-Length"]) / 1024 / 1024, 2)
    
    def wait_file(self, timeout = 60):
        path = os.path.join(DOWNLOAD_DIR, self.FILE_NAME)

        for _ in range(30):
            if os.path.exists(path) and not os.path.exists(path + ".crdownload"):
                return path
            time.sleep(1)
        
        raise TimeoutError("Файл не скачался")
    
    def get_real_file_size(self, path):
        return round(os.path.getsize(path) / 1024 / 1024, 2)