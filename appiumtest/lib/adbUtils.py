__author__ = 'anderson'

# -*- coding: utf-8 -*-

import platform
import subprocess
import re
from time import sleep
import time
import os
import random

PATH = lambda p: os.path.abspath(p)


system = platform.system()
if system is "Windows":
    find_util = "findstr"
else:
    find_util = "grep"


if "ANDROID_HOME" in os.environ:
    if system == "Windows":
        command = os.path.join(
            os.environ["ANDROID_HOME"],
            "platform-tools",
            "adb.exe")
    else:
        command = os.path.join(
            os.environ["ANDROID_HOME"],
            "platform-tools",
            "adb")
else:
    raise EnvironmentError(
        "Adb not found in $ANDROID_HOME path: %s." %
        os.environ["ANDROID_HOME"])


class ADB(object):


    def __init__(self, device_id=""):
        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    def adb(self, args):
        cmd = "%s %s %s" % (command, self.device_id, str(args))
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def shell(self, args):
        cmd = "%s %s shell %s" % (command, self.device_id, str(args),)
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def get_device_state(self):
        """
        status: offline | bootloader | device
        """
        return self.adb("get-state").stdout.read().strip()

    def get_device_id(self):

        return self.adb("get-serialno").stdout.read().strip()

    def get_android_version(self):

        return self.shell(
            "getprop ro.build.version.release").stdout.read().strip()

    def get_sdk_version(self):

        return self.shell("getprop ro.build.version.sdk").stdout.read().strip()

    def get_device_model(self):

        return self.shell("getprop ro.product.model").stdout.read().strip()

    def get_pid(self, package_name):

        if system is "Windows":
            pidinfo = self.shell(
                "ps | findstr %s$" %
                package_name).stdout.read()
        else:
            pidinfo = self.shell(
                "ps | %s -w %s" %
                (find_util, package_name)).stdout.read()

        if pidinfo == '':
            return "the process doesn't exist."

        pattern = re.compile(r"\d+")
        result = pidinfo.split(" ")
        result.remove(result[0])

        return pattern.findall(" ".join(result))[0]

    def kill_process(self, pid):

        if self.shell("kill %s" %
                      str(pid)).stdout.read().split(": ")[-1] == "":
            return "kill success"
        else:
            return self.shell("kill %s" %
                              str(pid)).stdout.read().split(": ")[-1]

    def quit_app(self, package_name):

        self.shell("am force-stop %s" % package_name)

    # def get_focused_package_and_activity(self):

    #     pattern = re.compile(r"[a-zA-Z0-9.]+/.[a-zA-Z0-9.]+")
    #     out = self.shell(
    #         "dumpsys window w | %s \/ | %s name=" %
    #         (find_util, find_util)).stdout.read().strip()
    #
    #     return pattern.findall(out)[0]
#
#     def get_focused_package_and_activity(self):
#         """

#         """
#         out = self.shell(
#             "dumpsys activity activities | %s mFocusedActivity" %
#             find_util).stdout.read().strip().split(' ')[3]
#         return out
#
#     def get_current_package_name(self):
#         """

#         """
#         return self.get_focused_package_and_activity().split("/")[0]
#
#     def get_current_activity(self):
#         """

#         """
#         return self.get_focused_package_and_activity().split("/")[-1]
#
#     def get_battery_level(self):
#         """

#         """
#         level = self.shell("dumpsys battery | %s level" %
#                            find_util).stdout.read().split(": ")[-1]
#
#         return int(level)
#
#     def get_backstage_services(self, page_name):
#         """

#         """
#         services_list = []
#         for line in self.shell(
#             'dumpsys activity services %s' %
#                 page_name).stdout.readlines():
#             if line.strip().startswith('intent'):
#                 service_name = line.strip().split('=')[-1].split('}')[0]
#                 if service_name not in services_list:
#                     services_list.append(service_name)
#
#         return services_list
#
#     def get_current_backstage_services(self):
#         """

#         """
#         package = self.get_current_package_name()
#         return self.get_backstage_services(package)
#
#
#     def get_battery_temp(self):
#         """

#         """
#         temp = self.shell("dumpsys battery | %s temperature" %
#                           find_util).stdout.read().split(": ")[-1]
#
#         return int(temp) / 10.0
#
#     def get_screen_resolution(self):
#         """

#         """
#         pattern = re.compile(r"\d+")
#         out = self.shell(
#             "dumpsys display | %s PhysicalDisplayInfo" %
#             find_util).stdout.read()
#         display = pattern.findall(out)
#
#         return int(display[0]), int(display[1])
#
#     def reboot(self):
#         """

#         """
#         self.adb("reboot")
#
#
# if __name__ == "__main__":
#     A = ADB()
#     print A.get_focused_package_and_activity()