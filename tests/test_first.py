from pages.saby_home_page import SabyHomePage
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_home_page import TensorHomePage
from pages.tensor_about_page import TensorAboutPage

def test_first(driver):
    saby_home = SabyHomePage(driver)
    saby_home.open("https://saby.ru/")
    saby_home.go_to_contacts()

    contacts = SabyContactsPage(driver)
    contacts.click_tensor_banner()
    contacts.switch_to_new_window()

    tensor_home = TensorHomePage(driver)
    assert "https://tensor.ru/" == tensor_home.get_url()
    assert tensor_home.has_power_in_people_block()
    tensor_home.click_details()

    about = TensorAboutPage(driver)
    assert about.is_needed_url()
    assert about.is_all_images_same_size()