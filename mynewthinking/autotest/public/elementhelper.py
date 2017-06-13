
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML
from autotest.public.imagehelper import Appium_Extend
from globals import WAIT_TIME
import time

class element_exist(object):

    def __init__(self, driver):
        self.driver = driver

    def IOS_element(self):

        self.driver.swipe('down')
        self.driver.swipe('up')

        page_course = YAML().current_page('CourseOverViewPage')
        settings = page_course['settings'].split(",")[1]
        location = self.driver.find_element_by_xpath(settings)
        pic = Appium_Extend(self.driver)
        course, classroom, setting = pic.get_location_by_element(location, 3)
        return course,classroom,setting

    def tap_course(self):
        course, classroom, setting = self.IOS_element()
        self.driver.tap(course, )
        time.sleep(WAIT_TIME)

    def tap_classroom(self):
        course, classroom, setting = self.IOS_element()
        self.driver.tap(classroom, )
        time.sleep(WAIT_TIME)

    def tap_setting(self):
        course, classroom, setting = self.IOS_element()
        self.driver.tap(setting, )
        time.sleep(WAIT_TIME)



