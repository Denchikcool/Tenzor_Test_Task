from .base_page import BasePage

class SabyHomePage(BasePage):
    CONTACTS_MENU = ("xpath", "//span[text()='Контакты']")
    CONTACTS_SUB_LINK = ("xpath", "//a[contains(@class, 'sbisru-link sbis_ru-link')]")

    def go_to_contacts(self):
        self.open("https://saby.ru/")
        self.hover(self.CONTACTS_MENU)
        self.click(self.CONTACTS_SUB_LINK)