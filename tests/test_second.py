import requests
from pages.saby_home_page import SabyHomePage
from pages.saby_contacts_page import SabyContactsPage

'''
    По заданию этими двумя функциями я проверяю правильно ли определяется мой текущий регион, но
    как я выяснил, в тестах лучше не использовать сторонние регионы. Поэтому возникает вопрос:
    нужно ли просто определять есть ли регион в поле или же создать какую-то переменную со 
    своим регионом по типу MY_REGION = "Новосибирская обл.". Но тогда в зависимости от того, 
    на каком компьютере это будет запускаться, нужно будет каждый раз менять регион на свой.
    С этим моментом у меня непонятки небольшие.
'''
def get_my_region():
    response = requests.get("https://ipmy.dev/api?lang=ru")
    data = response.json()
    return data.get("region_name")

def normalize_region(region: str):
    return region.lower().replace("область", "").replace("обл.", "").strip()

def test_second(driver):
    saby_home = SabyHomePage(driver)
    saby_home.open("https://saby.ru/")
    saby_home.go_to_contacts()

    contacts = SabyContactsPage(driver)
    initial_region = contacts.get_region()
    expected_region = get_my_region()
    assert normalize_region(expected_region) in normalize_region(initial_region)
    assert contacts.has_partners()
    initial_partners = contacts.get_partners_name()

    contacts.change_region()

    assert contacts.is_region_is_kamchatka()
    new_partners = contacts.get_partners_name()
    assert new_partners != initial_partners
    assert contacts.is_title_contains_region()
    assert contacts.is_url_contains_region()