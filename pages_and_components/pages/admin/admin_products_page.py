from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminProductsPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.ADD_NEW = (By.XPATH, "//*[@data-original-title='Add New']")
        self.NAME_IMAC = (By.XPATH, "//*[@class='text-left' and text()='iMac']")
        self.IMAC_EDIT_BUTTON = (By.XPATH, "//*[@class='text-left' and text()='iMac']/following-sibling::td/a")
        self.DELETE = (By.XPATH, "//*[@data-original-title='Delete']")
        self.IMAC_CHECKBOX = (By.XPATH, "//*[@class='text-left' and text()='iMac']/preceding-sibling::td//"
                                        "*[@type='checkbox']")

    def click_add_new(self):
        self.click(self.ADD_NEW)

    def check_product_title(self, name):
        result = self.is_element_visible((By.XPATH, f"//*[text()='{name}']"))
        return result

    def click_edit_imac(self):
        self.click(self.IMAC_EDIT_BUTTON)

    def select_imac(self):
        self.click(self.IMAC_CHECKBOX)

    def click_delete(self):
        self.click(self.DELETE)
        self.accept_alert()
