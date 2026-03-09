from selenium import webdriver
from selenium.webdriver.common.by import By
import time

vivek=webdriver.Chrome()

vivek.get("https://testautomationpractice.blogspot.com/")
vivek.maximize_window()

time.sleep(4)

vivek.find_element(By.XPATH,"//input[@placeholder='Enter Name']").send_keys("jay shree ram")

time.sleep(6)




vivek.quit()
