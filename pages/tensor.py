import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import Optional, Dict, Any

"""
Перейти на https://tensor.ru/,
Проверить, что есть блок "Сила в людях",
Перейти в этом блоке в "Подробнее" и убедиться, что открывается https://tensor.ru/about
"""

power_in_people_block_selector = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
get_more_info_link_selector = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg a.tensor_ru-link.tensor_ru-Index__link')


class TensorPage(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://tensor.ru/about
        :param browser:
        """
        super().__init__(browser)
        self.page_url = 'https://tensor.ru/'

    @property
    def tensor_block_exists(self) -> bool:
        return self.find(power_in_people_block_selector).is_displayed()
    @property
    def tensor_block_get_more_info_link(self) -> str:
        return self.find(get_more_info_link_selector).get_attribute('href')