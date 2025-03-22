from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SideBar:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    ADMIN_BUTTON = ("xpath", "//span[text()='Admin']")
    PIM_BUTTON = ("xpath", "//span[text()='PIM']")
    LEAVE_BUTTON = ("xpath", "//span[text()='Leave']")
    TIME_BUTTON = ("xpath", "//span[text()='Time']")
    RECRUITMENT_BUTTON = ("xpath", "//span[text()='Recruitment']")
    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")
    PERFORMANCE_BUTTON = ("xpath", "//span[text()='Performance']")
    DASHBOARD_BUTTON = ("xpath", "//span[text()='Dashboard']")
    DIRECTORY_BUTTON = ("xpath", "//span[text()='Directory']")
    MAINTENANCE_BUTTON = ("xpath", "//span[text()='Maintenance']")
    CLAIM_BUTTON = ("xpath", "//span[text()='Claim']")
    BUZZ_BUTTON = ("xpath", "//span[text()='Buzz']")

    def click_admin_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADMIN_BUTTON)).click()

    def click_pim_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM_BUTTON)).click()

    def click_leave_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LEAVE_BUTTON)).click()

    def click_time_button(self):
        self.wait.until(EC.element_to_be_clickable(self.TIME_BUTTON)).click()

    def click_recruitment_button(self):
        self.wait.until(EC.element_to_be_clickable(self.RECRUITMENT_BUTTON)).click()

    def click_my_info_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

    def click_performance_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PERFORMANCE_BUTTON)).click()

    def click_dashboard_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DASHBOARD_BUTTON)).click()

    def click_directory_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DIRECTORY_BUTTON)).click()

    def click_maintenance_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MAINTENANCE_BUTTON)).click()

    def click_claim_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CLAIM_BUTTON)).click()

    def click_buzz_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUZZ_BUTTON)).click()
