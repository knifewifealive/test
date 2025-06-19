import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    gchr_options = Options()
    gchr_options.add_argument("--headless")
    driver = webdriver.Chrome(options=gchr_options)
    driver.fullscreen_window()
    yield driver
    driver.quit()


