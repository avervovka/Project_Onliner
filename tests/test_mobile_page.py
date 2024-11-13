import pytest
from pages.mobile_page import MobilePage
import time


def test_opened(driver):
    mobile_page = MobilePage(driver)
    mobile_page.open()
    assert driver.current_url == mobile_page.URL, f'{MobilePage.URL} not equals {driver.current_url}'


def test_checkbox_clicked(driver):
    mobile_page = MobilePage(driver)
    mobile_page.open()
    mobile_page.click_first_checkbox()
    # mobile_page.click_second_checkbox()
    assert mobile_page.compare_link_exists(), 'Nothing to compare'
