from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = serObj)

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title) # To get the title of the current webpage
print(driver.current_url) # To get the current webpage url
#driver.page_source

driver.quit()