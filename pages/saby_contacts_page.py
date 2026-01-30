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
    
    def is_region_is_kamchatka(self):
        return "Камчатский край" in self.get_region()

    def is_url_contains_region(self):
        return "41-kamchatskij-kraj" in self.get_url().lower()

    def is_title_contains_region(self):
        #return self.wait.until(EC.title_contains("Камчатский край")) in self.get_title()
        return "Камчатский край" in self.get_title()