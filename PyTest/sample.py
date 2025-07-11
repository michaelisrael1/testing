from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--no-sandbox')
options.add_experimental_option("detach", True)
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=options)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')