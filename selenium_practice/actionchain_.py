import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# action_obj=ActionChains(driver)
# element=driver.find_element('xpath','//button[text()="Copy Text"]')
# action_obj.double_click(element).perform()
# time.sleep(6)

#-------------------------------------------------------------
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver=webdriver.Chrome()
#
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# act_obj=ActionChains(driver)
# element=driver.find_element('xpath','//a[@data-group="home-&-living"]')
# act_obj.move_to_element(element).perform()
# time.sleep(3)


#-------------------------------------------------------

#drag and drop

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver=webdriver.Chrome()
# act_obj=ActionChains(driver)
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window()
# source=driver.find_element('xpath','(//div[text()="Washington"])[2]')
# target=driver.find_element('xpath','//div[text()="United States"]')
# act_obj.drag_and_drop(source,target).perform()
# time.sleep(3)
# for i in range(1,8):
#     src=driver.find_element('xpath',f'//div[@id="box{i}"]')
#     target=driver.find_element('xpath',f'//div[@id="box10{i}"]')
#     act_obj.drag_and_drop(src,target).perform()
#     time.sleep(3)

#----------------------------------------------
#scrolling page
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
action_obj=ActionChains(driver)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(3)

action_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(3)
action_obj.send_keys(Keys.PAGE_UP).perform()
time.sleep(3)
action_obj.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)
action_obj.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)

element=driver.find_element('xpath','//a[text()="Search"]')
action_obj.move_to_element(element)
time.sleep(3)

action_obj.key_down(Keys.CONTROL).perform()
action_obj.send_keys('A').perform()
action_obj.key_up(Keys.CONTROL).perform()
time.sleep(3)

