"""
Automate Product Selection and Delivery Check on ShoppersStack

Automate the process of selecting a product category and verifying delivery availability using a pincode.

Perform the following steps:
- Launch the browser and open the ShoppersStack website
- Maximize the browser window
- Click on the **"APPLE"** product category
- Locate the delivery input field and enter the pincode
- Click on the **"Check"** button
"""
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

wait = WebDriverWait(driver, 15)

# Clicking on the apple category product
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='featuredProducts_footerLeft__PmkNa']//span[text()='APPLE']"))).click()

# Locating the delivery input field and enter the pincode
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='Check Delivery']"))).send_keys("302022")

# Clicking on the "Check" button using explicit wait
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='Check']"))).click()

sleep(5)
driver.quit()
