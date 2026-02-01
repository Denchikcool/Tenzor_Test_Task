import os
import shutil
from pages.saby_home_page import SabyHomePage
from pages.saby_download_page import SabyDownloadPage
from config import DOWNLOAD_DIR

def clear_downloads():
    shutil.rmtree(DOWNLOAD_DIR, ignore_errors = True)
    os.makedirs(DOWNLOAD_DIR, exist_ok = True)

def test_third(driver):
    clear_downloads()
    saby_home = SabyHomePage(driver)
    saby_home.open("https://saby.ru/")
    saby_home.go_to_download()

    download_page = SabyDownloadPage(driver)
    expected_size = download_page.get_expected_file_size()
    download_page.download_plugin()
    file_path = download_page.wait_file()
    assert os.path.exists(file_path)
    actual_size = download_page.get_real_file_size(file_path)

    print("Ожидаемый размер: ", expected_size)
    print("Фактический размер: ", actual_size)

    assert expected_size == actual_size
