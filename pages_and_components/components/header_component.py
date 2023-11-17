from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderComponent(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.MY_ACCOUNT_BUTTON = (By.XPATH, '//span[text()="My Account"]')
        self.REGISTER_IN_MY_ACCOUNT_DROPDOWN = (By.XPATH, '//*[@class="dropdown-menu dropdown-menu-right"]'
                                                          '//*[text()="Register"]')
        self.logger = browser.logger

    def click_on_my_account_registration(self):
        el = self.get_element_by_locator(self.MY_ACCOUNT_BUTTON)
        self.logger.info("Click MY_ACCOUNT_BUTTON")
        el.click()
        self.get_element_by_locator(self.REGISTER_IN_MY_ACCOUNT_DROPDOWN).click()
