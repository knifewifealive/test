import allure
import base64
import os.path
import pytest
from allure_commons.types import AttachmentType
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

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Получаем результат выполнения теста
    outcome = yield
    result = outcome.get_result()

    # Проверяем, что это фаза call (исполнение) и тест провалился
    if result.when == "call" and result.failed:
        # Получаем браузер из фикстуры
        browser = item.funcargs.get("browser", None)
        if browser:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="Screenshot on failure",
                attachment_type=AttachmentType.PNG
            )