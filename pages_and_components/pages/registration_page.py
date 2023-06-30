from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class RegistrationPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.INPUT_FIRSTNAME = (By.ID, 'input-firstname')
        self.INPUT_LASTNAME = (By.ID, 'input-lastname')
        self.INPUT_EMAIL = (By.ID, "input-email")
        self.INPUT_TELEPHONE = (By.ID, "input-telephone")
        self.INPUT_PASSWORD = (By.ID, 'input-password')
        self.INPUT_PASSWORD_CONFIRM = (By.ID, 'input-confirm')
        self.PRIVACY_POLICY = (By.NAME, 'agree')
        self.CONTINUE_BUTTON = (By.XPATH, "//input[@type='submit']")
        self.CONTINUE_SECOND_BUTTON = (By.XPATH, "//a[text()='Continue']")
        self.TITLE = "Register Account"
        self.TITLE_SUCCESSFUL = "Your Account Has Been Created!"
        self.check_registration_page()

    def registration_new_user(self, firstname, lastname, email, telephone, password):
        self.click(self.INPUT_FIRSTNAME)
        self.send_keys(self.INPUT_FIRSTNAME, firstname)
        self.click(self.INPUT_LASTNAME)
        self.send_keys(self.INPUT_LASTNAME, lastname)
        self.click(self.INPUT_EMAIL)
        self.send_keys(self.INPUT_EMAIL, email)
        "Второй вариант написания кода send_keys через точку"
        self.get_element_by_locator(self.INPUT_TELEPHONE).send_keys(telephone)
        self.get_element_by_locator(self.INPUT_PASSWORD).send_keys(password)
        self.get_element_by_locator(self.INPUT_PASSWORD_CONFIRM).send_keys(password)
        self.get_element_by_locator(self.PRIVACY_POLICY).click()
        self.get_element_by_locator(self.CONTINUE_BUTTON).click()
        self.check_registration_sucsessful()
        self.get_element_by_locator(self.CONTINUE_SECOND_BUTTON).click()

    def check_registration_page(self):
        assert self.wait_title_change(self.TITLE)

    def check_fields(self):
        try:
            self.get_element_by_locator(self.INPUT_FIRSTNAME)
            self.get_element_by_locator(self.INPUT_LASTNAME)
            self.get_element_by_locator(self.INPUT_EMAIL)
            self.get_element_by_locator(self.INPUT_TELEPHONE)
            self.get_element_by_locator(self.PRIVACY_POLICY)
            return True
        except TimeoutException:
            return False

    def check_registration_sucsessful(self):
        self.wait_title_change(self.TITLE_SUCCESSFUL)
