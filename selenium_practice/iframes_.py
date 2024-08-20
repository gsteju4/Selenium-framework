import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/admggnlptl/Downloads/iframe.html")
driver.maximize_window()
time.sleep(3)
#0 represents first fame in the webpage
driver.switch_to.frame('FR1')        #frame('attribute')
driver.find_element('xpath','//a[text()="Register"]').click()
time.sleep(3)

driver.switch_to.parent_frame()

driver.switch_to.frame('FR2')
driver.find_element('xpath','//a[text()="Home"]').click()
time.sleep(3)