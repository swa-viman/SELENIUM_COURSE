from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v143.fed_cm import click_dialog_button

swavi=webdriver.Chrome()

swavi.get("https://testautomationpractice.blogspot.com/")
swavi.maximize_window()

time.sleep(3)

swavi.find_element(By.XPATH,'//input[@value="female"]').click()

time.sleep(4)
swavi.quit()