import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.fullscreen_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
