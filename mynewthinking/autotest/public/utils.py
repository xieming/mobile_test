import os
import shutil
import subprocess
import time
from subprocess import Popen

import requests
from ptest.plogger import preporter

current_dir = os.path.split(os.path.realpath(__file__))[0]
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def run_command_on_shell(command_string):
    try:
        process = start_process_by_command(command_string)
        out, error = process.communicate()
        return out.decode().splitlines()
    except:
        print("Command Error")
        preporter.info('error occur for command {}'.format(command_string))
        raise

def start_process_by_command(command_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT):
    process = Popen(command_string, shell=shell, stdout=stdout, stderr=stderr)
    return process


def kill_progress_by_name(progress_name):
    cmd = "killall -9 {}".format(progress_name)
    run_command_on_shell(cmd)
    preporter.info("progress {} was killed ".format(progress_name))


def write_log(file_name, content):
    file = current_dir + "/" + file_name
    with open(file, 'w+') as f:
        f.write(content)


# def exec_command(cmd):
#     result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     (stdoutdata, stderrdata) = result.communicate()
#     if (re.search("error", str(stdoutdata))):
#         print ("error occur!")
#     else:
#         return stdoutdata


def check_folder(name):
    if os.path.exists(name):
        # os.removedirs(report_path)
        shutil.rmtree(name)
    os.makedirs(name)


# def get_url(url, folder_name):
#     cmd = 'curl -O {0}'.format(url)
#     os.chdir(folder_name)
#     exec_command(cmd)
#     os.chdir(current_dir)

def download_file(url, path):
    print(path)
    file = requests.get(url).content
    with open(path, 'wb') as f:
        f.write(file)
