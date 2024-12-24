from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("https://admin-demo.nopcommerce.com/login")

driver.maximize_window()

emailBox = driver.find_element(By.XPATH,"//input[@id='Email']")
emailBox.clear()
emailBox.send_keys('abc@gmail.com')
print("result of text: ",emailBox.text)
print("result of get_attribute(): ",emailBox.get_attribute('value'))


button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print(button.text)
print(button.get_attribute('type'))
















time.sleep(5)