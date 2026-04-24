from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace with your AWS EC2 URL
URL = "http://13.60.242.207"

driver = webdriver.Chrome()

driver.get(URL)

time.sleep(3)

# Find search box
search_box = driver.find_element(By.CLASS_NAME, "input-box")

search_box.send_keys("Mumbai")

time.sleep(2)

# Click search button
button = driver.find_element(By.ID, "searchBtn")
button.click()

time.sleep(5)

print("Test Completed Successfully")

driver.quit()