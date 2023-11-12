from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogMenuComponent(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.MP3_PLAYERS = (By.XPATH, "//*[text()='MP3 Players']")
        self.SHOW_ALL_MP3_PLAYERS = (By.XPATH, "//*[text()='Show All MP3 Players']")

    def click_mp3_players(self):
        self.get_element_by_locator(self.MP3_PLAYERS).click()

    def show_all_mp3_players(self):
        self.get_element_by_locator(self.SHOW_ALL_MP3_PLAYERS).click()
