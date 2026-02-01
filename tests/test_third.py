import os
import shutil
from pages.saby_home_page import SabyHomePage
from pages.saby_download_page import SabyDownloadPage
from config import DOWNLOAD_DIR

'''
    С этим тестом два основных вопроса:
    1. Нет в текущей версии сайта вкладки "СБИС Плагин", как указано в файле с заданием, поэтому
    я решил скачивать с вкладки "Saby (десктоп)", т.к. в url увидел tab=plugin, а в задании
    как раз говорилось про плагин.
    2. На сайте не было указано в виде текста размер файла, так что пришлось читать характеристики файла (.exe)
    по ссылке, которая хранится в теге <a>. Благодаря head и ключу Content-Length я узнал размер файла в байтах.
'''

def clear_downloads():
    shutil.rmtree(DOWNLOAD_DIR, ignore_errors = True)
    os.makedirs(DOWNLOAD_DIR, exist_ok = True)

def test_third(driver):
    clear_downloads()
    saby_home = SabyHomePage(driver)
    saby_home.open("https://saby.ru/")
    saby_home.go_to_download()

    download_page = SabyDownloadPage(driver)
    download_page.click_on_correct_tab()
    expected_size = download_page.get_expected_file_size()
    download_page.download_plugin()
    file_path = download_page.wait_file()
    assert os.path.exists(file_path), "Файл не скачался"
    actual_size = download_page.get_real_file_size(file_path)

    assert expected_size == actual_size, "Размеры файлов отличаются"
