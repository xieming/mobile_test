import subprocess
import os
import time
from datetime import datetime


import requests
from ptest.plogger import preporter

current_dir = os.path.split(os.path.realpath(__file__))[0]
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



START_ANDROID_DEVICE_TIMEOUT = 8
INVALID_PROCESS_ID = -1

MobileEnv = 'uat'
HttpStatusCode = 'http'

def run_command(command_string):
    try:
        output = subprocess.check_output(command_string, shell=True, stderr=subprocess.STDOUT)
        return output.decode().strip()
    except subprocess.CalledProcessError as err:
        print("Command Error", err)
        preporter.info('error {} for command {}'.format(err, command_string))

def kill_progress_by_name(progress_name):
    cmd="killall -9 {}".format(progress_name)
    run_command(cmd)
    preporter.info("progress {} was killed ".format(progress_name))



def write_log(file_name,content):
    file = current_dir+"/"+file_name
    with open(file, 'w+') as f:
        f.write(content)





# def open_genymotion_android_emulator(device_identity):
#     """
#     open genymotion android emulator by device id or device name
#     :return:
#     """
#     try:
#         start_process_by_command(
#             "open -a {} --args --vm-name '{}'".format(MobileEnv.GENYMOTION_APP_PATH, device_identity))
#     except:
#         preporter.info('emulator {} is not started'.format(device_identity))
#         raise
#
#
# def kill_process_by_name(process_name):
#     preporter.info('kill process {}'.format(process_name))
#     run_command_on_shell('killall {}'.format(process_name))
#
#
# def close_android_emulator():
#     """
#     close android emulator started by genymotion
#     use 'killall' command to be able to kill genymotion vms by process name player
#     refer to https://en.wikipedia.org/wiki/Killall, https://linux.die.net/man/1/killall
#     :return:
#     """
#
#     kill_process_by_name('player')
#     preporter.info('all android emulator killed')
#
#
# def remove_ios_app_on_simulator(bundle_id):
#     preporter.info('remove app {} on simulator'.format(bundle_id))
#     run_command_on_shell('xcrun simctl uninstall booted {}'.format(bundle_id))
#     preporter.info('app {} is removed from simulator'.format(bundle_id))
#
#
# def remove_android_app(package_name):
#     preporter.info('remove app {} on emulator'.format(package_name))
#     run_command_on_shell('adb uninstall {}'.format(package_name))
#     preporter.info('android app {} is removed from emulator'.format(package_name))
#
#
# def has_device_running(retry_times=MAX_RETRY_TIMES, interval=RETRY_INTERVAL):
#     # TODO: adb devices is not solid solution to determine device is ready for running automation, will figure out another approach to do this check
#     i = 0
#
#     while i < retry_times:
#         time.sleep(interval)
#         device_info = run_command_on_shell('adb devices')
#
#         if len(device_info) > 1:
#             for line in device_info:
#                 preporter.info(line)
#             return True
#
#         i += 1
#
#     return False
#
#
# def start_ios_simulator(device_identity, kill_before_start=True):
#     if kill_before_start:
#         kill_process_by_name(MobileEnv.IOS_SIMULATOR_PROCESS_NAME)
#
#     preporter.info('starting ios simulator {}'.format(device_identity))
#     run_command_on_shell('instruments -w \'{}\''.format(device_identity))
#     preporter.info('ios simulator {} started'.format(device_identity))
#
#
# def start_android_device_by_genymotion(device_identity, timeout=RETRY_INTERVAL * MAX_RETRY_TIMES):
#     """
#     setup device with device id or name using genymotion
#     :param device_identity:
#     :return:
#     """
#     close_android_emulator()
#     open_genymotion_android_emulator(device_identity)
#     start_time = datetime.now()
#     time.sleep(timeout)
#
#     if (not has_device_running()):
#         elapsed = datetime.now() - start_time
#         raise Exception(
#             "Emulator is not started successfully within {}, please check environment manually".format(elapsed))
#     else:
#         preporter.info("Emulator started successfully")
#
#
# def run_command_on_shell(command_string):
#     """
#     this function is used to run command and return output lines
#     command
#     :param command_string:
#     :return:
#     """
#     process = start_process_by_command(command_string)
#     out, error = process.communicate()
#     return out.decode().splitlines()
#
#
#
# def start_appium(address=MobileEnv.Appium.SERVER_ADDRESS_DEFAULT, port=MobileEnv.Appium.SERVER_PORT_DEFAULT,
#                  interval=RETRY_INTERVAL,
#                  retry_times=MAX_RETRY_TIMES):
#     kill_listening_process_on_port(port)
#     preporter.info('starting appium on port {}'.format(port))
#     appium_process = start_process_by_command('appium -a {} -bp {}'.format(address, str(port)))
#     i = 0
#
#     while i < retry_times:
#         time.sleep(interval)
#
#         if is_appium_running(address, port):
#             preporter.info('appium started on port: {}'.format(port))
#             return appium_process
#         i += 1
#
#     raise Exception('appium not started on port {} within {} seconds'.format(port, retry_times * interval))
#
#
# def is_appium_running(address=MobileEnv.Appium.SERVER_ADDRESS_DEFAULT, port=MobileEnv.Appium.SERVER_PORT_DEFAULT):
#     try:
#         status_url = MobileEnv.Appium.URL_PREFIX_FORMAT.format(address, port) + MobileEnv.Appium.STATUS_URL
#         response = requests.get(url=status_url)
#
#         if response.status_code == HttpStatusCode.OK:
#             return response.json()['status'] == MobileEnv.Appium.StatusCode.SUCCESS
#         else:
#             return False
#     except Exception as e:
#         preporter.info("checking status on {} failed with exception: \n{}".format(status_url, e))
#         return False
#
#
# def get_process_info_on_port(port):
#     result = run_command_on_shell("lsof -i tcp:{}".format(str(port)))
#
#     return result[1:] if len(result) > 1 else result
#
#
# def get_listening_process_id_on_port(port):
#     process_info = get_process_info_on_port(port)
#
#     processes = []
#
#     for process in process_info:
#         if process.__contains__(':{} (LISTEN)'.format(port)):
#             processes.append(process.split()[1])
#
#     return processes
#
#
# def kill_listening_process_on_port(port):
#     """
#     kill the process which listens on the port, it  will also kill all connection to this port
#     :param port:
#     :return:
#     """
#     pids = get_listening_process_id_on_port(port)
#     if not pids:
#         preporter.info('no process listening on port {}'.format(port))
#         return
#
#     for pid in pids:
#         run_command_on_shell('kill %s' % str(pid))
#
#     pids = get_listening_process_id_on_port(port)
#
#     if not pids:
#         preporter.info('process killed on port {}'.format(port))
#     else:
#         preporter.info('processes {} still running on port {}'.format(pids, port))