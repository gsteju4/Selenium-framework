import time
from selenium import webdriver
driver=webdriver.Chrome()
# fdriver=webdriver.Firefox()

##launch the url
driver.get("https://www.gmail.com/")

##maximize the window
driver.maximize_window()

time.sleep(2)

##minimize window
driver.minimize_window()

##print title
print(driver.title)

# #current url
print(driver.current_url)
#
# driver.