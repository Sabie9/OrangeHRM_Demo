#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_name="username"
    textbox_password_name= "password"
    button_login_xpath="//button[text()=' Login ']"
    button_dropdown="//p[contains(@class,'oxd-userdropdown-name')]"
    button_logout_xpath="//a[text()='Logout']"
    heading_dashboard= "//h6[text()='Dashboard']"

    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    def set_username(self,username):
        username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_username_name)))
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_dropdown_btn(self):
        self.driver.find_element(By.XPATH,self.button_dropdown).click()
    def click_logout_btn(self):
       self.driver.find_element(By.XPATH,self.button_logout_xpath).click()

    def check_dashboard(self):
       return self.driver.find_element(By.XPATH,self.heading_dashboard).is_displayed()