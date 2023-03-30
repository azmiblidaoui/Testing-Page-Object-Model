from BasePage import *
class LoginPage(BasePage):
    username_field =(By.NAME, '')
    password_field  = (By.NAME,'')
    login_button = (By.XPATH,'')
    worning_message = (By.XPATH,'')
    def __init__(self, driver):
        super().__init__(driver) #or BasePage.__init__(self,driver)
        
    def set_username(self,username_field,username):
        self.set_value(self,username_field,username)
    
    def set_password(self, password):
        self.set_value(self.password_field, password)
    
    def click_login_btn(self):
        self.click_ele(self.login_button)

    def login(self,username,password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_btn()


    
