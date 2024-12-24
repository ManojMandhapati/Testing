from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

#is_displayed() & is_enabled()

searchBox = driver.find_element(By.XPATH,"//input[contains(@id,'small')]")
print("Display status: ",searchBox.is_displayed())
print("Enabled status: ",searchBox.is_enabled())


#is_selected() - for radio buttons and check boxes

rdMale = driver.find_element(By.XPATH, " //input[@id = 'gender-male']")
rdFemale = driver.find_element(By.XPATH, "//input[@id = 'gender-female']")

print("Default radio button status: ")
print(rdMale.is_selected()) #False
print(rdFemale.is_selected()) #False

rdMale.click() #select male radio button
print("\nAfter selecting male radio button:  ")
print("Male raido button status is:",rdMale.is_selected()) #True
print(rdFemale.is_selected()) #False

rdFemale.click()
print("\nAfter selecting female radio button:  ")

print(rdMale.is_selected()) #False
print(rdFemale.is_selected()) #True





driver.quit()


