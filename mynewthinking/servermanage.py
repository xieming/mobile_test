from setupenv import run_command, kill_progress_by_name, current_time,write_log,current_dir
import os,re


def close_appium_server():
    return kill_progress_by_name("node")

def start_appium_server():
    cmd = "appium --session-override"
    return run_command(cmd)

def start_appium_server_with_log():
    file = current_dir+"/"+"appium.txt"
    if os.path.exists(file):
        os.remove(file)
    cmd = "appium --session-override > {}".format(file)
    run_command(cmd)

def kill_adb_port():
    cmd = "lsof -i tcp:5037"
    result = run_command(cmd)
    record = result.split("\n")[1]
    #port = record.split(" ")[1]
    port = re.search("\d+",record)
    cmd_port = "kill -9 {}".format(port.group(0))
    run_command(cmd_port)





if __name__ == '__main__':
    #close_appium_server()
    #start_appium_server_with_log()
    kill_adb_port()



