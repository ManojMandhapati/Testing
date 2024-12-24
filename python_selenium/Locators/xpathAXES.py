from http.cookiejar import debug

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serviceObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = serviceObj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
#Self
# txtMessage = driver.find_element(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/self::a").text
# print(txtMessage)

#Parent
# txtMsg = driver.find_element(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/parent::td").text
# print(txtMsg)

#Child
# childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Piramal Pharma')]//ancestor::tr/child::td")
# print(len(childs))
# for i in childs:
#     print(i.text)

# Ancestor
# ancestor = driver.find_element(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/ancestor::tr").text
# print(ancestor) #Piramal Pharma A 251.15 260.55 + 3.74 Buy  |  Sell

#Descendant
# descendant = driver.find_elements(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/ancestor::tr/descendant::*")
# print("Number of descendants: ",len(descendant))

#Following
# following = driver.find_elements(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/ancestor::tr/following::*")
# print("Number of following: ",len(following))

#Following-sibling
# followingSib = driver.find_elements(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/ancestor::tr/following-sibling::*")
# print("Number of following: ",len(followingSib))

#Preceding
# preceding = driver.find_elements(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/ancestor::tr/preceding::tr")
# print("Number of preceding: ",len(preceding))#14

#Preceding-sibling
# precedingSib = driver.find_elements(By.XPATH,"//a[contains(text(),'Piramal Pharma')]/ancestor::tr/preceding-sibling::tr")
# print("Number of preceding: ",len(precedingSib)) #13











