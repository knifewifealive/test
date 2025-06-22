from pages.selectors import DownloadPageSelectors
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DownloadPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://sbis.ru/download"

    def download_link_button(self):
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(DownloadPageSelectors.download_link)
        )
