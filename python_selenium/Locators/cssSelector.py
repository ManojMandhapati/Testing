from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = serviceObj )

driver.get("https://www.facebook.com/")
driver.maximize_window()
##TAG and ID (tagname#valueofID)
# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys("test@gmail.com")
# driver.find_element(By.CSS_SELECTOR, '#email').send_keys("test@gmail.com")

#TAG and CLASS (tagname.ClassValue)
#driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys("test")

#TAG ATTRIBUTE (tagname[attribute = value])
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys()
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys()

# ATG CLASS ATTRIBUTE (tagname.valueofclass[attribute = value])
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys('test@test.com')
driver.find_element(By.CSS_SELECTOR,'input.inputtext[name=pass]').send_keys('pass')