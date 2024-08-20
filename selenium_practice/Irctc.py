import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


opts=webdriver.ChromeOptions()
opts.add_argument("disable  notifications")

driver=webdriver.Chrome(options=opts)
action_obj=ActionChains(driver)

driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

driver.find_element('xpath','//input[@class="ng-tns-c57-8 ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted"]').send_keys("KSR BENGALURU-SBC")
time.sleep(3)
driver.find_element('xpath','(//input[@role="searchbox"])[2]').send_keys("DAVANGERE - DVG ")
time.sleep(3)
# driver.find_element('xpath','//li[text()="KSR BENGALURU-SBC"]').click()
# time.sleep(3)

date=driver.find_element('xpath','(//input[@type="text"])[3]')
action_obj.key_down(Keys.CONTROL).perform()
action_obj.send_keys('A').perform()
action_obj.send_keys("06/09/2023")
action_obj.key_up(Keys.CONTROL).perform()
time.sleep(3)

claslist=driver.find_element('xpath','(//div[@role="button"])[1]')

select_obj=Select(classlist)