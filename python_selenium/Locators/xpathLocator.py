from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serviceObj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service = serviceObj)

driver.get("http://www.automationpractice.pl/")

#input("Press Enter to quit...")  # Keeps browser open until Enter is pressed
# OR

driver.maximize_window()

#Absolute xpath
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

#Relative xpath
# driver.find_element(By.XPATH,'//input[@id="search_query_top"]').send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[@type ='submit']").click()

#Using OR & AND
# driver.find_element(By.XPATH,"//input[@id = 'search_query_top' or @name = 'search']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//button[@type ='submit' and @name = 'submit_search']").click()

#Contains() & start-with()

# driver.find_element(By.XPATH,"//input[contains(@id, 'search')]").send_keys("T-shirt")
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()

#Text()
driver.find_element(By.XPATH,"//a[text()='Women']").click()

time.sleep(10)  # Keeps the browser open for 10 seconds


# driver.set_window_position(0, 0)
# driver.set_window_size(1920, 1080)  # Adjust to your screen resolution

