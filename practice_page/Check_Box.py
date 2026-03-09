from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver  =   webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# check = driver.find_element(By.ID, "checkBoxOption1")

"""check.click()

time.sleep(2)

check.click()

time.sleep(5)"""

#with the help of actionchain

"""action = ActionChains(driver)

action.double_click(check).perform()

time.sleep(5)"""

#Multiple check box click method

multi_clcik = driver.find_elements(By.XPATH, "//div[@id='checkbox-example']//label/input")
#//input[@type='checkbox']   //div[@id='checkbox-example']//input[@type='checkbox']

for i in multi_clcik:
    i.click()

time.sleep(5)






driver.close()