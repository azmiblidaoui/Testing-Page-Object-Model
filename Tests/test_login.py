from Pages.Login_pages import LoginPage
from Base_Test import BaseTest
from utilities.test_data import TestData

class TestLogin(BaseTest):
    def test_valid_cerdentials(self):
       LoginPg = LoginPage(self.driver)
       LoginPg.set_username(TestData.username)
       LoginPg.set_username(TestData.password)
       LoginPg.login()
       title = LoginPg.get_title()
       assert title == "OrangeHRM"