from pages.base_page import BasePage
from pages.selectors import TensorAboutPageSelectors
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Находим раздел Работаем и проверяем, что у всех фотографии
хронологии одинаковые высота (height) и ширина (width)
"""


class TensorAbout(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://tensor.ru/about
        :param browser:
        """
        super().__init__(browser)
        self.page_url = "https://tensor.ru/about"
        self.browser = browser

    @property
    def work_block(self):
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(TensorAboutPageSelectors.work_block_selector)
        )

    @property
    def work_block_exists(self) -> bool:
        return self.work_block.is_displayed()

    @property
    def work_block_containts_equal_imgs(self) -> bool:
        """

        :return: true if block contains equal imgs, false if not
        """
        imgs = self.find_all(TensorAboutPageSelectors.imgs_in_work_block_selector)
        width, height = [], []
        for img in imgs:
            width.append(img.get_attribute('height'))
            height.append(img.get_attribute('height'))

        return (len(set(width)) or len(set(height))) <= 1
