from base.base_page import BasePage
from base.side_bar import SideBar
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.side_bar = SideBar(driver)
