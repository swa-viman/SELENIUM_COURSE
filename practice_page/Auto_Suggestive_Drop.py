from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID, "autocomplete").send_keys("ind")

time.sleep(3)


all_options = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li/div")

for i in all_options:
    if i.text == "India":
        i.click()
        break

time.sleep(5)
driver.close()


















