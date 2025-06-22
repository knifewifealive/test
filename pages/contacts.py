from pages.base_page import BasePage
from pages.selectors import ContactsPageSelectors
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any

"""
Найти баннер Тензор, кликнуть по нему
Проверить, что определился ваш регион (в нашем примере
Ярославская обл.) и есть список партнеров.
"""


class Contacts(BasePage):
    def __init__(self, browser):
        """
        Метод конструктор для страницы https://saby.ru/contacts/77-moskva?tab=clients
        :param browser:
        """
        super().__init__(browser)
        self.page_url = 'https://saby.ru/contacts/77-moskva?tab=clients'
        self.browser = browser

    def tensor_banner_link(self, browser) -> Any:
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ContactsPageSelectors.tensor_banner_link)
        )

    def tensor_banner_link_click(self, browser) -> Any:
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ContactsPageSelectors.tensor_banner_link)).click()

    def tensor_banner_is_displayed(self, browser) -> bool:
        return self.tensor_banner_link(browser).is_displayed()

    def contacts_section_change_rg_button_link(self, browser):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ContactsPageSelectors.change_rg_link_button)
        )

    def contacts_section_change_rg_button_link_is_displayed(self, browser) -> bool:
        return self.contacts_section_change_rg_button_link(browser).is_displayed()

    def contacts_section_rg_is_correct(self, browser, region="Москва"):
        partners_list = self.find_all(ContactsPageSelectors.partner_selector)
        page_title = browser.title
        rg_button_change_text = self.contacts_section_change_rg_button_link(browser).text

        # Отладочный вывод:
        print("⏺ Проверка региона:")
        print(f"  ▶ Ожидаемый регион: {region}")
        print(f"  ▶ Кол-во партнёров: {len(partners_list)}")
        print(f"  ▶ Заголовок страницы: {page_title}")
        print(f"  ▶ Надпись на кнопке смены региона: {rg_button_change_text}")

        return (len(partners_list) > 0) and (region in page_title) and (region in rg_button_change_text)

    def change_rg(self, browser, rg_name="Камчатский край"):
        self.contacts_section_change_rg_button_link(browser=self.browser).click()

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ContactsPageSelectors.rg_choice_panel)
        )

        rg_to_change = self.find(ContactsPageSelectors.rg_41_selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", rg_to_change)
        self.browser.execute_script("arguments[0].click()", rg_to_change)

        # Ждём смену текста региона
        WebDriverWait(self.browser, 10).until(
            lambda d: rg_name in self.contacts_section_change_rg_button_link(d).text
        )

        return self.contacts_section_rg_is_correct(browser, rg_name) and browser.current_url.__contains__('41')
