import time
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.myntra.com/")
driver.maximize_window()
# action_obj=ActionChains(driver)

driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys("handbag")
time.sleep(3)
driver.find_element('xpath','//li[text()="Handbags Women"]').click()
time.sleep(3)
driver.find_element('xpath','//img[@title="Lino Perros Off-White Quilted Handheld Bag"]').click()
time.sleep(3)
handles=driver.window_handles
driver.switch_to.window(handles[1])

driver.find_element('xpath','//div[text()="ADD TO BAG"]').click()

time.sleep(3)
driver.switch_to.window(handles[0])
time.sleep(3)


driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys("puma")
time.sleep(3)
driver.find_element('xpath','//li[text()="Puma Bags"]').click()
time.sleep(3)
driver.find_element('xpath','//img[@title="Puma Unisex Black Phase Printed Backpack"]').click()

time.sleep(2)

driver.switch_to.window(handles[2])
driver.find_element('xpath','//div[text()="ADD TO BAG"]').click()
time.sleep(3)
driver.switch_to.window(handles[0])
time.sleep(2)