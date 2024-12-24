import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("http://www.deadlinkcity.com/")

driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME,"a")

count = 0

for i in allLinks:
   url = i.get_attribute('href')
   try:
    res = requests.head(url)
   except:
       None
   if res.status_code >= 400:
       print(url,'is broken link')
       count +=1
   else:
       print(url, "is valid link")

print("Total no of broken links:", count)