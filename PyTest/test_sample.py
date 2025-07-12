from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


class TestSample():
        @pytest.fixture()
        def test_setup(self):
                global driver
                options = Options()
                options.add_experimental_option("detach", True)
                driver = webdriver.Chrome(service=ChromeService(
                        ChromeDriverManager().install()), options=options)

                driver.maximize_window()

                yield
                driver.close()
                driver.quit()
                print('Test Completed!')


        def test_login(self, test_setup):
                driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
                username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
                username.send_keys('Admin')

                password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
                password.send_keys('admin123')

                submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.orangehrm-login-button[type="submit"]')))
                submit.click()
                x = driver.title
                assert x == 'OrangeHRM'

        # def test_teardown():
        #         driver.close()
        #         driver.quit()
        #         print('Test Completed!')