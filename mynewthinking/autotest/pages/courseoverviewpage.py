# coding=utf-8
__author__ = 'Anderson'
from time import sleep
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML
from autotest.public.imagehelper import Appium_Extend
import time
from autotest.pages.loginpage import Login
from autotest.public.elementhelper import element_exist

from selenium.webdriver.common.by import By


class Course(Base_page):
    # usr_input = 'com.ef.core.engage.englishtown:id/txtName'  # password input
    # pwd_input = 'com.ef.core.engage.englishtown:id/txtPwd'
    #
    # # login button
    # login_btn = 'com.ef.core.engage.englishtown:id/btnLogin'

    page_course = YAML().current_page("CourseOverViewPage")
    Setting = page_course['settings']
    settings_logout = page_course['settings_logout']

    def course_overview_android(self):
        self.wait_activity(self.page_course["Activity"])
        self.saveScreenshot("%s.png"%(self.page_course))

    def logout_android(self):
        self.course_overview_android()
        Login().logout()


    def logout_ios(self):
        element = element_exist(self.driver)
        element.tap_setting()
        self.clickat(self.find_element(self.settings_logout))

    def pass_one_module_android(self, module):
        # self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"],10)
        # time.sleep(10)
        # units = self.driver.find_elements_by_id(self.files["CourseOverViewPage"]["LessonOne"])
        # units[1].click()
        # time.sleep(5)
        # self.driver.wait_activity(self.files["LessonOverViewPage"]["Activity"],10)
        # self.driver.find_element_by_id(self.files["LessonOverViewPage"]["Lesson_collapse"][0]["id"]).click()
        # time.sleep(2)
        # self.driver.find_element_by_id(self.files["LessonOverViewPage"]["Back_button"][0]["id"]).click()
        # self.driver.wait_activity(self.files["ModuleOverViewPage"]["Activity"], 2)
        # elements = self.driver.find_elements_by_xpath(self.files["ModuleOverViewPage"]["modules"])
        module.click()
        time.sleep(2)
        ele = element_exist(self.driver)

        if ele.is_element_exists_by_id(self.files["ModuleOverViewPage"]["activity_download"][0]["id"]):
            self.driver.find_element_by_id(self.files["ModuleOverViewPage"]["activity_download"][0]["id"]).click()
            time.sleep(5)
        start_activity = self.driver.find_element_by_id(self.files["ModuleOverViewPage"]["start_activity"][0]["id"])
        start_activity.click()
        time.sleep(2)

        while ele.is_element_exists_by_id(self.files["ModuleOverViewPage"]["activity_skip_button"][0]["id"]):
            activity_skip_button = self.driver.find_element_by_id(
                self.files["ModuleOverViewPage"]["activity_skip_button"][0]["id"])
            activity_skip_button.click()
            time.sleep(2)

        self.driver.find_element_by_id(self.files["ModuleOverViewPage"]["countinue_button"][0]["id"]).click()
        time.sleep(2)
        # self.driver.find_element_by_id(self.files["ModuleOverViewPage"]["back_button"][0]["id"]).click()

        # for i in elements:
        #     i.click()
        #     module_down.click()
        #     time.sleep(2)
        #     start_activity.click()
        #     time.sleep(3)
        #     activity_skip_button.click()

    def pass_one_lesson_android(self, lesson):
        # self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"],10)
        # time.sleep(10)
        # units = self.driver.find_elements_by_id(self.files["CourseOverViewPage"]["LessonOne"])
        lesson.click()
        time.sleep(5)
        self.driver.wait_activity(self.files["LessonOverViewPage"]["Activity"], 10)
        self.driver.find_element_by_id(self.files["LessonOverViewPage"]["Lesson_collapse"][0]["id"]).click()
        time.sleep(2)
        # self.driver.find_element_by_id(self.files["LessonOverViewPage"]["Back_button"][0]["id"]).click()
        self.driver.wait_activity(self.files["ModuleOverViewPage"]["Activity"], 2)
        elements = self.driver.find_elements_by_xpath(self.files["ModuleOverViewPage"]["modules"])
        print("module number is {number}".format(number=len(elements)))
        i = 0
        for element in elements:
            self.pass_one_module(element)
            print("start %d module" % (i))
            i = i + 1

        # self.driver.find_element_by_id(self.files["ModuleOverViewPage"]["back_button"][0]["id"]).click()
        self.driver.keyevent(4)
        time.sleep(3)

    def pass_one_unit_android(self):
        self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"], 10)
        time.sleep(10)
        lessons = self.driver.find_elements_by_id(self.files["CourseOverViewPage"]["LessonOne"])
        for i in range(4):
            self.pass_one_lesson(lessons[i])
            # time.sleep(5)
            # self.driver.wait_activity(self.files["LessonOverViewPage"]["Activity"], 10)
            # self.driver.find_element_by_id(self.files["LessonOverViewPage"]["Lesson_collapse"][0]["id"]).click()
            # time.sleep(2)


            # for i in elements:
            #     i.click()
            #     module_down.click()
            #     time.sleep(2)
            #     start_activity.click()
            #     time.sleep(3)
            #     activity_skip_button.click()
