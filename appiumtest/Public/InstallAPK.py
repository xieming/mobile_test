__author__ = 'anderson'

import lib.adbUtils
import xml.etree.cElementTree as ET
import re
import lib.Utils as U
import threading
from multiprocessing import Queue
import os
import CheckEnvironment
import yaml


class Ia:
    def __init__(self, all_result_path, device):
        """
        Queue progress
        :param all_result_path: folder for this test
        :param device: device id
        """
        self.all_result_path = all_result_path
        self.device = device
        self.adb = lib.adbUtils.ADB(self.device)
        self.queue = Queue(10)

    @U.l()
    def __uidump(self):
        """
        get current Activity tree
        :return:xml on the path of computer
        """
        save_path = self.all_result_path + "/dump.xml"
        self.adb.get_focused_package_xml(save_path)
        return save_path
    #
    # @U.l()
    # def __element(self):
    #     """
    #     element has the same attribute, return a signal point
    #     button_list:conform button,agree,button id
    #     """
    #     button0 = 'com.android.packageinstaller:id/ok_button'
    #     button1 = 'com.android.packageinstaller:id/btn_allow_once'
    #     button2 = 'com.android.packageinstaller:id/bottom_button_two'
    #     button3 = 'com.android.packageinstaller:id/btn_continue_install'
    #     button4 = 'android:id/button1'
    #     button5 = 'vivo:id/vivo_adb_install_ok_button'
    #     button_list = [button0, button1, button2, button3, button4, button5]
    #     self.__uidump()
    #     self.pattern = re.compile(r"\d+")
    #     if not os.path.exists(self.all_result_path + "/dump.xml"):
    #         U.Logging.warn('Failed to get xml')
    #         return None
    #
    #     tree = ET.ElementTree(file=self.all_result_path + "/dump.xml")
    #     tree_iter = tree.iter(tag="node")
    #     for elem in tree_iter:
    #         if elem.attrib["resource-id"] in button_list:
    #             bounds = elem.attrib["bounds"]
    #             coord = self.pattern.findall(bounds)
    #             x_point = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
    #             y_point = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
    #             return x_point, y_point
    #     else:
    #         return None

    # def tap(self):
    #
    #     coordinate_points = self.__element()
    #     if coordinate_points is not None:
    #         self.adb.touch_by_element(coordinate_points)

    # def tap_all(self):
    #     """
    #     get xml contiunly,add click with mutipli threads
    #     :return:
    #     """
    #     while True:
    #         self.tap()
    #         if not self.queue.empty():
    #             break
    #
    # @U.l()
    # def __install_app(self, package_name, app_file_path):
    #     """
    #     :param package_name: package name:com:x.x
    #     :param app_file_path: the path of the package, absloutely path
    #     :return:
    #     """
    #     self.adb.quit_app(
    #         'com.android.packageinstaller')
    #     if self.queue.empty():
    #         if self.adb.is_install(package_name):
    #             U.Logging.success(
    #                 'del {}-{}'.format(self.device, package_name))
    #             self.adb.remove_app(package_name)
    #         install_num = 0
    #         while install_num < 4:
    #             install_info = self.adb.install_app(app_file_path).stdout.readlines()
    #             U.Logging.success('install_info:%s'%install_info)
    #             if self.adb.is_install(package_name):
    #                 self.queue.put(1)
    #                 break
    #             else:
    #                 U.Logging.error('Reinstalling %s %s '%(package_name,self.device))
    #                 install_num += 1
    #         else:
    #             raise AssertionError('Reinstalling app error')
    #
    #         # kill application
    #         self.adb.quit_app('com.android.packageinstaller')
    #
    # def main(self):
    #     """
    #     start mutiply threads:
    #             thread 1: install application
    #             thread 2: get current page wheather has clickble button
    #     :return:
    #     """
    #     ini = U.ConfigIni()
    #     install_file = ini.get_ini('test_install_path', 'path')
    #     package_name = ini.get_ini('test_package_name', 'package_name')
    #
    #     threads = []
    #
    #     click_button = threading.Thread(target=self.tap_all, args=())
    #     threads.append(click_button)
    #     install_app = threading.Thread(
    #         target=self.__install_app, args=(
    #             package_name, install_file))
    #     threads.append(install_app)
    #     process_list = range(len(threads))
    #
    #     for i in process_list:
    #         threads[i].start()
    #     for i in process_list:
    #         threads[i].join()
    #
    #     self.adb.shell('"rm -r /data/local/tmp/*.xml"')
    def get_apk_name(self):
        dir = os.path.split(__file__)[0].replace('Public', 'Data')

        ini = U.ConfigIni()

        with open(dir + ini.get_ini('apk_info', 'apk_info_path'), 'r') as f:
            apk_name =yaml.load(f)
            f.close()
        return apk_name

    def install_apks(self,package_name):
        U.cmd('adb install {}'.format(self.all_result_path + package_name))

    def cover_install_apks(self,package_name):
        U.cmd('adb install -r {}'.format(self.all_result_path+package_name))

    def find_apks(self):
        apks = []
        for c in os.listdir(self.all_result_path):
            if c.endswith('.apk'):
                apks.append(c)
        return apks

    def install(self,package_name):
        dir = os.path.split(__file__)[0].replace('Public', 'Data')

        ini = U.ConfigIni()
        apk_path = dir + ini.get_ini('apk_location', 'apk_path')

        if not os.listdir(apk_path):
            print "please check you apk folder"
        else:
            print self.find_apks()
            if self.find_apks() !=[]:
                print "find the file"
                self.install_apks(package_name)
            else:
                print "cannot find apk file"



if __name__ == '__main__':
    CheckEnvironment.check_environment()


    a = Ia('/Users/anderson/work/autotest/mobile_test/mobile_test/appiumtest/Data/apk/', 'A7J5T15A28007700')
    apk_name =a.get_apk_name()
    print apk_name
    a.install(apk_name)