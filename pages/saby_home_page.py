from .base_page import BasePage

class SabyHomePage(BasePage):
    CONTACTS_MENU = ("xpath", "//span[contains(text(),'Контакты')]")
    CONTACTS_SUB_LINK = ("xpath", "//a[contains(@class,'sbisru-link')]")

    def go_to_contacts(self):
        self.hover(self.CONTACTS_MENU)
        self.click(self.CONTACTS_SUB_LINK)