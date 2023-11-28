from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class MyAccountPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.TITLE = "My Account"
        self.EDIT_INFO_LINK = (By.XPATH, '//a[text()="Edit your account information"]')
        self.CHANGE_PASSWORD_LINK = (By.XPATH, '//a[text()="Change your password"]')
        self.YOUR_TRANSACTIONS_LINK = (By.XPATH, '//a[text()="Your Transactions"]')
        self.LOGOUT_BUTTON_RIGHT_MENU = (By.XPATH, '//*[@class="list-group"]//*[text()="Logout"]')
        self.check_my_account_page()
        self.logger = browser.logger

    def check_my_account_page(self):
        self.wait_title_change(self.TITLE)

    def check_links_visible(self):
        try:
            self.is_element_visible(self.EDIT_INFO_LINK)
            self.is_element_visible(self.CHANGE_PASSWORD_LINK)
            self.is_element_visible(self.YOUR_TRANSACTIONS_LINK)
            return True
        except TimeoutException:
            return False

    def check_logout_button_right_menu(self):
        try:
            self.is_element_visible(self.LOGOUT_BUTTON_RIGHT_MENU)
            return True
        except TimeoutException:
            return False
