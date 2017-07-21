
import datetime
import pytz
from selenium import webdriver
from globals import *

class web_page():

    def __init__(self,host,admin,teacher,type):
        self.host = host
        self.admin =admin
        self.teacher=teacher
        self.type=type
        self.login_url = "https://{}.englishtown.com/axis/home".format(self.host)
        self.reload_url = "https://{}.englishtown.com/axis/_debug/testdatagenerator.aspx".format(self.host)

        self.driver = webdriver.Chrome("C:\python35\chromedriver.exe")

    def fill_value_with_name(self,key,value):
        user = self.driver.find_element_by_name(key)
        user.clear()
        user.send_keys(value)

    def fill_value_with_id(self,key,value):
        user = self.driver.find_element_by_name(key)
        user.clear()
        user.send_keys(value)

    def open_page_with_admin(self):

        self.driver.get(self.login_url)
        self.driver.set_page_load_timeout(10)


        self.fill_value_with_name("UserName",self.admin)
        self.fill_value_with_name("Password",1)

        self.driver.find_element_by_class_name("btn-submit").click()
        self.driver.set_page_load_timeout(10)
        self.driver.get(self.reload_url)

    def arrange_class(self):

        self.fill_value_with_id("txtTeacherMemberId",self.teacher)
        self.fill_value_with_id("txtTemplateId","784563")



        if self.type.upper() == 'PL':
            duration = 20
            self.fill_value_with_id("txtClassDuration",str(duration))
            self.fill_value_with_id("txtServiceTypeCode",self.type.upper())

        else:
            duration = 30
            self.fill_value_with_id("txtClassDuration",str(duration))
            self.fill_value_with_id("txtServiceTypeCode",self.type.upper())



        current_server_datetime = self.get_current_server_date()
        start_time = self.calculate_start_time(current_server_datetime)
        end_time = start_time + datetime.timedelta(minutes=duration)

        start_time_value = start_time.strftime('%Y-%m-%d %H:%M:%S')
        end_time_value = end_time.strftime('%Y-%m-%d %H:%M:%S')
        self.fill_value_with_id("txtStartTime",start_time_value)
        self.fill_value_with_id("txtEndTime", end_time_value)



    @staticmethod
    def calculate_start_time(current_server_datetime):
        start_time = current_server_datetime.replace(second=0)
        if current_server_datetime.minute < 30:
            start_time = start_time.replace(minute=30)
        else:
            start_time += datetime.timedelta(hours=1)
            start_time = start_time.replace(minute=0)
        return start_time

    @staticmethod
    def get_current_server_date():
        server_tz = pytz.timezone('US/Eastern')
        now_server = datetime.datetime.now(server_tz)
        return now_server






# if __name__ == "__main__":
#     host = "mobilefirst"
#     type = "pl"
#     page = web_page(host)
#     page.open_page_with_admin()
