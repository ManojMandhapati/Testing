from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
servObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = servObj)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']"))
).click()
# driver.switch_to.frame("frame_name_or_id")
# driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()



#driver.close()
driver.quit()



