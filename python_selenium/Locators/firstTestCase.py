# Test case
# ------------------
# 1. Open web browser (ch,ff,ex)
# 2. Open url https://opensource-demo.orangehrmlive.com/
# 3. Provide Email (Admin)
# 4. Provide password (admin123)
# 5. Click on login
# 6. Capture title of the Dashboard page (Actual Title)
# 7. Verify title of the page : Dashboard / nopCommerce administration (expected)
# 8. Close browser

# Webdriver is a python module which is available in Selenium.


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

# Correctly initialize the Service object
service = Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")

# Launch the Firefox browser
driver = webdriver.Edge(service=service)
##driver = webdriver.Edge()
driver.get("https://demo.applitools.com/")

# driver.find_element(By.Name,"username").send_keys("Admin")
# driver.find_element(By.ID, "password").send_keys("admin123")
# driver.find_element(By.ID,"submit").click()
#time.sleep(3)
# Locate and enter the username
driver.find_element(By.ID, "username").send_keys("admin")

# Locate and enter the password
driver.find_element(By.ID, "password").send_keys("admin")

# Locate and click the login button
driver.find_element(By.ID, "log-in").click()



actualTitle = driver.title
expTitle = "ACME demo app"

if actualTitle == expTitle:
    print("Login test passed")
else:
    print("login test failed")

driver.close()























#driver = webdriver.Firefox("C:\\Drivers\\geckodriver-v0.35.0-win-aarch64\\geckodriver.exe") #This will launch the browser
#driver.get("https://opensource-demo.orangehrmlive.com/")
# service = (executable_path = "C:\Drivers\geckodriver-v0.35.0-win-aarch64\geckodriver.exe")
# driver = webdriver.Firefox(service=service)
# driver.get("https://opensource-demo.orangehrmlive.com/")