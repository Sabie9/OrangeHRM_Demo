import pytest
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

class Test_TC001_login_test:
    # Retrieve application URL and admin credentials from configuration file
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    # Initialize logger for logging test execution details
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        """Test case to verify the homepage title of the application."""
        self.logger.info("*** Start of test_homePageTitle ***")
        self.driver = setup
        self.driver.implicitly_wait(3)
        self.driver.delete_all_cookies()  # Clear cookies to avoid session conflicts
        self.driver.get(self.base_url)  # Open the application URL

        act_title = self.driver.title  # Get the current page title

        try:
            # Verify if the title matches the expected value
            assert act_title == "OrangeHRM", "Test Failed: Home Page Title Mismatch"
            self.logger.info("*** PASS: test_homePageTitle ***")
        except AssertionError as e:
            self.logger.error("*** FAIL: test_homePageTitle ***")
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")  # Capture screenshot on failure
            raise e  # Raise the assertion error for test reporting
        finally:
            self.driver.quit()  # Ensure the browser closes after test execution

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_admin_login(self, setup):
        """Test case to verify admin login functionality."""
        self.logger.info("*** Start of test_admin_login ***")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.delete_all_cookies()  # Clear cookies before login
        self.driver.get(self.base_url)  # Open the application URL

        # Create an instance of the LoginPage object
        self.lp = LoginPage(self.driver)

        # Enter admin credentials
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login_btn()

        # Check if the "Dashboard" heading is displayed after login
        self.dashboard_status = self.lp.check_dashboard()

        try:
            if self.dashboard_status:
                self.logger.info("*** Logged in Successfully as expected ***")
                # Perform logout operation
                self.lp.click_dropdown_btn()
                self.lp.click_logout_btn()
                self.logger.info("*** Logged out Successfully ***")
                self.logger.info("*** PASS: test_admin_login ***")
                assert True  # Test passes if login is successful
            else:
                self.logger.info("*** Login Failed ***")
                self.logger.info("*** FAIL: test_admin_login ***")
                assert False  # Test fails if login is unsuccessful
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\test_admin_login.png")  # Capture screenshot on failure
            self.logger.error("*** FAIL: test_admin_login ***")
            raise e  # Raise the exception for debugging
        finally:
            self.driver.quit()  # Ensure the browser closes after test execution
