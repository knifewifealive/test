import os.path
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

DOWNLOAD_PATH = os.path.abspath("./tests/")


@pytest.fixture(scope="session")
def browser():
    gchr_options = Options()
    gchr_options.add_argument("--window-size=1600,900")
    gchr_options.add_argument("--headless")
    gchr_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_PATH,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(options=gchr_options)
    yield driver
    driver.quit()
