from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminProductsPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.ADD_NEW = (By.XPATH, "//*[@data-original-title='Add New']")
        self.NAME_IPHONE = (By.XPATH, "//*[@class='text-left' and text()='iPhone']")
        self.IPHONE_EDIT_BUTTON = (By.XPATH, "//*[@class='text-left' and text()='iPhone']/following-sibling::td/a")
        self.DELETE = (By.XPATH, "//*[@data-original-title='Delete']")
        self.IPHONE_CHECKBOX = (By.XPATH, "//*[@class='text-left' and text()='iPhone']/preceding-sibling::td//*"
                                          "[@type='checkbox']")
        self.logger = browser.logger

    def click_add_new(self):
        self.logger.info("Click add new product")
        self.click(self.ADD_NEW)

    def check_product_title(self, name):
        result = self.is_element_visible((By.XPATH, f"//*[text()='{name}']"))
        return result

    def click_edit_iphone(self):
        self.logger.info("Click edit iPhone")
        self.click(self.IPHONE_EDIT_BUTTON)

    def select_iphone(self):
        self.logger.info("Select iPhone")
        self.click(self.IPHONE_CHECKBOX)

    def click_delete(self):
        self.logger.info("Delete iPhone")
        self.click(self.DELETE)
        self.accept_alert()
