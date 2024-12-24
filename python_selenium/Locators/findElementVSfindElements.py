from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

#find_element() - Returns single web element
# 1. Locator matching with single web element
# 2. pointing to multiple web elements
# 3. passing locator which is not available on webpage

# 1. Locator matching with single web element
# driver.maximize_window()
# element = driver.find_element(By.XPATH, "//input[@id = 'small-searchterms']")
# element.send_keys("Mobiles")
# driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
#
#time.sleep(5)

# 2. Locator matching with multiple web elements
# element = driver.find_element(By.XPATH,"//div[@class = 'footer']//a")
# print(element.text) # printing first link

# 3. passing locator which is not available then thorw NosuchElementException
# logElement = driver.find_element(By.LINK_TEXT, "Log")
# logElement.click()

#########################################################################################

#find_elements() - Returns multiple web elements
# 1. Locator matching with single web element
# element = driver.find_elements(By.XPATH,  "//input[@id = 'small-searchterms']")
# print(len(element)) #1
# print(element[0].text)
# element[0].send_keys('Samsung Series 9 NP900X4C Premium Ultrabook')

# 2. Locator matching with multiple web elements
# element = driver.find_elements(By.XPATH,"//div[@class = 'footer']//a")
# print(len(element)) # 23
# #print(element[5].text)
# for i in element:
#     print(i.text)

# 3. passing locator which is not available - ZERO
logElement = driver.find_elements(By.LINK_TEXT, "Log") #Not throw any exception
print("Elements returned: ",len(logElement))
#logElement.click()





