from pages.base_page import BasePage
from pages.selectors import TensorPageSelectors
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
Перейти на https://tensor.ru/,
Проверить, что есть блок "Сила в людях",
Перейти в этом блоке в "Подробнее" и убедиться, что открывается https://tensor.ru/about
"""


class TensorPage(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://tensor.ru/about
        :param browser:
        """
        super().__init__(browser)
        self.page_url = 'https://tensor.ru/'
        self.browser = browser

    def tensor_block(self):
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(TensorPageSelectors.power_in_people_block_selector)
        )

    @property
    def tensor_block_exists(self) -> bool:
        return self.find(TensorPageSelectors.power_in_people_block_selector).is_displayed()

    @property
    def tensor_block_get_more_info_link(self) -> str:
        return self.find(TensorPageSelectors.get_more_info_link_selector).get_attribute('href')
