# coding=utf-8
__author__ = 'Anderson'
from time import sleep
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML
from autotest.public.imagehelper import Appium_Extend
from autotest.public.elementhelper import element_exist
import time

from selenium.webdriver.common.by import By


# driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.Base.capabilities)
class Login(Base_page):
    # usr_input = 'com.ef.core.engage.englishtown:id/txtName'  # password input
    # pwd_input = 'com.ef.core.engage.englishtown:id/txtPwd'
    #
    # # login button
    # login_btn = 'com.ef.core.engage.englishtown:id/btnLogin'
    files = YAML().read_yml("/Users/anderson/testcode/mynewthinking/autotest/pages/pages.yml")

    # usr_input =files[0]['id']


    def input_username(self, username):
        ele = self.driver.find_element_by_id(self.files['LoginPage']['Login'][0]['id'])
        self.driver.set_value(ele, (self.files['LoginPage']['Login'][0]['value']) % (username))

    def input_password(self, password):
        ele = self.driver.find_element_by_id(self.files['LoginPage']['Login'][1]['id'])
        self.driver.set_value(ele, (self.files['LoginPage']['Login'][1]['value']) % (password))

        # click login

    def click_login_button(self):
        self.driver.find_element_by_id(self.files['LoginPage']['Login'][2]['id']).click()
        sleep(3)

    def click_logout_button(self):
        self.driver.find_element_by_xpath(self.files['CourseOverViewPage']['Setting'][0]['xpath']).click()
        self.driver.find_element_by_id(self.files['CourseOverViewPage']['settings']['logout']).click()

    def login_action(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    def logout_action(self):
        self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"], 10)
        self.click_logout_button()

    def course_overview(self):
        self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"], 10)
        time.sleep(10)
        self.driver.save_screenshot("a.png")
        # print(self.files["CourseOverViewPage"]["Download"])
        element = self.driver.find_element_by_id(self.files["CourseOverViewPage"]["LessonOne"])
        pic = Appium_Extend(self.driver)
        pic.get_screenshot_by_element(element)

    def pass_one_module(self, module):
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

    def pass_one_lesson(self, lesson):
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

    def pass_one_unit(self):
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
