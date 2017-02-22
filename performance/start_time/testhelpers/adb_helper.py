import os
import re
from utils import *
from ptest.plogger import preporter
import platform
import shutil
import subprocess
import time

def find_devices():
    rst = os.popen('adb devices').read()
    devices = re.findall(r'(.*?)\s+device', rst)
    if len(devices) > 1:
        Ids = devices[1:]
    else:
        Ids = []
    return Ids


def get_device_state():
    """
    status: offline | bootloader | device
    """
    return exec_command("adb get-state")

def get_device_id():
    return exec_command("adb get-serialno")


def get_android_version():
    return exec_command("adb shell getprop ro.build.version.release")


def get_sdk_version():
    return exec_command("adb shell getprop ro.build.version.sdk")


def get_device_model():
    return exec_command("adb shell getprop ro.product.model")


# def get_pid(package_name):
#     if system is "Windows":
#         pidinfo = exec_command("adb shell ps | findstr %s$" %package_name).stdout.read()
#     else:
#         pidinfo = exec_command("adb shell ps | %s -w %s" %(find_util, package_name)).stdout.read()
#
#     if pidinfo == '':
#         return "the process doesn't exist."
#
#     pattern = re.compile(r"\d+")
#     result = pidinfo.split(" ")
#     result.remove(result[0])
#
#     return pattern.findall(" ".join(result))[0]


def kill_process(pid):
    if exec_command("adb shell kill %s" %str(pid)).stdout.read().split(": ")[-1] == "":
        return "kill success"
    else:
        return exec_command("adb shell kill %s" %str(pid)).stdout.read().split(": ")[-1]


def quit_app(package_name):
    exec_command("adb shell am force-stop %s" % package_name)


def find_apks(path):

    if os.path.isfile(path) and path.endswith('.apk'):
        return True
    else:
        print("No file found")
        return False



def install_apks(apk_name):
    cmd = 'adb install {0}'.format(apk_name)
    result = exec_command(cmd)


def cover_install_apks(apk_name):
    cmd = 'adb install -r {0}'.format(apk_name)
    result = exec_command(cmd)


def uninstall_apks(package_name):
    cmd = 'adb uninstall {0}'.format(package_name)
    result = exec_command(cmd)

def check_start_time(start_page):
    cmd='adb shell am start -W -n {} | grep TotalTime'.format(start_page)
    result = exec_command(cmd)
    return result