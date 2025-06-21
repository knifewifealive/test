import allure

from conftest import browser
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any

"""
Найти баннер Тензор, кликнуть по нему
Проверить, что определился ваш регион (в нашем примере
Ярославская обл.) и есть список партнеров.
"""

tensor_banner_link = (By.CSS_SELECTOR, '#contacts_clients a.sbisru-Contacts__logo-tensor.mb-12')
change_rg_link_button = (By.CSS_SELECTOR, '.sbisru-Contacts__relative span.sbis_ru-Region-Chooser__text.sbis_ru-link')
title = (By.TAG_NAME, 'title')
# Сделать уникальный или индекс
partner_selector = (By.CSS_SELECTOR, '.controls-ListView__itemContent')
rg_choice_panel = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel')
rg_41_selector = (By.XPATH, '//span[@title="Камчатский край"]')

class Contacts(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://saby.ru/contacts/77-moskva?tab=clients
        :param browser:
        """
        super().__init__(browser)
        self.page_url = 'https://saby.ru/contacts/77-moskva?tab=clients'

    @property
    def tensor_banner_link(self) -> Any:
        return self.find(tensor_banner_link)

    def tensor_banner_link_click(self) -> Any:
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(tensor_banner_link)).click()




    @property
    def tensor_banner_is_displayed(self) -> bool:
        return self.find(tensor_banner_link).is_displayed()


    def contacts_section_change_rg_button_link(self) -> str:
        return self.find(change_rg_link_button)

    @property
    def contacts_section_change_rg_button_link_is_displayed(self) -> bool:
        return self.find(change_rg_link_button).is_displayed()

    @property
    def contacts_section_rg_is_correct(self,browser):
        partners_list = self.find_all(partner_selector)
        page_title = self.find(title).text
        rg_button_change_text = self.contacts_section_change_rg_button_link
        print(len(partners_list) > 0,page_title,rg_button_change_text)
        return True if (len(partners_list) > 0) and (page_title.__contains__('Москва')) and (rg_button_change_text.__contains__('Москва')) else False

    def change_rg(self, rg = 41):
        self.contacts_section_change_rg_button_link().click()
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(rg_choice_panel)
        )
        self.find(rg_41_selector).click()
        partners_list = self.find_all(partner_selector)
        page_title = self.find(title).text
        rg_button_change_text = self.contacts_section_change_rg_button_link().text
        print(len(partners_list) > 0, page_title, rg_button_change_text)
        return True if (len(partners_list) > 0) and (page_title.__contains__('Москва')) and (
            rg_button_change_text.__contains__('Москва')) else False

