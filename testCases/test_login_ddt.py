import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v85.network import set_data_size_limits_for_test
import time
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XlLUtils


class Test_002_DDTLogin:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()


    def test_Login(self,setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)

        self.rows = XlLUtils.getRowCount(self.path,"Sheet1")
        print("no of rows in excel:",self.rows)

        lst_status=[]

        for r in range(2, self.rows+1):
            self.user = XlLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XlLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XlLUtils.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(10)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout();
                    lst_status.append("Pass")

                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)

            if "Fail" not in lst_status:
                self.logger.info("******* DDT Login test passed **********")
                self.driver.close()
                assert True
            else:
                self.logger.error("******* DDT Login test failed **********")
                self.driver.close()
                assert False

            self.logger.info("******* End of Login DDT Test **********")
            self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");







