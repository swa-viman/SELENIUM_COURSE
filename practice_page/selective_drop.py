from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

happy_demand =driver.find_element(By.ID, "dropdown-class-example")
happy_demand.click()

select_option = Select(driver.find_element(By.ID, "dropdown-class-example"))

select_option.select_by_index(2)
time.sleep(2)
select_option.select_by_value('option3')
time.sleep(2)
select_option.select_by_visible_text('Option1')
time.sleep(2)



time.sleep(5)


driver.close()

