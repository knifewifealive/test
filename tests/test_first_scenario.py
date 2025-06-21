import allure
from pages.base_page import BasePage
from pages.contacts import Contacts
from pages.tensor import TensorPage
from pages.tensor_about import TensorAbout


@allure.feature('Main page, contacts button-link in header')
@allure.story('Existence')
def test_contacts_button_link_exist(browser):
    with allure.step('Open base page'):
        main_page = BasePage(browser)
        main_page.open()
    with allure.step('Check the link-button'):
        assert main_page.contacts_button_is_displayed


@allure.feature('Main page, contacts button-link in header')
@allure.story('Click')
def test_contacts_button_link_click(browser):
    with allure.step('Click the link-button'):
        main_page = BasePage(browser)
        main_page.open()
        assert main_page.contacts_button_click

@allure.feature('Main page, regions link in header after clicking on contacts button-link in header')
@allure.story('Existence')
def test_wait_for_regions_link(browser):
    main_page = BasePage(browser)
    main_page.open()
    with allure.step('Check for regions link in header after clicking on contacts button-link in header'):
        assert main_page.find_region_link

@allure.feature('Main page, regions link in header after clicking on contacts button-link in header')
@allure.story('Click')
def test_click_on_regions_link(browser):
    main_page = BasePage(browser)
    main_page.open()

    with allure.step('Click on regions link in header after clicking on contacts button-link in header'):
        assert main_page.find_region_link

@allure.feature('Main page, regions link in header after clicking on contacts button-link in header')
@allure.story('Correct URL')
def test_correct_url_on_regions_link(browser):
    main_page = BasePage(browser)
    main_page.open()
    main_page.find_region_link().click()

    with allure.step('Main page, check for correct regions link in header after clicking on contacts button-link in header'):
        browser.implicitly_wait(0.1)
        assert browser.current_url == 'https://saby.ru/contacts/77-moskva?tab=clients'

@allure.feature('Contacts moscow page, tensor link is displayed')
@allure.story('Existence')
def test_contacts_tensor_link_is_displayed(browser):
    with allure.step('Open contacts moscow page'):
        contacts_page = Contacts(browser)
        contacts_page.open()
    with allure.step('Check the tensor banner'):
        assert contacts_page.tensor_banner_is_displayed

@allure.feature('Contacts moscow page, tensor link contains correct url')
@allure.story('Correct URL')
def test_correct_url_on_regions_link(browser):
    contacts_page = Contacts(browser)
    contacts_page.open()
    url = contacts_page.tensor_banner_link().get_attribute('href')
    with allure.step('Contacts moscow page, tensor link contains correct url'):
        assert url == 'https://tensor.ru/'


@allure.feature('Tensor.ru page, block exists')
@allure.story('Existence')
def test_tensor_block_exists(browser):
    tensor_page = TensorPage(browser)
    tensor_page.open()
    with allure.step('Tensor.ru page, tensor block power in people exists'):
        assert tensor_page.tensor_block_exists

@allure.feature('Tensor.ru page, tensor_block_get_more_info_link contains correct url')
@allure.story('Correct URL')
def test_correct_url_on_regions_link(browser):
    tensor_page = TensorPage(browser)
    tensor_page.open()
    url = tensor_page.tensor_block_get_more_info_link
    with allure.step('Tensor.ru page, tensor get more info link contains correct url'):
        assert url == 'https://tensor.ru/about'

@allure.feature('Tensor.ru/about page, block exists')
@allure.story('Existence')
def test_tensor_block_exists(browser):
    tensor_about = TensorAbout(browser)
    tensor_about.open()
    with allure.step('Tensor.ru page, tensor block working exists'):
        assert tensor_about.work_block_exists

@allure.feature('Tensor.ru/about page, imgs have same width and height in working block')
@allure.story('UI')
def test_tensor_block_imgs_have_same_height_width(browser):
    tensor_about = TensorAbout(browser)
    tensor_about.open()
    with allure.step('Tensor.ru page, imgs have same width and height in working block'):
        assert tensor_about.work_block_containts_equal_imgs