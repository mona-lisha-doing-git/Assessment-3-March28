from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Launching ShoppersStack website
driver.implicitly_wait(15)
driver.get("https://www.shoppersstack.com/")
driver.maximize_window()
