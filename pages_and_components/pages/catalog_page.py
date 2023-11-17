from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CatalogPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.PRODUCTS = (By.CSS_SELECTOR, ".product-thumb")
        self.PRICES = (By.XPATH, '//*[@class="price"]')
        self.ADD_TO_CARD_BUTTONS = (By.XPATH, "//*[text()='Add to Cart']")
        self.SELECTED_CATEGORY = (By.XPATH, "//*[@class='list-group-item active']")
        self.PRODUCTS_NAMES = (By.XPATH, "//h4/a")
        self.logger = browser.logger

    def check_content_visible(self):
        try:
            self.is_element_visible(self.PRODUCTS)
            self.is_element_visible(self.PRICES)
            self.is_element_visible(self.ADD_TO_CARD_BUTTONS)
            return True
        except TimeoutException:
            return False

    def check_selected_category(self, category):
        selected_category = self.get_element_by_locator(self.SELECTED_CATEGORY).text
        if category in selected_category:
            return True
        else:
            return False

    def wait_title(self, title):
        self.wait_title_change(title)

    def click_first_product(self):
        self.logger.info("Click first product")
        self.get_element_by_locator(self.PRODUCTS_NAMES).click()
