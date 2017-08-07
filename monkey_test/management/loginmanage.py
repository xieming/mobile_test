from Base import Base_page
import time
from globals import WAIT_TIME

class Login(Base_page):
    # def __init__(self,device):
    #     super(Login, self).__init__(device=device)
    #     self.username= device["name"].split("/")[0]
    #     self.password = device["name"].split("/")[1]

    def login(self,device):
        super(Login, self).__init__(device=device)
        self.username = device["name"].split("/")[0]
        self.password = device["name"].split("/")[1]
        username = self.driver.find_element_by_id("txtName")
        username.clear()
        self.driver.set_value(username,self.username)
        password =self.driver.find_element_by_id("txtPwd")
        password.clear()
        self.driver.set_value(password,self.password)
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(WAIT_TIME)


