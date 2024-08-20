# #
# # 1.simple alert
# # 2.confirmation alert
# # 3.authentication alert
# # 4.file upload popup
# import time
#
# #simple alert
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','//button[text()="Alert"]').click()
# time.sleep(3)
#
# alert_obj=driver.switch_to.alert  #switching the control to chrome,here alert is property
# alert_obj.accept()
# time.sleep(3)
#
# driver.find_element('xpath','//button[text()="Confirm Box"]').click()
# time.sleep(3)
#
# alert_obj.dismiss()
# time.sleep(3)
#
#
#
# # #authentication pop up
# #as soon as we launch the webpage ,we get a pop up to give the username and password
# #since its pop up we cannot inspect
# #https:username:password@url
#
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#
# time.sleep(3)

#--------------------------------------------------------------
import xlrd
import time
from selenium import webdriver



driver=webdriver.Chrome()
driver.get("https://www.foundit.in/")
time.sleep(3)
path=r"C:\Users\admggnlptl\Desktop\Selenium_1\Files\example.xlsx"
driver.find_element('xpath','//div[@class="content"]').sendkeys(path)
time.sleep(4)
