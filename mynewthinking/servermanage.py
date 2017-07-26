import os
import re
import time
import requests
from globals import MAX_TIMES, WAIT_TIME
from ptest.plogger import preporter

from autotest.public.utils import kill_progress_by_name, current_dir,start_process_by_command,run_command_on_shell


def close_appium_server():
    kill_progress_by_name("node")


def start_appium_server():
    close_appium_server()

    print("start appium server")
    cmd = "appium --session-override"
    start_process_by_command(cmd)
    time.sleep(WAIT_TIME)
    # i =0
    # while i< MAX_TIMES:
    #     time.sleep(WAIT_TIME)
    #     if is_appium_running():
    #         preporter.info("appium has started!")
    #         return appium_process
    #     i +=1
    # raise Exception("appium not start within {} seconds".format(MAX_TIMES*WAIT_TIME))


def is_appium_running():
    try:
        statu_url = "0.0.0.0:4723/wd/hub/status"
        response = requests.get(statu_url)

        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        preporter.info("check staus on appium fail")
        return False
# def start_appium_server_with_log():
#     file = current_dir + "/" + "appium.txt"
#     if os.path.exists(file):
#         os.remove(file)
#     cmd = "appium --session-override > {}".format(file)
#     start_process_by_command(cmd)




def kill_adb_port():
    cmd = "lsof -i tcp:5037"
    result = run_command_on_shell(cmd)
    #record = result.split("\n")[1]
    # port = record.split(" ")[1]
    port = re.search("\d+", result[1])
    if port:
        cmd_port = "kill -9 {}".format(port.group(0))
        run_command_on_shell(cmd_port)


if __name__ == '__main__':
    # close_appium_server()
    # start_appium_server_with_log()
    kill_adb_port()
