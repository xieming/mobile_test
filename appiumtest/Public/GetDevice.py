__author__ = 'anderson'

# -*- coding: utf-8 -*-

import lib.Utils as U
import lib.adbUtils
import yaml
import os


def get_device():
    android_devices_list = []
    for device in U.cmd('adb devices').stdout.readlines():
        if 'device' in device and 'devices' not in device:
            device = device.split('\t')[0]
            android_devices_list.append(device)

    return android_devices_list


def set_device_yaml():
    device_lst = []
    for device in get_device():
        adb = lib.adbUtils.ADB(device)
        U.Logging.success(
            'get device:{},Android version:{}'.format(
                device, adb.get_android_version()))
        device_lst.append({'platformVersion': adb.get_android_version(
        ), 'deviceName': device, 'platformName': 'Android'})

        ini = U.ConfigIni()
        dir = os.path.split(__file__)[0].replace('Public', 'Data')

        print dir
        with open(dir + ini.get_ini('test_device', 'device'), 'w') as f:
            yaml.dump(device_lst, f)
            f.close()

if __name__ == '__main__':
    # set_device_yaml()
    print "cao"
    ss = get_device()
    print "fuck"
    print ss
    if get_device() != []:
        set_device_yaml()
