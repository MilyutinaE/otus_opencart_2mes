from models.admin import username, passwod
from pages_and_components.components.header_component import HeaderComponent
from pages_and_components.pages.admin.admin_login_page import AdminLoginPage
from pages_and_components.pages.catalog_page import CatalogPage
from pages_and_components.pages.product_page import ProductPage
from pages_and_components.pages.registration_page import RegistrationPage
from pages_and_components.pages.main_page import MainPage
from pages_and_components.components.catalog_menu_component import CatalogMenuComponent


def test1_main_page(browser):
    "Проверяем контент на мейн пейдже"
    main_page = MainPage(browser)
    assert main_page.check_content_visible()


def test2_catalog_page_mp3_players(browser):
    "В синем меню сверху выбираем MP3 Players и открываем каталог с плеерами"
    catalog_menu = CatalogMenuComponent(browser)
    catalog_menu.click_mp3_players()
    catalog_menu.show_all_mp3_players()
    catalog_page = CatalogPage(browser)
    catalog_page.check_content_visible()
    catalog_page.wait_title("MP3 Players")
    assert catalog_page.check_selected_category("MP3 Players")
    catalog_page.wait_title("MP3 Players")


def test3_product_page(browser):
    "Открываем страницу первого мп3 плеера из каталога и проверяем контент"
    catalog_menu = CatalogMenuComponent(browser)
    catalog_menu.click_mp3_players()
    catalog_menu.show_all_mp3_players()
    catalog_page = CatalogPage(browser)
    catalog_page.click_first_product()
    product_page = ProductPage(browser)
    assert product_page.check_content_visible()


def test4_admin_page(browser, base_url):
    "Проверяем неуспешный логин"
    browser.get(f"{base_url}/admin")
    admin_login = AdminLoginPage(browser)
    assert admin_login.failed_login(username, passwod)


def test5_register_page(browser):
    "Проверяем поле имя, фамилия, емейл, телефон, чекбокс на странице реги"
    header = HeaderComponent(browser)
    header.click_on_my_account_registration()
    register = RegistrationPage(browser)
    assert register.check_fields()
