import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.fullscreen_window()
    yield driver
    driver.quit()
