# coding=utf-8
__author__ = 'Anderson'
import time

from autotest.Base import Base_page
from autotest.public.elementhelper import element_exist
from autotest.public.yamlmanage import YAML
from globals import PLATFORM,WAIT_TIME,WAIT_MAX_TIME



class ManageCourse(Base_page):
    def __init__(self,driver):
        self.driver=driver

    manage_course_page = YAML().current_page("ManageCoursePage")
    Back_button = manage_course_page['Back_button']
    GE_course = manage_course_page['GE_course']
    BE_course = manage_course_page['BE_course']
    Lessons = manage_course_page['Lessons']

    def change_level_on_GE(self,id):
        self.wait_for_presence_of_element_located(self.Back_button)
        self.clickat(self.GE_course)
        if id > 6:
            self.swipe("up")
        level = self.Lessons%(id)
        print(level)
        self.clickat(level)
        time.sleep(WAIT_TIME)


