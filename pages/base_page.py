from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver = driver, timeout = 15, poll_frequency = 1)

    def open(self, url):
        logger.info(f"OPEN URL: {url}")
        self.driver.get(url)
    
    def find_element(self, locator):
        logger.info(f"FIND ELEMENT: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        logger.info(f"FIND ELEMENTS: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        logger.info(f"CLICK: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def get_text(self, locator):
        logger.info(f"GET TEXT FROM: {locator}")
        return self.find_element(locator).text

    def get_url(self):
        logger.info("GETTING URL")
        return self.driver.current_url
    
    def get_title(self):
        logger.info("GETTING TITLE")
        return self.driver.title
    
    def hover(self, locator):
        logger.info(f"HOVER: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def switch_to_new_window(self):
        logger.info("SWITCH TO NEW WINDOW")
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])