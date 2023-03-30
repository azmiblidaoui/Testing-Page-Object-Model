from basePage import BasePage
class LoginPage(BasePage):
    email_address_field =(By.name, "username")
    password_field  = (By.name,"password")
    login_button = (By.XPATH,"//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    worning_message = (By.XPATH,"//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
    



    

    
