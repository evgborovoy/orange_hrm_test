import allure

from base.base_test import BaseTest


@allure.feature("Profile info functionality")
class TestMyInfo(BaseTest):

    @allure.title("Change first name")
    @allure.severity("Critical")
    def test_first_name_in_my_info(self):
        self.login_page.open()
        self.login_page.input_login(self.data.LOGIN)
        self.login_page.input_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.side_bar.click_my_info_button()
        self.my_info_page.is_opened()
        first_name = "John"
        self.my_info_page.change_first_name(first_name)
        self.my_info_page.save_pd_changes()
        self.my_info_page.is_first_name_changed(first_name)
