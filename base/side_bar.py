from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


class SideBar:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    _ADMIN_BUTTON = ("xpath", "//span[text()='Admin']")
    _PIM_BUTTON = ("xpath", "//span[text()='PIM']")
    _LEAVE_BUTTON = ("xpath", "//span[text()='Leave']")
    _TIME_BUTTON = ("xpath", "//span[text()='Time']")
    _RECRUITMENT_BUTTON = ("xpath", "//span[text()='Recruitment']")
    _MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")
    _PERFORMANCE_BUTTON = ("xpath", "//span[text()='Performance']")
    _DASHBOARD_BUTTON = ("xpath", "//span[text()='Dashboard']")
    _DIRECTORY_BUTTON = ("xpath", "//span[text()='Directory']")
    _MAINTENANCE_BUTTON = ("xpath", "//span[text()='Maintenance']")
    _CLAIM_BUTTON = ("xpath", "//span[text()='Claim']")
    _BUZZ_BUTTON = ("xpath", "//span[text()='Buzz']")

    def click_admin_button(self):
        self.wait.until(EC.element_to_be_clickable(self._ADMIN_BUTTON)).click()

    def click_pim_button(self):
        self.wait.until(EC.element_to_be_clickable(self._PIM_BUTTON)).click()

    def click_leave_button(self):
        self.wait.until(EC.element_to_be_clickable(self._LEAVE_BUTTON)).click()

    def click_time_button(self):
        self.wait.until(EC.element_to_be_clickable(self._TIME_BUTTON)).click()

    def click_recruitment_button(self):
        self.wait.until(EC.element_to_be_clickable(self._RECRUITMENT_BUTTON)).click()

    @allure.step("Click on 'My Info' link")
    def click_my_info_button(self):
        self.wait.until(EC.element_to_be_clickable(self._MY_INFO_BUTTON)).click()

    def click_performance_button(self):
        self.wait.until(EC.element_to_be_clickable(self._PERFORMANCE_BUTTON)).click()

    def click_dashboard_button(self):
        self.wait.until(EC.element_to_be_clickable(self._DASHBOARD_BUTTON)).click()

    def click_directory_button(self):
        self.wait.until(EC.element_to_be_clickable(self._DIRECTORY_BUTTON)).click()

    def click_maintenance_button(self):
        self.wait.until(EC.element_to_be_clickable(self._MAINTENANCE_BUTTON)).click()

    def click_claim_button(self):
        self.wait.until(EC.element_to_be_clickable(self._CLAIM_BUTTON)).click()

    def click_buzz_button(self):
        self.wait.until(EC.element_to_be_clickable(self._BUZZ_BUTTON)).click()
