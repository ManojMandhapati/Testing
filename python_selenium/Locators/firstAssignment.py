# Test case
# ------------------
# 1. Open web browser (ch,ff,ex)
# 2. Open url https://admin-demo.nopcommerce.com/login
# 3. Provide Email (admin@yourstore.com)
# 4. Provide password (admin)
# 5. Click on login
# 6. Capture title of the Dashboard page (Actual Title)
# 7. Verify title of the page : Dashboard / nopCommerce administration (expected)
# 8. Close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= service)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()

import pickle

# Save cookies
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

# Load cookies
for cookie in pickle.load(open("cookies.pkl", "rb")):
    driver.add_cookie(cookie)
driver.refresh()

WebDriverWait(driver, 30).until(EC.title_is("Dashboard / nopCommerce administration"))

actualTitle = driver.title
exptitle = "Dashboard / nopCommerce administration"

if actualTitle == exptitle:
    print("test case passed")
else:
    print("test case failed")

print("Actual title:", driver.title)


driver.close()