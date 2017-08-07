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
    if not os.path.exists(black_list):
        get_blacklist()
    cmd = "adb -s {} push {} /sdcard/{}".format(device['id'],black_list,black_list)
    run_command_on_shell(cmd)



if __name__ == '__main__':

    get_blacklist()








