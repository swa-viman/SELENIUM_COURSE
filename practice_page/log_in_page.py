from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/login/")

driver.maximize_window()

driver.find_element(By.NAME, "email").send_keys("swaviman")
driver.find_element(By.NAME, "pass").send_keys("swaviman@123")
driver.find_element(By.XPATH, "//div[@role='button']").click()

time.sleep(4)
driver.quit()