import time 
from pages.saby_home_page import SabyHomePage
from pages.saby_contacts_page import SabyContactsPage

def test_second(driver):
    saby_home = SabyHomePage(driver)
    saby_home.open("https://saby.ru/")
    saby_home.go_to_contacts()

    contacts = SabyContactsPage(driver)
    initial_region = contacts.get_region()
    print(initial_region)
    assert initial_region
    print(contacts.has_partners())
    assert contacts.has_partners()
    initial_partners = contacts.get_partners_name()
    #print(initial_partners)

    contacts.change_region()

    print(contacts.get_region())
    #assert contacts.is_region_is_kamchatka()
    print(contacts.get_title())
    print(contacts.get_url())
    #assert contacts.is_title_contains_region()
    #assert contacts.is_url_contains_region()
    #new_partners = contacts.get_partners_name()
    #print(new_partners)
    #assert new_partners != initial_partners

    time.sleep(15)