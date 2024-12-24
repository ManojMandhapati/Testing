import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

#Clcik on the link
#driver.find_element(By.LINK_TEXT,"Digital downloads ").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#Find no of links in a page
# links = driver.find_elements(By.TAG_NAME,'a')
# links = driver.find_elements(By.XPATH,"//a")
# print("Total no of links:",len(links))
#
# #Print all the link names
# for link in links:
#     print(link.text)





time.sleep(5)