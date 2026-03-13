from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Index.html")

driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("swavimanbehera34@gmail.com")

driver.find_element(By.ID,"enterimg").click()

driver.find_element(By.XPATH,'//input[@placeholder="First Name"]').send_keys("Swaviman")

driver.find_element(By.XPATH,'//input[@placeholder="Last Name"]').send_keys("Behera")

time.sleep(3)

driver.find_element(By.XPATH,'//textarea[@ng-model="Adress"]').send_keys("IRC VILLAGE N6 143 NAYAPALLI, Bhubaneswar")

time.sleep(3)
# email adress
driver.find_element(By.XPATH,'//input[@type="email"]').send_keys("swavimanbehera34@gmail.com")

driver.find_element(By.XPATH,'//input[@ng-model="Phone"]').send_keys("7789024106")
time.sleep(4)
driver.close()