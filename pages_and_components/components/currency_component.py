import random
import allure
from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CurrencyComponent(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.CURRENCY_DROPDOWN = (By.XPATH, '//*[@data-toggle="dropdown"]//*[text()="Currency"]')
        self.CURRENCY = (By.XPATH, '//*[@data-toggle="dropdown"]//strong')
        self.EUR_IN_DROPDOWN = (By.XPATH, '//*[@name="EUR"]')
        self.GBP_IN_DROPDOWN = (By.XPATH, '//*[@name="GBP"]')
        self.USD_IN_DROPDOWN = (By.XPATH, '//*[@name="USD"]')

    @allure.step("Click CURRENCY_DROPDOWN")
    def open_currency_dropdown(self):
        el = self.get_element_by_locator(self.CURRENCY_DROPDOWN)
        el.click()

    @allure.step("Check currency in dropdown")
    def is_currency_in_dropdown(self, currency):
        try:
            self.get_element_by_locator(By.XPATH, f'//*[@name="{currency}"]')
            return True
        except TimeoutException:
            return False

    @allure.step("Change rendom currency")
    def change_random_currency(self):
        list_cur = [self.EUR_IN_DROPDOWN, self.GBP_IN_DROPDOWN, self.USD_IN_DROPDOWN]
        cur_random = random.choice(list_cur)
        cur_el = self.get_element_by_locator(cur_random)   # получаем рандомный элемент валюты
        cur_full_text = cur_el.text         # получаем полный текст из элемента валюты
        cur = cur_full_text.split(" ")[0]   # получаем символ валюты
        cur_el.click()                      # выбираем эту новую валюту в дропдауне
        new_cur_el = self.get_element_by_locator(self.CURRENCY)  # получаем новый элемент валюты
        new_cur_full_text = new_cur_el.text
        new_cur = new_cur_full_text.split(" ")[0]                # получаем символ валюты, на которую мы поменяли
        if cur == new_cur:
            return True
        else:
            return False
