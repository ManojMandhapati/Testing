from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

servObj = servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("https://orangehrm.com/en/book-a-free-demo")

driver.maximize_window()
#time.sleep(15)
#countryDrop = driver.find_element(By.XPATH,"//select[@name='country_id']")
drpCountry = Select(driver.find_element(By.XPATH,"//select[@id = 'Form_getForm_Country']"))

#Select option from the dropdown
#drpCountry.select_by_visible_text("India")
#drpCountry.select_by_value('Hong Kong')
# drpCountry.select_by_value("10")
# drpCountry.select_by_index()

#Capture all the options and print them
# allOptions = drpCountry.options
# print('Total no of options: ',len(allOptions))
#
# for i in allOptions:
#     print(i.text)
# Select option form dropdown without using built-in method
# for i in allOptions:
#     if i.text == "India":
#         i.click()
#         break

allOpt = driver.find_elements(By.XPATH,"//*[@id='Form_getForm_Country']/option")
print(len(allOpt))

time.sleep(5)

