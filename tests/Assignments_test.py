from selenium import webdriver
import pytest
from pages.Assignment1_LoginPage import LoginPage
from pages.Assignment1_HomePage import HomePage
from pages.Assignment2_MytripPage import MytripPage
from utils import utils1 as utils1


@pytest.mark.usefixtures("test_setup")
class AssignmentTestLogin():

    def Assignment1_test(self,test_setup):
        driver = self.driver
        driver = driver.get(utils1.URL1)

        login = LoginPage(driver)
        login.login_App(utils1.USERNAME,utils1.PASSWORD)

        home = HomePage(driver)
        home.Shopping()

    def Assignment2_test(self,test_setup):
        driver = self.driver
        driver = driver.get(utils1.URL2)
        booking = MytripPage(driver)
        booking.Flight_booking(utils1.fromcity, utils1.tocity)