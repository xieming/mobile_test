# coding=utf-8
__author__ = 'Anderson'
import time

from autotest.Base import Base_page
from autotest.public.elementhelper import element_exist
from autotest.public.yamlmanage import YAML
from globals import PLATFORM,WAIT_TIME,WAIT_MAX_TIME,WAIT_LONG_TIME



class ManageCourse(Base_page):
    def __init__(self,driver):
        self.driver=driver

    manage_course_page = YAML().current_page("ManageCoursePage")
    Back_button = manage_course_page['Back_button']
    GE_course = manage_course_page['GE_course']
    BE_course = manage_course_page['BE_course']
    Lessons = manage_course_page['Lessons']
    Lessonall = manage_course_page['Lessonsall']
    Lessonchild = manage_course_page['Lessonchild']

    def change_level_on_GE(self,id):
#        self.wait_for_presence_of_element_located(self.Back_button)
        self.clickat(self.GE_course)
        # if 6 < id <= 10:
        #     self.scroll(self.Lessons%(5), self.Lessons%(1))
        # elif 10 <id <= 14:
        #     self.scroll(self.Lessons % (5), self.Lessons % (1))
        #     self.scroll(self.Lessons % (9), self.Lessons % (5))
        # else:
        #     self.scroll(self.Lessons % (5), self.Lessons % (1))
        #     self.scroll(self.Lessons % (9), self.Lessons % (5))
        #     self.scroll(self.Lessons % (13), self.Lessons % (11))

        if id > 6:
            swipe_time = int((id -5)/2)
            for i in range (swipe_time):
                self.swipe('up')

        #     levelid = abs(id - 5 - 2 *(swipe_time))
        #     level = self.Lessons % (levelid)
        #
            ele = self.find_elements(self.Lessonchild)
            print(ele)
            for each in ele:
                if str(id) in each.text:
                    each.click()
                    break
                else:
                    print("cannot find the element")
        else:
            level = self.Lessons%(id)
            print(level)
            self.clickat(level)

        time.sleep(WAIT_LONG_TIME)


