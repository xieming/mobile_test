import datetime
import pytz
from selenium import webdriver
from globals import *
import site
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os


class web_page():
    def __init__(self, host, admin, teacher, type, level='BEG', start_frome=None, end_to=None):
        self.host = host
        self.admin = admin
        self.teacher = teacher
        self.type = type
        self.level = level
        self.start_time = start_frome
        self.end_time = end_to
        self.login_url = "https://{}.englishtown.com/axis/home".format(self.host)
        self.reload_url = "https://{}.englishtown.com/axis/_debug/testdatagenerator.aspx".format(self.host)
        self.driver = self.get_driver()

    def get_python_location(self):
        return site.getsitepackages()[0]

    def get_driver(self):
        if os.path.exists(os.path.join(self.get_python_location(), 'chromedriver.exe')):
            chrome_options = Options()
            chrome_options.add_experimental_option("prefs", {'profile.manage_default_content_settings.images': 2})
            driver = webdriver.Chrome(os.path.join(self.get_python_location(), 'chromedriver.exe'),
                                      chrome_options=chrome_options)
        else:
            firefoxProfile = FirefoxProfile()
            firefoxProfile.set_preference('permissions.default.stylesheet', 2)
            firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
            firefoxProfile.set_preference('permissions.default.image', 2)
            driver = webdriver.Firefox(firefoxProfile,
                                       executable_path="C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe")
        return driver

    def fill_value_with_name(self, key, value):
        user = self.driver.find_element_by_name(key)
        user.clear()
        user.send_keys(value)

    def fill_value_with_id(self, key, value):
        user = self.driver.find_element_by_name(key)
        user.clear()
        user.send_keys(value)

    def open_page_with_admin(self):

        self.driver.get(self.login_url)
        self.driver.set_page_load_timeout(10)

        self.fill_value_with_name("UserName", self.admin)
        self.fill_value_with_name("Password", 1)

        loginbutton = self.driver.find_element_by_class_name("btn-submit").click()
        # if loginbutton.is_enabled():
        #     loginbutton.click()
        # else:
        #     print("please check your driver")

        self.driver.set_page_load_timeout(15)
        self.driver.get(self.reload_url)

    def arrange_class(self):

        self.fill_value_with_id("txtTeacherMemberId", self.teacher)
        self.fill_value_with_id("txtTemplateId", "784563")
        self.fill_value_with_id("txtLevelCode", self.level)

        if self.type.upper() == 'GL':
            duration = 60
            self.fill_value_with_id("txtClassDuration", str(duration))
            self.fill_value_with_id("txtServiceTypeCode", self.type.upper())

        elif self.type.upper() == 'PL':
            duration = 60
            self.fill_value_with_id("txtClassDuration", str(duration))
            self.fill_value_with_id("txtServiceTypeCode", self.type.upper())
            self.fill_value_with_id("txtLevelCode", 'BEG')

        elif self.type == 'cp20':
            duration = 30
            self.fill_value_with_id("txtClassDuration", str(duration))
            self.fill_value_with_id("txtServiceTypeCode", 'PL')
            self.fill_value_with_id("txtServiceSubTypeCode", self.type)

        if self.start_time == None and self.end_time == None:
            current_server_datetime = self.get_current_server_date()
            start_time = self.calculate_start_time(current_server_datetime)
            end_time = start_time + datetime.timedelta(minutes=duration)
        else:
            start_time = self.start_time
            end_time = self.end_time

        start_time_value = start_time.strftime('%Y-%m-%d %H:%M:%S')
        end_time_value = end_time.strftime('%Y-%m-%d %H:%M:%S')
        self.fill_value_with_id("txtStartTime", start_time_value)
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
