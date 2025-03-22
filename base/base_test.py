import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage
from config.data import Data


class BaseTest:
    dashboard_page: DashboardPage
    login_page: LoginPage
    my_info_page: MyInfoPage

    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.my_info_page = MyInfoPage(driver)
