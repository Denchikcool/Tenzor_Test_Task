from .base_page import BasePage

class TensorHomePage(BasePage):
    URL = "https://tensor.ru/"
    BLOCK_POWER_IN_PEOPLE = ("xpath", "//p[contains(text(),'Сила в людях')]")
    DETAILS_LINK = ("xpath", "//a[contains(@class, 'tensor_ru-link') and @href='/about']")

    def is_needed_url(self):
        return bool(self.get_url() == self.URL)
    
    def has_power_in_people_block(self):
        return bool(self.find_element(self.BLOCK_POWER_IN_PEOPLE))
    
    def click_details(self):
        self.click(self.DETAILS_LINK)