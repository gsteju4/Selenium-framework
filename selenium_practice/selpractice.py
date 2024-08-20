import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver=Chrome(options = o )
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(5)
action_obj=ActionChains(driver)
action_obj.send_keys(Keys.PAGE_DOWN).perform()
action_obj.send_keys(Keys.PAGE_UP).perform()

driver.close()