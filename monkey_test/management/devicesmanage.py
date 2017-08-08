import os
import shutil
import subprocess
import time
from subprocess import Popen
from multiprocessing import Pool

import requests
from ptest.plogger import preporter
from public.utils import run_command_on_shell
from management.yamlmanage import YAML

current_dir = os.path.split(os.path.realpath(__file__))[0]
log_dir = current_dir + "/log/"
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_devices_version(device):
    cmd = "adb -s {} shell getprop ro.build.version.release".format(device)
    result = run_command_on_shell(cmd)[0]
    return result


def get_devices_name(device):
    cmd = "adb -s {} shell getprop ro.product.model".format(device)
    result = run_command_on_shell(cmd)[0]
    return result


def list_devices():
    cmd = "adb devices"
    result = run_command_on_shell(cmd)
    print(result)
    return result


def get_devices_info():
    current = list_devices()
    devices = []
    j = 0
    port= 4723
    bootstrap = 5000
    for i in current[1:]:
        if i != "":
            each_device = {}
            nPos = i.index("\t")
            dev = i[:nPos]
            each_device["id"] = dev
            each_device["version"] = get_devices_version(dev)
            each_device["name"] = get_devices_name(dev)
            each_device["port"]= port + j
            each_device["bootstrap"] = bootstrap + j
            each_device["username"]= YAML().get_users()[j]
            devices.append(each_device)
            j = j + 1

    print(devices)
    return devices