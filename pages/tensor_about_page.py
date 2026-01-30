from .base_page import BasePage

class TensorAboutPage(BasePage):
    URL = "https://tensor.ru/about"
    #WORK_SECTION = ("xpath", "//div[contains(@class,'tensor_ru-About__block3')]")
    IMAGES = ("xpath", "//div[@class='tensor_ru-About__block3-image-wrapper']/img")

    def is_needed_url(self):
        return bool(self.get_url() == self.URL)
    
    def get_images_size(self):
        images = self.find_elements(self.IMAGES)
        print(len(images))
        return [img.size for img in images if img.is_displayed()]
    
    def is_all_images_same_size(self):
        sizes = self.get_images_size()

        if not sizes:
            return False
        
        first_height, first_width = sizes[0]['height'], sizes[0]['width']
        return all(size['height'] == first_height and size['width'] == first_width for size in sizes)