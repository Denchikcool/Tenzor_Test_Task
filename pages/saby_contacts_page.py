from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class SabyContactsPage(BasePage):
    TENSOR_BANNER = ("xpath", "//a[contains(@class,'sbisru-Contacts__logo-tensor')]")
    REGION = ("xpath", "//div[contains(@class, 's-Grid-col')]//span[contains(@class, 'sbis_ru-Region-Chooser__text')]")
    #PARTNERS_LIST = ("xpath", "//div[contains(@name, 'itemsContainer')]")
    PARTNERS = ("xpath", "//div[contains(@class, 'sbisru-Contacts-List__col-1')]")
    PARTNERS_NAME = ("xpath", "//div[contains(@class, 'sbisru-Contacts-List__col-1')]//div")
    REGION_ITEM = ("xpath", "//span[contains(text(), '41 Камчатский край')]")

    REGION_NAME = "Камчатский край"
    URL_PART = "41-kamchatskij-kraj"

    def click_tensor_banner(self):
        self.click(self.TENSOR_BANNER)
    
    def get_region(self):
        return self.get_text(self.REGION)
    
    def has_partners(self):
        return len(self.find_elements(self.PARTNERS)) > 0
    
    def get_partners_name(self):
        return [element.text for element in self.find_elements(self.PARTNERS_NAME) if element.text]
    
    def change_region(self):
        self.click(self.REGION)
        self.wait.until(EC.visibility_of_element_located(self.REGION_ITEM))
        self.click(self.REGION_ITEM)
        self.wait.until(EC.text_to_be_present_in_element(self.REGION, self.REGION_NAME))
        self.wait.until(EC.url_contains(self.URL_PART))
    
    def is_region_is_kamchatka(self):
        return self.REGION_NAME in self.get_region()

    def is_url_contains_region(self):
        return self.URL_PART in self.get_url().lower()

    def is_title_contains_region(self):
        return self.REGION_NAME in self.get_title()