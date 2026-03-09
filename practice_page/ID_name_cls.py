from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drivewer = webdriver.Chrome()

drivewer.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(3)

drivewer.find_element(By.ID, "name").send_keys("swaviman")


drivewer.close()