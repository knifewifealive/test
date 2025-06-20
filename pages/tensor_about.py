import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import Any
"""
Находим раздел Работаем и проверяем, что у всех фотографии
хронологии одинаковые высота (height) и ширина (width)
"""

work_block_selector = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .s-Grid-container')
imgs_in_work_block_selector = (By.CSS_SELECTOR, 'img.tensor_ru-About__block3-image')


class TensorAbout(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://tensor.ru/about
        :param browser:
        """
        super().__init__(browser)
        self.page_url = "https://tensor.ru/about"

    @property
    def work_block(self) -> Any:
        return self.find(work_block_selector)

    @property
    def work_block_exists(self) -> bool:
        return self.find(work_block_selector).is_displayed()

    @property
    def work_block_containts_equal_imgs(self) -> bool:
        """

        :return: true if block contains equal imgs, false if not
        """
        imgs = self.find_all(imgs_in_work_block_selector)
        width, height = [], []
        for img in imgs:
            width.append(img.get_attribute('height'))
            height.append(img.get_attribute('height'))

        return (len(set(width)) or len(set(height))) <= 1