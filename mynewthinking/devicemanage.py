__author__ = 'anderson'

import time
from datetime import datetime

import pandas as pd
import yaml
from ptest.plogger import preporter

from autotest.public.utils import run_command_on_shell, kill_progress_by_name,start_process_by_command
from globals import MAX_TIMES, WAIT_TIME


def get_file():
    filename = './apks.yml'
    f = open(filename)
    s = yaml.load(f)
    f.close()
    print(s['apk']['englishtown']['activity'])


def get_device_list():
    result = run_command_on_shell('VBoxManage list vms')
    print(result)

    device_list = []
    for each in result.split('\n'):
        device_list.append(each[0:each.index("{") - 1])

    # print(device_list)


    translated_dataframe = pd.DataFrame(device_list, columns=["Devices"])

    translated_dataframe["Run"] = ""

    writer = pd.ExcelWriter('devices.xlsx')
    translated_dataframe.to_excel(writer, 'android')
    writer.save()


def get_run_list():
    runlist = pd.read_excel("./devices.xlsx")
    print(runlist)
    print(runlist[runlist['Run'] == 'Y'])


def get_android_version():
    cmd = "adb shell getprop ro.build.version.release"
    result = run_command_on_shell(cmd)[0]
    return result

def get_device_name():
    cmd = "adb shell getprop ro.product.model"
    result = run_command_on_shell(cmd)[0]
    return result



def open_genemotion():
    device_name = '"Custom Phone - 5.0.0 - API 21 - 768x1280"'
    cmd = "open -a /Applications/Genymotion.app/Contents/MacOS/player.app --args --vm-name {}".format(device_name)
    try:
        start_process_by_command(cmd)
    except:
        preporter.info('emulator {} is not started'.format(device_name))
        raise


def open_new_genymotion(device_name, timeout=MAX_TIMES * WAIT_TIME):
    """
    setup device with device id or name using genymotion
    :param device_identity:
    :return:
    """
    close_android_emulator()
    open_genemotion()
    start_time = datetime.now()
    time.sleep(timeout)

    if (not is_device_running()):
        elapsed = datetime.now() - start_time
        raise Exception(
            "Emulator is not started successfully within {}, please check environment manually".format(elapsed))
    else:
        preporter.info("Emulator started successfully")


def is_device_running(retry_times=MAX_TIMES, interval=WAIT_TIME):
    i = 0

    while i < retry_times:
        time.sleep(interval)
        device_info = run_command_on_shell('adb devices')

        if len(device_info) > 1:
            for line in device_info:
                preporter.info(line)
            return True

        i += 1

    return False


def close_android_emulator():
    """
    close android emulator started by genymotion
    use 'killall' command to be able to kill genymotion vms by process name player
    refer to https://en.wikipedia.org/wiki/Killall, https://linux.die.net/man/1/killall
    :return:
    """
    return kill_progress_by_name("player")


if __name__ == '__main__':
    # get_device_list()
    # open_genemotion()

    print(get_android_version())
    print(get_device_name())
    # get_run_list()
    # get_file()
