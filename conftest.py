import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(autouse=True, scope="function")
def driver(request):
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options, service=service)
    request.cls.driver = driver
    yield driver
    driver.quit()
