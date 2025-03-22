from base.base_page import BasePage
from base.side_bar import SideBar
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class MyInfoPage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE

    # Personal details
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    PD_SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.side_bar = SideBar(driver)

    def change_first_name(self, value):
        with allure.step(f"Change first name on '{value}'"):
            self.input_value(self.FIRST_NAME_FIELD, value)

    def change_middle_name(self, value):
        with allure.step(f"Change middle name on '{value}'"):
            self.input_value(self.MIDDLE_NAME_FIELD, value)

    def change_last_name(self, value):
        with allure.step(f"Change last name on '{value}'"):
            self.input_value(self.LAST_NAME_FIELD, value)

    @allure.step("Click 'Save' button")
    def save_pd_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.PD_SAVE_BUTTON)).click()

    @allure.step("Changes was saved successfully")
    def is_field_changed(self, field_locator, value):
        self.wait.until(EC.text_to_be_present_in_element_value(field_locator, value))

    def is_first_name_changed(self, value):
        self.is_field_changed(self.FIRST_NAME_FIELD, value)

    def is_middle_name_changed(self, value):
        self.is_field_changed(self.MIDDLE_NAME_FIELD, value)

    def is_last_name_changed(self, value):
        self.is_field_changed(self.LAST_NAME_FIELD, value)
