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



class TensorAbout(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://tensor.ru/about
        :param browser:
        """
        super().__init__(browser)

    def open(self):
        with allure.step('Open https://tensor.ru/ page'):
            self.browser.get('https://tensor.ru/')
