from my_account import MyAccount
from Base_Page  import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username_field =(By.NAME, 'username')
    password_field  = (By.NAME,'password')
    login_button = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    worning_message = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')
    def __init__(self, driver):
        super().__init__(driver) #or BasePage.__init__(self,driver)
        
    def set_username(self,username_field,username):
        self.set_value(self,username_field,username)
    
    def set_password(self, password):
        self.set_value(self.password_field, password)
    
    def click_login_btn(self):
        self.click_ele(self.login_button)
        return MyAccount(self.driver)

    def login(self,username,password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_btn()
    
    def get_worning_message(self):
        return self.get_title(self.worning_message)