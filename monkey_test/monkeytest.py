import os
import shutil
import subprocess
import time
from subprocess import Popen
from multiprocessing import Pool

from public.utils import check_folder

import requests
from ptest.plogger import preporter
from globals import build_path
from public.jenkinshelper import Jenkins
from management.devicesmanage import get_devices_info
from management.appiumservermanage import start_appium_server
from management.loginmanage import login
from management.logmanage import write_blacklist
from public.utils import run_command_on_shell
from management.yamlmanage import YAML
from management.logmanage import get_log
from management.appiumservermanage import close_appium_server

current_dir = os.path.split(os.path.realpath(__file__))[0]
log_dir = current_dir + "/log/"
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())










def run_monkey(device):

    cmd = "adb -s {} shell monkey -p {} --ignore-crashes --ignore-timeouts --ignore-native-crashes -v -v -v --throttle 500 20000 > {}".format(device['id'], YAML().get_package(),get_log(device)[0])
    run_command_on_shell(cmd)
    cmd2 = "adb logcat >{}".format(get_log(device)[1])
    run_command_on_shell(cmd2)
    cmd3 = "adb shell pm clear {}".format(YAML().get_package())
    run_command_on_shell(cmd3)


# def quit():
#     cmd="adb shell input keyevent 45"
#     run_command_on_shell(cmd)
#
# def clear():
#     cmd = 'adb shell top | grep monkey'
#     pid = run_command_on_shell(cmd)[0]
#     cmd2 = 'kill -9 {}'.format(pid)
#     run_command_on_shell(cmd2)


if __name__ == '__main__':
    close_appium_server()

    check_folder(log_dir)
    # jenkins = Jenkins(build_path)
    # jenkins.download_build()
    get_devices_info()


    if get_devices_info():

        # pool3 = Pool(len(get_devices_info()))
        # pool3.map(write_blacklist,get_devices_info())
        # pool3.close()
        # pool3.join()

        pool = Pool(len(get_devices_info()))
        pool.map(start_appium_server,get_devices_info())
        pool.close()
        pool.join()

        pool2 = Pool(len(get_devices_info()))
        pool2.map(login,get_devices_info())
        pool2.close()
        pool2.join()
        # #
        # pool3 = Pool(len(get_devices_info()))
        # pool3.map(write_blacklist,get_devices_info())
        # pool3.close()
        # pool3.join()
        # #
        pool4 = Pool(len(get_devices_info()))
        pool4.map(run_monkey, get_devices_info())
        pool4.close()
        pool4.join()
    else:
        print("no device found")

    # end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # if end_time > current_time + 400:
    #     quit()
    #     clear()


        # if current_time > start_time + 100:
        #     clear()
        #
        # print("Done")
