
from selenium.common.exceptions import NoSuchElementException

class element_exist(object):
    def __init__(self, driver):
        self.driver = driver
    def is_element_exists_by_xpath(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def is_element_exists_by_id(self,id):
        try:
            self.driver.find_element_by_id(id)
        except NoSuchElementException:
            return False
        return True