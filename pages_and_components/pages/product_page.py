from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.AVAILABILITY = (By.XPATH, "//*[@class='list-unstyled']//*[contains(text(), 'Availability:')]")
        self.PRODUCT_CODE = (By.XPATH,  "//*[@class='list-unstyled']//*[contains(text(),'Product Code:')]")
        self.BRAND = (By.XPATH, "//*[@class='list-unstyled']//*[contains(text(), 'Brand:')]")
        self.ADD_TO_CART = (By.XPATH, "//*[text()='Add to Cart']")
        self.DESCRIPTION = (By.XPATH, "//*[text()='Description']")
        self.logger = browser.logger

    def check_content_visible(self):
        try:
            self.is_element_visible(self.AVAILABILITY)
            self.is_element_visible(self.PRODUCT_CODE)
            self.is_element_visible(self.BRAND)
            self.is_element_visible(self.ADD_TO_CART)
            self.is_element_visible(self.DESCRIPTION)
            return True
        except TimeoutException:
            return False
