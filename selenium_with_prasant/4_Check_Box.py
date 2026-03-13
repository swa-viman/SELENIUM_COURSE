from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Index.html")

driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("swavimanbehera34@gmail.com")

driver.find_element(By.ID,"enterimg").click()
time.sleep(3)

driver.find_element(By.XPATH,'//input[@value="Cricket"]').click()
driver.find_element(By.XPATH,'//input[@value="Movies"]').click()

time.sleep(3)
driver.close()