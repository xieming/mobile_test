# coding=utf-8
__author__ = 'Anderson'
import time

from autotest.Base import Base_page
from autotest.public.elementhelper import element_exist
from autotest.public.yamlmanage import YAML
from globals import PLATFORM


class Course(Base_page):
    def __init__(self,driver):
        self.driver=driver

    course_page = YAML().current_page("CourseOverViewPage")

    setting = course_page['settings']
    settings_logout = course_page['settings_logout']

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



    def course_overview_android(self):
        self.wait_activity(self.course_page_activity)
        self.saveScreenshot("%s.png" % (self.course_page))

    def logout_android(self):
        self.course_overview_android()
        self.clickat(self.setting)
        self.clickat(self.settings_logout)

    def pass_one_unit_android(self):
        self.wait_activity(self.course_page_activity)
        time.sleep(10)
        print(self.course_page["lessonone"])
        lessons = self.find_elements(self.course_page["lessonone"])
        #lessons = self.driver.find_elements_by_id("unit_lessons_page")
        print(lessons)
        for i in range(5):
            print("start lesson {}".format(i))
            print("lesson {}".format(lessons[i]))
            self.pass_one_lesson_android(lessons[i])

    def pass_one_lesson_android(self, lesson):
        lesson.click()
        time.sleep(5)
        self.wait_activity(self.lesson_page_activity)
        time.sleep(2)
        self.clickat(self.lesson_collapse)
        time.sleep(2)
        #self.driver.wait_activity(self.module_page_activity)
        elements = self.find_elements(self.module_page["modules"])
        print("module number is {number}".format(number=len(elements)))
        i = 0
        for element in elements:
            self.pass_one_module_android(element)
            print("start %d module" % (i))
            i = i + 1

        self.clickat(self.back_button)
        time.sleep(3)

    def pass_one_module_android(self, module):
        module.click()
        time.sleep(2)

        if self.is_element_exists(self.module_download):
            self.clickat(self.module_download)
            time.sleep(35)
        self.clickat(self.module_start)

        time.sleep(2)

        while self.is_element_exists(self.activity_skip):
            self.clickat(self.activity_skip)
            time.sleep(2)

        self.clickat(self.countinue_button)
        time.sleep(2)

    def logout_ios(self):
        element = element_exist(self.driver)
        self.swipe('down')
        element.tap_setting()
        self.swipe('down')
        self.swipe('down')
        time.sleep(2)
        self.clickat(self.settings_logout)

    def pass_one_unit_ios(self):
        pass

    def pass_one_lesson_ios(self):
        self.countinue_button(self.find_element(self.course_page["lessonone"]))
        time.sleep(2)
        modules = self.find_elements(self.module_page["moduleall"])
        for i in range(0, len(modules) + 1, 2):
            modulesline = self.find_element(self.module_page["moduleach"] % (i))
            for module in modulesline:
                self.pass_one_module_ios(module)

    def pass_one_module_ios(self, module):

        module.click()
        if self.is_element_exists(self.module_download):
            self.clickat(self.module_download)
            time.sleep(5)
        self.clickat(self.module_start)
        time.sleep(2)

        if self.is_element_exists(self.module_page["arrow"]):
            self.clickat(self.module_page["arrow"])
            self.swipe('down')

        if self.is_element_exists(self.countinue_button):
            self.clickat(self.countinue_button)

        self.clickat(self.module_start)

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

    # def pass_one_lesson_action(self):
    #     if PLATFORM == "Android":
    #         self.pass_one_lesson_android()
    #
    #     if PLATFORM == "IOS":
    #         self.pass_one_lesson_ios()
    #
    def pass_one_unit_action(self):
        if PLATFORM == "Android":
            self.pass_one_unit_android()

        if PLATFORM == "IOS":
            self.pass_one_unit_ios()

