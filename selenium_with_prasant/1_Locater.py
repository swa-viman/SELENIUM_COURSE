from selenium import webdriver
from selenium.webdriver.common.by import By
import time

locate=webdriver.Chrome()

locate.get("https://demo.automationtesting.in/Index.html")

locate.maximize_window()

locate.find_element(By.ID,"email").send_keys("swavimanbehera34@gmail.com")

locate.find_element(By.ID,"enterimg").click()

time.sleep(3)

locate.close()
