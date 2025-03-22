import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Open {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def input_value(self, locator, value):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(Keys.COMMAND + "A")
        element.send_keys(Keys.BACKSPACE)
        element.clear()
        element.send_keys(value)
