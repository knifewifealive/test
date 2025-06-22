import allure
import os
from pages.base_page import BasePage
from pages.download import DownloadPage
from services.static_methods import StaticMethods as SM

DOWNLOAD_PATH = os.path.abspath("./tests/")
print(DOWNLOAD_PATH)


@allure.feature('Main page, download button-link in footer')
@allure.story('UX')
def test_able_to_download(browser):
    with allure.step('Open main page'):
        base_page = BasePage(browser)
        base_page.open("https://saby.ru/")
    with allure.step('Check link existence to go to saby.ru/downloads'):
        assert base_page.download_link_is_displayed
    with allure.step('Check the URL'):
        assert base_page.download_link().get_attribute('href') == 'https://saby.ru/download'
    with allure.step('Go to download page, download a file'):
        base_page.download_link().click()
        download_page = DownloadPage(browser)
        download_page.download_link_button().click()
    with allure.step('Wait till download finish'):
        downloaded_file = SM.wait_for_download(DOWNLOAD_PATH)
    with allure.step('Compare file sizes'):
        expected_file_size = SM.get_size_of_file(download_page.download_link_button().text)
        actual_size_mb = round(downloaded_file.stat().st_size / (1024 * 1024), 2)
        assert actual_size_mb == expected_file_size
    with allure.step('Delete file from OS'):
        assert SM.delete_file(downloaded_file)