"""
Automate Myntra Product Selection

Automate the process of navigating categories, selecting a product, applying filters, sorting products and adding to bag.

Perform the following steps:
- Launch the browser and open the Myntra website
- Maximize the browser window
- Hover over the **Genz** category
- Click on **"Jackets Under ₹899"**
- Select any 2 filter under the product filters (e.g., brand, size, or color)
- Click on the **Sort By** 'Popularity'
- Click on any one product
- Select size (if mentioned)
- Add to bag
"""

from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Launching Myntra website
driver.implicitly_wait(15)
driver.get("https://www.myntra.com/")
driver.maximize_window()

action = ActionChains(driver)

# Hovering Genz Category
action.move_to_element(driver.find_element(By.XPATH, "//a[text()='Genz']")).perform()

wait = WebDriverWait(driver, 10)

# Clicking on **"Jackets Under ₹899"**
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Jackets Under ₹899']"))).click()

# Selecting 2 filters under the product filters - brand and color
wait.until(EC.visibility_of_element_located((By.XPATH, "(//ul[@class='brand-list']//input[@value='QIOA']/following::div)[1]"))).click()
sleep(2)

wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='vertical-filters-filters'])[1]//span[@data-colorhex='black']/following::div"))).click()
sleep(2)

# Clicking on the **Sort By** 'Popularity'
action.move_to_element(driver.find_element(By.XPATH, "//div[@class='sort-sortBy']")).perform()

wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Popularity']"))).click()
sleep(2)

# Clicking on any one product
wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='product-productMetaInfo'])[2]"))).click()
sleep(2)

# Clicking on one product, selecting size and adding to bag
driver.switch_to.window(driver.window_handles[1])

wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='size-buttons-size-button size-buttons-size-button-default'])[1]"))).click()
sleep(2)

wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='ADD TO BAG']"))).click()
sleep(2)

sleep(3)
driver.quit()
