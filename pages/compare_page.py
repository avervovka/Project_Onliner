from selenium.webdriver.common.by import By
from mobile_page import MobilePage
import re


class ComparePage(MobilePage):
    MOBILE_1_PRICE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[2]/tr/th[3]/div/div/div/a")
    MOBILE_2_PRICE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[2]/tr/th[4]/div/div/div[2]/a")
    MOBILE_1_DISPLAY_SIZE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[5]/tr[8]/td[3]/span/span")
    MOBILE_2_DISPLAY_SIZE_LOCATOR = (By.XPATH, "//*[@id='product-table']/tbody[5]/tr[8]/td[4]/span/span")

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
        price = self.mobile_1_price_list() + self.mobile_2_price_list()
        all_price_list_final = [float(i.replace(',', '.')) for i in price]
        return all_price_list_final

    def maximum_price(self):
        maximum = max(self.price_list())
        return maximum

    def minimum_price(self):
        minimum = max(self.price_list())
        return minimum

    def list_displays(self):
        display1 = self.driver.find_element(*self.MOBILE_1_DISPLAY_SIZE_LOCATOR).text.replace('"', '')
        display2 = self.driver.find_element(*self.MOBILE_1_DISPLAY_SIZE_LOCATOR).text.replace('"', '')
        all_displays = [display1, display2].sort()
        return all_displays

    # def minimum_display(self):
    #     minimum = min(self.list_displays())
    #     return minimum
    #
    # def maximum_display(self):
    #     max_display = self.driver.find_element(*self.MOBILE_1_DISPLAY_SIZE_LOCATOR)
    #     return max_display
    #
