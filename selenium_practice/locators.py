''
# id
# name


# #id
# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# time.sleep(2)
#
# search=driver.find_element('class name','desktop-searchBar')
# search.send_keys('Dresses for girls')
# time.sleep(2)
#
# driver.find_element('class name','desktop-autoSuggest.desktop-showContent').click()
#

#--------------------------------------
# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://demo.actitime.com/login.do")
# driver.maximize_window()
# time.sleep(2)
#
#
# # user_name=driver.find_element('class name','textField')
# # user_name.send_keys('admin')
# driver.find_element('class name','textField').send_keys('admin')
# # password=driver.find_element('class name','textField.pwdfield')
# # password.send_keys('manager')
# driver.find_element('class name','textField.pwdfield').send_keys('manager')
# time.sleep(2)

#------------------------------------------------
# #css selector
# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
#
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(2)
# # driver.find_element('css selector', 'a[class="ico-register"]').click()
# # time.sleep(2)
#
# driver.find_element('css selector','a[class="ico-login"]').click()
# time.sleep(3)
#
# driver.find_element('css selector','input[class="email"]').send_keys('tejaswini052@gmail.com')
# # time.sleep(2)
# driver.find_element('css selector','input[id="gender-female"]').click()
# driver.find_element('css selector','input[class="text-box single-line"]').send_keys('Tejaswini')
# # driver.find_element('css selector','input[id="LastName"]').send_keys('GS')
# time.sleep(2)
# driver.find_element('css selector','input[id="Email"]').send_keys('tejaswini052@gmail.com')
# time.sleep(2)
# driver.find_element('css selector','input[name="Password"]').send_keys('1234567')
# time.sleep(2)
# driver.find_element('css selector','input[id="ConfirmPassword"]').send_keys('1234567')
#
# driver.find_element('css selector','input[id="register-button"]').click()
# time.sleep(2)

# time.sleep(2)


#------------------------------------
# # xpath
# import time
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath','//a[@class="ico-register"]').click()
#
# # driver.find_element('xpath','//a[@class="ico-login"]')
#
# time.sleep(3)
#
# driver.find_element('xpath,')
# driver.find_element('xpath','//input[@id="Email"]').send_keys("tejaswini052@gmail.com")
# time.sleep(2)




# #------------------------
# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
#
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','(//a[contains(text(),"Books")])[3]').click()
# time.sleep(5)





# #------------------------------------------
import time
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get("https://www.python.org/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','(//a[text()="Downloads"])[1]').click()
# time.sleep(3)
#
# driver.find_element('xpath','//a[text()="Python 3.9.18"]/../..//a[text()="Release Notes"]').click()
# time.sleep(3)

#wap to get the text of the elements present in the footer of demo web shop
#
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(2)
# result=driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
# for webelement in result:
#     print(webelement.text)


# #----------------------------------------
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
#
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys("nike")
# driver.find_element('xpath','//span[@class="myntraweb-sprite desktop-iconSearch sprites-search"]').click()
# result=driver.find_elements('xpath','//ul[@class="results-base"]//h4')
# price=driver.find_elements('xpath','//ul[@class="results-base"]//span')
# d={}
#
# for i,j in zip(result,price):
#     d[i.text]=(j.text)
# print(d)



#----------------------------------
#print all the link texts present in python.org"
#
# from selenium import webdriver
# driver=webdriver.Chrome()
#
# driver.get("https://www.python.org/")
# driver.maximize_window()
# res=driver.find_elements('tag name','a')
# for ele in res:
#     print(ele.text)

#------------------------------
#click on downloads in demo.html

#-----------------------
#wap to get the text of the elements present in th eleft navigation bar of demowebshop"
#
#
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# res=driver.find_elements('xpath','//div[@class="leftside-3"]//a')
# for webelement in res:
#     print(webelement.text)
#----------------------------------------------------------------


#list box
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome()
# driver.get(r"file:///C:/Users/admggnlptl/Desktop/demo.html")
# driver.maximize_window()
# time.sleep(3)
#
#
# list_box=driver.find_element('xpath','//select[@id="standard_cars"]')
# select_obj=Select(list_box)
# carlist=driver.find_elements('xpath','//select[@id="standard_cars"]//option')
# list_=[]
# for webelement in carlist:
#    list_.append(webelement.text)
# for ele in list_:
#     select_obj.select_by_visible_text(ele)
#     time.sleep(1)
# time.sleep(3)

# drop=driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj=Select(drop)
# cars=driver.find_elements('xpath','//select[@id="multiple_cars"]//option')
# car_list=[]
# for ele in cars:
#     car_list.append(ele.text)
# print(car_list)
#
# for element in car_list:
#     select_obj.select_by_visible_text(element)
#     time.sleep(1)
# time.sleep(3)
#--------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640")
# driver.maximize_window()
# time.sleep(3)
# day=driver.find_element('xpath','//select[@id="day"]')
# sel_obj=Select(day)
# daylist=driver.find_elements('xpath','//select[@id="day"]//option')
# daylist_=[]
# for ele in daylist:
#     daylist_.append(ele.text)
# for item in daylist_:
#     if item=='13':
#         sel_obj.select_by_visible_text("13")
#         time.sleep(3)
# time.sleep(3)
#
#
# month=driver.find_element('xpath','//select[@id="month"]')
# sel_obj2=Select(month)
# monthlist=driver.find_elements('xpath','//select[@id="month"]//option')
# month_list=[]
# for i in monthlist:
#     month_list.append(i.text)
# for item in month_list:
#     sel_obj2.select_by_visible_text("Jan")
#     time.sleep(3)
# time.sleep(3)
#
# year=driver.find_element('xpath','//select[@id="year"]')
# sel_obj3=Select(year)
# yearlist=driver.find_elements('xpath','//select[@id="year"]//option')
# year_list=[]
# for i in yearlist:
#     year_list.append(i.text)
# for item in year_list:
#     sel_obj3.select_by_visible_text("1989")
#     time.sleep(3)
# time.sleep(3)

#-----------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element('xpath','(//a[contains(text(),"Books")])[3]').click()
# sort=driver.find_element('xpath','//select[@id="products-orderby"]')
#
# sel_obj=Select(sort)
# sortlist=driver.find_elements('xpath','//select[@id="products-orderby"]//option')
# sel_obj.select_by_visible_text("Name: A to Z")
# time.sleep(3)
# driver.find_element('xpath','(//input[@value="Add to cart"])[2]').click()
#
# time.sleep(3)

