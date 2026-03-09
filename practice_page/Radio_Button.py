from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()


#Single click method
"""click_radio_button = driver.find_element(By.XPATH,"//input[@value='radio1']").click()"""

#Multiple click method

"""all_radio_button = driver.find_elements(By.XPATH,"//input[@name='radioButton']")

for i in all_radio_button:
    i.click()

time.sleep(5)"""

#mo iccha anusaar click method

wait = WebDriverWait(driver, 5)

all_radio_button = driver.find_elements(By.XPATH,"//input[@name='radioButton']")

for happy in all_radio_button:
    wait.until(EC.element_to_be_clickable(happy))
    happy.click()
time.sleep(3)


driver.close()