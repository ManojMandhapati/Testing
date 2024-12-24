from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= servObj)

driver.get('https://www.ironspider.ca/forms/checkradio.htm')
driver.maximize_window()

# Selecting specific checkbox
#driver.find_element(By.XPATH,"//input[@value = 'purple']").click()

#time.sleep(5)


#Select all the checkboxes

checkBoxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@value, 'e')]")
print(len(checkBoxes)) #6

#Approach 1

# for i in range(len(checkBoxes)):
#     checkBoxes[i].click()

#Approach 2

for checkBox in checkBoxes:
    checkBox.click()

#Select multiple checkboxes by choice

# for checkBox in checkBoxes:
#     color = checkBox.get_attribute('value')
#     if color == 'green' or color == 'red':
#         checkBox.click()

# Select last 2 checkboxes
#range((6-2),6)
#totalnofoelemenets -2 =startingIndex
# for i in range(len(checkBoxes)-2,len(checkBoxes)):
#     checkBoxes[i].click()

#Select first 2 checkboxes
# for i in range(len(checkBoxes)):
#     if i< 2:
#         checkBoxes[i].click()

#Clearing all the checkboxes
for checkBox in checkBoxes:
    if checkBox.is_selected():
        checkBox.click()







time.sleep(5)

driver.quit()