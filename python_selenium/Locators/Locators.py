from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window() #maximize the browser window
#driver.find_element(By.ID, "small-searchterms" ).send_keys("Asus N551JK-XO076H Laptop")
#driver.find_element(By.NAME, "q").send_keys("Asus N551JK-XO076H Laptop")
#driver.find_element(By.LINK_TEXT, "Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()

#slides = driver.find_elements(By.CLASS_NAME, "homeslider-container")
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))







#driver.close() #closes one by one
#driver.quit() # closes all the tabs