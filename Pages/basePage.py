from selenium import webdriver
from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self,driver):
        """
        The basepage's purpose is to hold methods that are common to all page objects.
        """
        self.driver = driver
    def find_element(self,*locator):
        return self.driver.find_element(*locator)
    def click_ele(self,locator):
        self.find_element(*locator).click()
    def set_value(self,locator,value):
        self.find_element(*locator).clear()
        self.find_element(*locator).send_keys(value)
    def get_text(self,locator):
        return self.find_element(*locator).text
    def get_title(self):
        return self.driver.title
    


