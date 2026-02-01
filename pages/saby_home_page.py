from .base_page import BasePage

class SabyHomePage(BasePage):
    CONTACTS_MENU = ("xpath", "//span[contains(text(),'Контакты')]")
    CONTACTS_SUB_LINK = ("xpath", "//a[contains(@class,'sbisru-link')]")
    DOWNLOAD_LINK = ("xpath", "//a[contains(@href, 'download')]")

    def go_to_contacts(self):
        self.hover(self.CONTACTS_MENU)
        self.click(self.CONTACTS_SUB_LINK)
    
    def go_to_download(self):
        self.click(self.DOWNLOAD_LINK)