import os
import shutil
import subprocess
import time
from subprocess import Popen
from multiprocessing import Pool

import requests
from ptest.plogger import preporter
from globals import current_dir


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

def check_folder(folder):
    # if os.path.exists(folder):
    #     shutil.rmtree(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)