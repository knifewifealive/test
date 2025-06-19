import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

"""
Находим раздел Работаем и проверяем, что у всех фотографии
хронологии одинаковые высота (height) и ширина (width)
"""

work_block_selector = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .s-Grid-container')



class TensorAbout(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://tensor.ru/about
        :param browser:
        """
        super().__init__(browser)

    def open(self):
        with allure.step('Open https://tensor.ru/about page'):
            self.browser.get('https://tensor.ru/about')