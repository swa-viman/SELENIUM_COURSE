from selenium import webdriver
from selenium.webdriver.common.by import By
import time

locater=webdriver.Chrome()

locater.get("https://testautomationpractice.blogspot.com/")

locater.maximize_window()

time.sleep(4)

name=locater.find_element(By.ID,"name").send_keys("swaviman behera")

time.sleep(3)

email=locater.find_element(By.ID,"email").send_keys("swavimanbehera34@gmail.com")

time.sleep(3)

locater.close()