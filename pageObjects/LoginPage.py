from selenium.webdriver.common.by import By
class LoginPage:
    testbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class = 'button-1 login-button']"
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver): #Construcotr
        self.driver = driver

    def setUserName(self,username): #Action method
        #self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.testbox_username_id)#.send_keys(username)

    def setPassword(self,password): #Action method
        #self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id)#.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()