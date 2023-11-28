from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger

    def is_element_visible(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                name=self.driver.current_url,
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            return False
        return True

    def get_element_by_locator(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:

            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    def clear_input(self, input):
        self.logger.info("Clear input")
        input.send_keys(Keys.SHIFT, Keys.ARROW_UP)
        input.send_keys(Keys.BACK_SPACE)

    def send_keys(self, element, keys):
        element = self.get_element_by_locator(element)
        element.send_keys(keys)

    def accept_alert(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()

    def click(self, locator: tuple):
        self.get_element_by_locator(locator).click()

    def wait_title_change(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
        except TimeoutException:
            return False
        return True
