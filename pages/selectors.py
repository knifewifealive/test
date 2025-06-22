from selenium.webdriver.common.by import By


class BasePageSelectors:
    contact_button_to_pop_up = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu.js-ContactsMenu')
    more_offices_in_regions_link = (By.CSS_SELECTOR,
                                    '.sbisru-Header-ContactsMenu__items > .sbisru-link.sbis_ru-link > span')
    download_page_link = (By.XPATH, '//li/a[@href=\'/download\']')


class ContactsPageSelectors:
    tensor_banner_link = (By.CSS_SELECTOR, '#contacts_clients a.sbisru-Contacts__logo-tensor.mb-12')
    change_rg_link_button = (By.CSS_SELECTOR,
                             '.sbisru-Contacts__relative span.sbis_ru-Region-Chooser__text.sbis_ru-link')
    title = (By.TAG_NAME, 'title')
    # Сделать уникальный или индекс
    partner_selector = (By.CSS_SELECTOR, '.controls-ListView__itemContent')
    rg_choice_panel = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel')
    rg_41_selector = (By.XPATH, '//*[@class="sbis_ru-Region-Panel__item"][41]/span')


class TensorPageSelectors:
    power_in_people_block_selector = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
    get_more_info_link_selector = (By.CSS_SELECTOR,
                                   '.tensor_ru-Index__block4-bg a.tensor_ru-link.tensor_ru-Index__link')


class TensorAboutPageSelectors:
    work_block_selector = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .s-Grid-container')
    imgs_in_work_block_selector = (By.CSS_SELECTOR, 'img.tensor_ru-About__block3-image')


class DownloadPageSelectors:
    download_link = (By.XPATH, '//a[@href="https://update.saby.ru/SabyDesktop/master/win32/saby-setup-web.exe"]')
