import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize undetected ChromeDriver
driver = uc.Chrome()

# Open login page
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()

# Wait until the title updates
WebDriverWait(driver, 10).until(EC.title_is("Dashboard / nopCommerce administration"))

actualTitle = driver.title
exptitle = "Dashboard / nopCommerce administration"

if actualTitle == exptitle:
    print("test case passed")
else:
    print("test case failed")

print("Actual title:", driver.title)
driver.close()
