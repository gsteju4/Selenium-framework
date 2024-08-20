from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

wait_=WebDriverWait(driver,30)
element=driver.find_element('xpath','//a[text()="Login"]')
wait_.until(expected_conditions.visibility_of(element))

# driver.find_element('xpath','//input[2name="fname"]').send_keys("Tom")