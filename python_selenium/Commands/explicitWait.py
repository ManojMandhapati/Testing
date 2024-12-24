from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Create an explicit wait object
wait = WebDriverWait(driver, 10)
#wait = WebDriverWait(driver, 10, poll_frequency = 2,ignored_exceptions = [NoSUchElementException,
# ElementNotVisibleException,
# ElementNotSelectedException])

try:
    # Open Google
    driver.get("https://www.google.com/")
    driver.maximize_window()

    # Wait for the search box to be visible
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Scroll into view (if needed) and interact directly
    driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
    search_box.send_keys("Selenium")
    search_box.submit()

    # Wait for and click the Selenium result link
    selenium_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Selenium']")))
    selenium_link.click()

finally:
    # Close the browser
    driver.quit()