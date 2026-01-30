from .base_page import BasePage

class SabyContactsPage(BasePage):
    TENSOR_BANNER = ("xpath", "//a[contains(@class, 'sbisru-Contacts__logo-tensor mb-12')]")

    def click_tensor_banner(self):
        self.click(self.TENSOR_BANNER)