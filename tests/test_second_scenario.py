import allure
from pages.contacts import Contacts


@allure.feature('Contacts page, correct user region displayed, able to switch it')
@allure.story('UX')
def test_check_for_local_user_region(browser):
    contacts_page = Contacts(browser)
    contacts_page.open()

    with allure.step('Check that contacts button-link is displayed'):
        assert contacts_page.contacts_section_change_rg_button_link_is_displayed
    with allure.step('Check that rg is correct'):
        assert contacts_page.contacts_section_rg_is_correct(browser)

    with allure.step('Change rg for Kamchatskiy Kray'):
        assert contacts_page.change_rg(browser)
