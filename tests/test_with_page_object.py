from models.admin import username, passwod
from models.product import name_product, meta_tag, model
from pages_and_components.components.admin.admin_left_menu import AdminLeftMenu
from pages_and_components.components.currency_component import CurrencyComponent
from pages_and_components.components.header_component import HeaderComponent
from pages_and_components.pages.admin.admin_add_product_page import AdminAddProductPage
from pages_and_components.pages.admin.admin_login_page import AdminLoginPage
from pages_and_components.pages.admin.admin_products_page import AdminProductsPage
from pages_and_components.pages.registration_page import RegistrationPage
from pages_and_components.pages.my_account_page import MyAccountPage
from models.fake_user import fake_first_name, fake_last_name, fake_email, fake_phone, fake_password


def test_register_new_user(browser):
    "Регаемся и проверяем линки и кнопку логаута на странице аккаунта"
    header = HeaderComponent(browser)
    header.click_on_my_account_registration()
    register = RegistrationPage(browser)
    register.registration_new_user(fake_first_name(), fake_last_name(), fake_email(), fake_phone(), fake_password())
    my_account = MyAccountPage(browser)
    assert my_account.check_links_visible()
    assert my_account.check_logout_button_right_menu()


def test_change_currency(browser):
    "Меняем валюту в хедере и проверяем, что она поменялась"
    currency = CurrencyComponent(browser)
    currency.open_currency_dropdown()
    assert currency.change_random_currency()


def test_add_mew_product(browser, base_url):
    "Успешно и неуспешно добавляем новый продукт в админке"
    browser.get(f"{base_url}/admin")
    admin_login = AdminLoginPage(browser)
    admin_login.login(username, passwod)
    admin_left_menu = AdminLeftMenu(browser)
    admin_left_menu.select_products()
    admin_products_page = AdminProductsPage(browser)
    admin_products_page.click_add_new()
    add_product = AdminAddProductPage(browser)
    assert add_product.add_new_product_success(name_product, meta_tag, model)
    assert admin_products_page.check_product_title(name_product)
    admin_products_page.click_add_new()
    add_product = AdminAddProductPage(browser)
    assert add_product.add_new_product_fail(name_product, meta_tag)


def test_delete_product(browser, base_url):
    "Удаляем продукт в админке"
    browser.get(f"{base_url}/admin")
    admin_login = AdminLoginPage(browser)
    admin_login.login(username, passwod)
    admin_left_menu = AdminLeftMenu(browser)
    admin_left_menu.select_products()
    admin_products_page = AdminProductsPage(browser)
    admin_products_page.select_imac()
    admin_products_page.click_delete()
    assert admin_products_page.check_product_title(name="iMac") is False
