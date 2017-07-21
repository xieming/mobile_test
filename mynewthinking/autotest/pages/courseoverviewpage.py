# coding=utf-8
__author__ = 'Anderson'
import time

from autotest.Base import Base_page
from autotest.public.elementhelper import element_exist
from autotest.public.yamlmanage import YAML
from globals import PLATFORM,WAIT_TIME,WAIT_MAX_TIME



class Course(Base_page):
    def __init__(self,driver):
        self.driver=driver

    course_page = YAML().current_page("CourseOverViewPage")

    setting = course_page['settings']
    settings_logout = course_page['logout']
    lessonall = course_page["lessonall"]
    lesson1 = course_page["lessonone"]
    lesson2 = course_page["lessontwo"]
    lesson3 = course_page["lessonthree"]
    lesson4 = course_page["lessonfour"]
    lessonpl = course_page["lessonpl"]

    lesson_page = YAML().current_page("LessonOverViewPage")
    back_button = lesson_page["back_button"]

    module_page = YAML().current_page("ModuleOverViewPage")
    module_download = module_page["module_download"]
    module_start = module_page["module_start"]
    activity_skip = module_page["activity_skip_button"]
    countinue_button = module_page["countinue_button"]

    if PLATFORM == "Android":
        course_page_activity = course_page["Activity"]
        lesson_page_activity = lesson_page["Activity"]
        module_page_activity = module_page["Activity"]
        lesson_collapse = lesson_page["Lesson_collapse"]
        change_course_btn = course_page['Change_level_button']
    if PLATFORM == "IOS":
        allmodules = module_page["moduleall"]
        moduleseachline = module_page["moduleach"]



    def course_overview_android(self):
        self.wait_activity(self.course_page_activity)
        self.saveScreenshot("%s.png" % (self.course_page))

    def change_level_btn(self):
        self.clickat(self.change_course_btn)


    def logout_android(self):
        self.course_overview_android()
        self.clickat(self.setting)

        self.swipe('up')
        self.clickelement(self.settings_logout)

    def pass_one_unit_android(self):
        self.wait_activity(self.course_page_activity)
        self.wait_for_presence_of_element_located(self.lessonall)
        lessons = self.find_elements(self.lessonall)
        #lessons = self.driver.find_elements_by_id("unit_lessons_page")
        print(lessons)
        for i in range(1,5):
            print("start lesson {}".format(i))
            print("lesson {}".format(lessons[i]))
            self.pass_one_lesson_android(eval("self.lesson{}".format(i)))

    def pass_one_lesson_android(self, lesson):

        self.clickat(lesson)
        self.wait_activity(self.lesson_page_activity)

        self.clickelement(self.lesson_collapse)

        self.wait_for_presence_of_element_located(self.module_page["modules"])
        #self.driver.wait_activity(self.module_page_activity)
        elements = self.find_elements(self.module_page["modules"])
        print("module number is {number}".format(number=len(elements)))
        i = 0
        for element in elements:
            self.pass_one_module_android(element)
            print("start %d module" % (i))
            i = i + 1

        self.clickelement(self.back_button)


    def pass_one_module_android(self, module):

        module.click()

        if self.is_element_exists(self.module_download):
            self.clickelement(self.module_download)
            time.sleep(WAIT_TIME)

        if self.is_element_exists(self.module_download):
            time.sleep(WAIT_MAX_TIME)


        self.wait_for_presence_of_element_located(self.module_start)
        self.clickelement(self.module_start)


        self.wait_for_presence_of_element_located(self.activity_skip)
        while self.is_element_exists(self.activity_skip):
            self.wait_for_presence_of_element_located(self.activity_skip)
            self.clickelement(self.activity_skip)

        self.clickelement(self.countinue_button)


    def logout_ios(self):
        element = element_exist(self.driver)
        self.swipe('down')
        element.tap_setting()
        self.swipe('down')
        self.swipe('down')
        time.sleep(2)
        self.clickat(self.settings_logout)

    def pass_one_unit_ios(self):
        time.sleep(10)
        lessons = self.find_elements(self.lessonall)
        print(lessons)
        for i in range(5):
            print("start lesson {}".format(i))
            print("lesson {}".format(lessons[i]))
            self.pass_one_lesson_ios(lessons[i])

    def pass_one_lesson_ios(self,lesson):
        time.sleep(15)
        self.clickat(lesson)

        modules = self.find_elements(self.allmodules)
        for i in range(0, len(modules) + 1, 2):
            modulesline = self.find_elements(self.moduleseachline % (i))
            for module in modulesline:
                self.pass_one_module_ios(module)

    def pass_one_module_ios(self, module):
        module.click()
        time.sleep(5)
        if self.is_element_exists(self.module_download):
            self.clickat(self.module_download)
            time.sleep(15)

        # if self.is_element_exists(self.module_page["arrow"]):
        #     self.clickat(self.module_page["arrow"])
        #     self.swipe('down')
        #
        # if self.is_element_exists(self.countinue_button):
        #     self.clickat(self.countinue_button)

        self.clickat(self.module_start)

        time.sleep(2)

        while self.is_element_exists(self.activity_skip):
            self.clickat(self.activity_skip)
            time.sleep(2)

        self.clickat(self.countinue_button)
        time.sleep(2)

    def logout_action(self):
        if PLATFORM == "Android":
            self.logout_android()

        if PLATFORM == "IOS":
            self.logout_ios()

    def change_course_action(self):
        if PLATFORM == "Android":
            self.change_level_btn()



    def pass_one_lesson_action(self, lesson):
        if 'one' in lesson:
            takelesson = self.lesson1

        if 'two' in lesson:
            takelesson = self.lesson2

        if 'three' in lesson:
            takelesson = self.lesson3

        if 'four' in lesson:
            takelesson = self.lesson4
        if PLATFORM == "Android":
            self.pass_one_lesson_android(takelesson)

        if PLATFORM == "IOS":
            self.pass_one_lesson_ios(takelesson)

    def pass_one_unit_action(self):
        if PLATFORM == "Android":
            self.pass_one_unit_android()

        if PLATFORM == "IOS":
            self.pass_one_unit_ios()

