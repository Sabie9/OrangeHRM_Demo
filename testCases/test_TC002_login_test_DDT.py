import pytest
from selenium.common import NoSuchElementException

from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_TC002_login_test_DDT:
    # Read base URL from configuration file
    base_url = ReadConfig.get_base_url()

    # Define the path of the Excel file containing test data
    path = ".\\TestData\\LoginData.xlsx"

    # Initialize logger for logging test execution details
    logger = LogGen.log_gen()

    @pytest.mark.regression
    @pytest.mark.DDT
    def test_admin_login_DDT(self, setup):
        self.logger.info("***Start of test_admin_login***")

        # Get the total number of rows in the Excel sheet
        self.row = XLUtils.get_row_count(self.path, "Sheet1")

        # Initialize the WebDriver instance
        self.driver = setup
        self.driver.implicitly_wait(5)  # Implicit wait to handle loading delays
        self.driver.delete_all_cookies() #Deleting all cookies

        print("The number of admin login credential sets is: ", self.row)

        # List to store the test results (Pass/Fail) for each login attempt
        list_status = []

        # Loop through each row in the Excel sheet, starting from row index 2 (assuming row 1 contains headers)
        for i in range(2, self.row + 1):

            # Open the base URL for login
            self.driver.get(self.base_url)

            # Initialize LoginPage object
            self.lp = LoginPage(self.driver)

            # Read username, password, and expected result from Excel sheet
            self.username = XLUtils.get_cell_value(self.path, "Sheet1", i, 1)
            self.password = XLUtils.get_cell_value(self.path, "Sheet1", i, 2)
            self.exp = XLUtils.get_cell_value(self.path, "Sheet1", i, 3)

            # Enter credentials and attempt login
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.logger.info(f"Trying login with Username: {self.username}, Password: {self.password}")
            self.lp.click_login_btn()

            try:
                # Check if the "Dashboard" heading is displayed after login
                self.dashboard_status=self.lp.check_dashboard()

                # Validate the login result against the expected outcome
                if self.dashboard_status == (self.exp == 'Pass'):
                    self.logger.info("***Logged in Successfully as expected***")
                    list_status.append("Pass")
                else:
                    self.logger.info("***Logged in Successfully but not expected***")
                    list_status.append("Fail")

                # Perform logout operation
                self.lp.click_dropdown_btn()
                self.lp.click_logout_btn()
                self.logger.info("***Logged out Successfully***")

            except NoSuchElementException:
                # Handle case where login fails (i.e., Dashboard element is not found)
                if self.exp == 'Pass':
                    self.logger.info("***Login Failed but not expected***")
                    list_status.append("Fail")
                else:
                    self.logger.info("***Login Failed as expected***")
                    # Capture screenshot for reference in case of a failed login attempt
                    self.driver.save_screenshot(f".\\Screenshots\\test_homePageTitle{i}.png")
                    list_status.append("Pass")

        # Final assertion: If any test case failed, mark the test as failed
        if 'Fail' in list_status:
            self.logger.error("***FAIL: test_admin_login_DDT***")
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")  # Capture failure screenshot
            assert False
        else:
            self.logger.info("***PASS: test_admin_login***")
            assert True
