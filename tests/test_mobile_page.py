import pytest
from pages.mobile_page import MobilePage
# from pages.compare_page import ComparePage
import time
from selenium.webdriver.common.by import By


def test_opened(driver):
    mobile_page = MobilePage(driver)
    mobile_page.open()
    assert driver.current_url == mobile_page.URL, 'NOT THE SAME URL'


def test_cookies(driver):
    mobile_page = MobilePage(driver)
    time.sleep(5)
    mobile_page.find_and_click_cookies_message()


def test_click_checkbox_1(driver):
    mobile_page = MobilePage(driver)
    time.sleep(5)
    mobile_page.click_checkbox_1(0)
    # assert mobile_page.checkbox_is_selected(0), 'First Mobile Phone NOT selected'


def test_click_checkbox_2(driver):
    mobile_page = MobilePage(driver)
    mobile_page.click_checkbox_2(1)
#     # assert mobile_page.checkbox_is_selected(1), 'Second Mobile Phone NOT selected'


def test_compare_button(driver):
    mobile_page = MobilePage(driver)
    try:
        mobile_page.compare_button().click()
        driver.back()
    finally:
        print('THIS TEST IS NOT GOOD')


