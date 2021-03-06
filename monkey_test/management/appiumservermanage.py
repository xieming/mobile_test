import re
import re
import time
import os

import requests
from ptest.plogger import preporter

from management.logmanage import log_dir
from public.utils import kill_progress_by_name, run_command_on_shell,start_process_by_command
from globals import  WAIT_TIME

CMD = 'appium -a {} -p {} --bootstrap-port {} --session-override --command-timeout 600 -U {} >{} 2>&1 &'



def close_appium_server():
    kill_progress_by_name("node")

def start_appium_server(device):
    #close_appium_server()

    host = "0.0.0.0"



    port = device['port']
    bootstrap_port = device['bootstrap']
    udid = device['id']
    appium_log = log_dir + "/" + "server.log"

    # print("start appium server")
    # cmd = CMD.format(host,port,bootstrap_port)
    # print(cmd)
    # os.popen(cmd)
    # time.sleep(WAIT_TIME)
    cmd = CMD.format(host,port,bootstrap_port,udid,appium_log)
    run_command_on_shell(cmd)
    time.sleep(WAIT_TIME)

    #time.sleep(WAIT_TIME)
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
        # record = result.split("\n")[1]
        # port = record.split(" ")[1]
    port = re.search("\d+", result[1])
    if port:
        cmd_port = "kill -9 {}".format(port.group(0))
        run_command_on_shell(cmd_port)


# if __name__ == '__main__':
#     # close_appium_server()
#     # start_appium_server_with_log()
#     APPIUMSERVER().kill_adb_port()
