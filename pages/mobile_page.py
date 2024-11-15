import pytest
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MobilePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.COMPARE_LOCATOR = (By.XPATH, "//*[@id='container']/div/div/div/div/div[3]/div/div/div[1]/a")
        self.URL = "https://catalog.onliner.by/mobile"

        self.CHECKBOXES_LOCATOR = (By.XPATH, "//*[contains(@title, ' ')][contains(@class, 'checkbox')]")
        self.MIN_PRICE_LOCATOR = (By.XPATH,
                                  "//*[@id='container']/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[12]/div/div/div[2]/div[2]/div/div[1]/input")
        self.MAX_PRICE_LOCATOR = (By.XPATH,
                         "//*[@id='container']/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[12]/div/div/div[2]/div[2]/div/div[2]/input")
        self.ACCEPT_COOKIES_BUTTON_LOCATOR = (By.XPATH, "//*[@id='submit-button']")

    def url(self):
        return self.URL

    def open(self):
        self.driver.get(self.URL)

    def find_and_click_cookies_message(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON_LOCATOR)).click()

    def click_checkbox_1(self, index):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES_LOCATOR)
        if len(checkboxes) > index:
            checkboxes[index].click()

    def click_checkbox_2(self, index):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES_LOCATOR)
        if len(checkboxes) > index:
            checkboxes[index].click()

    def checkbox_is_selected(self, index):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES_LOCATOR)
        return checkboxes[index].is_selected()

    def compare_button(self):
        button = self.driver.find_element(*self.COMPARE_LOCATOR)
        return button
