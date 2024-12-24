from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service= serObj)
#driver.implicitly_wait(10) #implecit wait
driver.get("https://www.google.com/")

driver.maximize_window()
driver.implicitly_wait(10)

searchBox = driver.find_element(By.NAME,"q")
#time.sleep(5)
searchBox.send_keys("Selenium")
searchBox.submit()
#time.sleep(5)
driver.find_element(By.XPATH,"//h3[text() = 'Selenium']").click()

driver.quit()