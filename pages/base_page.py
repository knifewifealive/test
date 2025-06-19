import allure
from attr.converters import optional
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional, Dict, Any

"""
раздел "Контакты" (Ещё <> офисов в
регионе)
"""

contact_button_to_pop_up = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu.js-ContactsMenu .sbisru-Header__menu-link')
more_offices_in_regions_link = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items > .sbisru-link.sbis_ru-link')


class BasePage:
    def __init__(self,browser):
        self.browser = browser
        """
        При наследовании от этого класса, нужно переопределить аттрибут page_url, который будет хранить в себе
        ссылку на странице с который работаем
        """
        self.page_url = 'https://saby.ru/'

    def find(self, args):
        """
        Ищет необходимый элемент по селектору в формате find("BY.XPATH","//div[@class="result-text"]/a") / find("BY.ID","send-form-btn")
        :param args: BasePage object
        :return: webdriver object
        """
        return self.browser.find_element(*args)

    def open(self, url: Optional[str] = None) -> None:
        """
        Пытается открыть страницу, указанную в конструкторе объекта выше. При ошибке логгирует ошибку в консоль
        :param url: необходимый адрес для открытия
        :return: None
        """
        target_url = url or self.page_url
        try:
            with allure.step(f'Открытие страницы {target_url}'):
                self.browser.get(target_url)
        except WebDriverException as e:
            # Добавим шаг для отчёта Allure
            with allure.step(f'Unable to open {target_url}: {e}'):
                print(f'!Error, unable to open {target_url}: {e}')
                raise  # если не откроется, то я все