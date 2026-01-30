from .base_page import BasePage

class TensorHomePage(BasePage):
    BLOCK_POWER_IN_PEOPLE = ("xpath", "//p[text()='Сила в людях']")
    DETAILS_LINK = ("xpath", "//a[contains(@class, 'tensor_ru-link tensor_ru-Index__link') and @href='/about']")

    def has_power_in_people_block(self):
        return bool(self.find_element(self.BLOCK_POWER_IN_PEOPLE))
    
    def click_details(self):
        self.click(self.DETAILS_LINK)