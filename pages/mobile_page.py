from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver


class MobilePage:
    URL = "https://catalog.onliner.by/mobile"
    CHECKBOXES_LOCATOR = (By.XPATH, "//*[contains(@title, ' ')][contains(@class, 'checkbox')]")
    COMPARE_LOCATOR = (By.XPATH, "//*[contains(@href, 'compare')]")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_e_checkbox(self):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES_LOCATOR)
        checkboxes[0].click()
        checkboxes[1].click()

    # def click_second_checkbox(self):
    #     checkboxes = self.driver.find_elements(*self.CHECKBOXES_LOCATOR)
    #     if len(checkboxes) > 1:
    #         checkboxes[1].click()

    def compare_link_exists(self):
        compare_button = self.driver.find_element(*self.COMPARE_LOCATOR)
        return compare_button.is_displayed()
