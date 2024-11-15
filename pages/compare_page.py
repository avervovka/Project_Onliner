from selenium.webdriver.common.by import By
from mobile_page import MobilePage
import re


class ComparePage(MobilePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.MOBILE_1_PRICE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[2]/tr/th[3]/div/div/div/a")
        self.MOBILE_2_PRICE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[2]/tr/th[4]/div/div/div[2]/a")
        self.MOBILE_1_DISPLAY_SIZE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[5]/tr[8]/td[3]/span/span")
        self.MOBILE_2_DISPLAY_SIZE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[5]/tr[8]/td[4]/span/span")

    # mobile_1_price_list = re.findall(r'\d+\,\d+|\d+', mobile_1_price)
    # time.sleep(5)
    # mobile_2_price = str(browser.find_element(*MOBILE_2_PRICE_LOCATOR).text)
    # mobile_2_price_list = re.findall(r'\d+\,\d+|\d+', mobile_2_price)
    # time.sleep(5)
    #
    def mobile_1_price_list(self):
        mobile_1_price = str(self.driver.find_element(*self.MOBILE_1_PRICE_LOCATOR))
        return re.findall(r'\d+\,\d+|\d+', mobile_1_price)

    def mobile_2_price_list(self):
        self.driver.find_element(*self.MOBILE_2_PRICE_LOCATOR)
        mobile_2_price = str(self.driver.find_element(*self.MOBILE_2_PRICE_LOCATOR))
        return re.findall(r'\d+\,\d+|\d+', mobile_2_price)

    def price_list(self):
        self.mobile_1_price_list() + self.mobile_2_price_list()

