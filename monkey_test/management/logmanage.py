import os
import time
from public.utils import run_command_on_shell
from globals import current_dir



log_dir = current_dir + "/log"
black_list = current_dir + "/black.txt"
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



def get_log(device):
    monkey_log = log_dir + "/monkey{}_{}_{}.txt".format(device['id'] ,device['name'], device['version'])
    logcat_log = log_dir + "/logcat_{}_{}_{}.txt".format(device['id'] ,device['name'], device['version'])
    return monkey_log,logcat_log

def get_blacklist():
    cmd = "adb shell pm list packages -s > {}".format(black_list)
    run_command_on_shell(cmd)


def write_blacklist(device):
    print(black_list)
    if not os.path.exists(black_list):
        get_blacklist()
    cmd = "adb push {} /sdcard/{}".format(black_list,os.path.basename(black_list))
    run_command_on_shell(cmd)



if __name__ == '__main__':

    cmd = "adb devices"
    result = run_command_on_shell(cmd)
    print(result)

    dev = ""

    for i in result[1:]:
        if i != "":
            each_device = {}
            nPos = i.index("\t")
            dev = i[:nPos]
            print(dev)
        else:
            "no devices"


    devices = dev



    # get_blacklist()
    #
    write_blacklist(devices)








