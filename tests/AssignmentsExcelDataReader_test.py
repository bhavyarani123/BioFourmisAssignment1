from utils import XLUtils
from selenium import webdriver
import pytest

class Test_ExcelReader():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=r"C:/Users/bhavy/PycharmProjects/BioFourmisAssignment/drivers/chromedriver.exe")
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_ReadTestData(self, test_setup):

        path = "C://Users/bhavy/PycharmProjects/BioFourmisAssignment/utils/login_users.xlsx"
        rows = XLUtils.getRowsCount(path, 'Sheet1')

        for r in range(2, rows + 1):
            username = XLUtils.readData(path, "Sheet1", r, 1)
            password = XLUtils.readData(path, "Sheet1", r, 2)

            driver.find_element_by_xpath("//a[@class='login']").Click()
            driver.find_element_by_id("email").send_keys(username)
            driver.find_element_by_id("passwd").send_keys(password)
            driver.find_element_by_xpath("span[text()='Sign in']").click()

            if driver.title == "My Store":
                print("test is passed")
                XLUtils.writeData(path, 'Sheet1', r, 3, "test passed")
            else:
                print("test failed")
                XLUtils.writeData(path, 'Sheet1', r, 3, "test failed")

        driver.find_element_by_xpath("//a[@class='login']").Click()