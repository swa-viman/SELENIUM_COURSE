from selenium import webdriver
from selenium.webdriver.common.by import By
import time

jiban=webdriver.Chrome()

jiban.get("https://www.google.com/?olud&zx=1773049136276&no_sw_cr=1")

jiban.maximize_window()
time.sleep(3)

jiban.find_element(By.PARTIAL_LINK_TEXT,"How").click()

jiban.find_element(By.XPATH,"")

time.sleep(4)

jiban.close()