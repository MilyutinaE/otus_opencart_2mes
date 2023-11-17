from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminLeftMenu(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.CATALOG = (By.XPATH, "//*[text()=' Catalog']")
        self.PRODUCTS = (By.XPATH, "//a[text()='Products']")
        self.logger = browser.logger

    def select_products(self):
        self.logger.info("Click CATALOG in left menu")
        self.click(self.CATALOG)
        self.logger.info("Click PRODUCTS in left menu")
        self.click(self.PRODUCTS)
