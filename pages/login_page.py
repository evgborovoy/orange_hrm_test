from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Input login")
    def input_login(self, login):
        self.input_value(self.USERNAME_FIELD, login)

    @allure.step("Input password")
    def input_password(self, password):
        self.input_value(self.PASSWORD_FIELD, password)

    @allure.step("Click 'Login' button")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
