from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("https://www.amazon.co.uk/")
driver.get("https://www.flipkart.com/")

driver.maximize_window()

driver.back() #amazon
driver.forward() #flipkart

driver.refresh()
time.sleep(5)

driver.quit()
