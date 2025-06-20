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

contact_button_to_pop_up = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu.js-ContactsMenu')
more_offices_in_regions_link = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items > .sbisru-link.sbis_ru-link > span')


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

    def find_all(self, args):
        """
        Ищет необходимые элементы по селектору в формате find("BY.XPATH","//div[@class="result-text"]/a") / find("BY.ID","send-form-btn")
        :param args: BasePage object
        :return: webdriver object
        """
        return self.browser.find_elements(*args)

    def open(self, url: Optional[str] = None) -> None:
        """
        Пытается открыть страницу, указанную в конструкторе объекта выше. При ошибке логгирует ошибку в консоль
        :param url: необходимый адрес для открытия
        :return: None
        """
        target_url = url or self.page_url
        try:
            with allure.step(f'Open page: {target_url}'):
                self.browser.get(target_url)
        except WebDriverException as e:
            # Добавим шаг для отчёта Allure
            with allure.step(f'Unable to open {target_url}: {e}'):
                print(f'!Error, unable to open {target_url}: {e}')
                raise  # если не откроется, то я все


    @property
    def contacts_button_link(self) -> Any:
        """

        :return: #Веб-драйвер объект кнопки-ссылки на поп-ап контактов на главной
        """
        return self.find(contact_button_to_pop_up)

    #Проверка на существование кнопки-ссылки в хедере
    @property
    def contacts_button_is_displayed(self: Any) -> bool:
        """

        :return: true if button exists, false if not
        """

        with allure.step('Check that contacts button-link is displayed'):
            return self.contacts_button_link.is_displayed()

    # Клик по кнопке-ссылке в хедере для открытия поп-апа
    def contacts_button_click(self: Any):
        self.contacts_button_link.click()

    # Возвращает вебдрайвер элемент ссылки в хедере "Еще N офисов в регионе" https://saby.ru/contacts
    @property
    def find_region_link(self) -> Any:
        self.contacts_button_click()
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(more_offices_in_regions_link)
        )

    @property
    def region_link_id_displayed(self) -> bool:
        """

        :return: true if displays, false if not
        """
        return self.find_region_link().is_displayed()

    def region_link_click(self) -> None:
        """
        Clicks on region link in header
        """
        self.find_region_link().click()