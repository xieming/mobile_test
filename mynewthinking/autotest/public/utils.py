import os
import re
import shutil
import subprocess
import requests
from com.android.monkeyrunner import MonkeyRunner ,MonkeyDevice ,MonkeyImage

current_dir = os.path.split(os.path.realpath(__file__))[0]
apk_path = current_dir + "/apk/"
old_path = current_dir + "/old/"
new_path = current_dir + "/new/"


def exec_command(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (stdoutdata, stderrdata) = result.communicate()
    if (re.search("error", str(stdoutdata))):
        print ("error occur!")
    else:
        return stdoutdata


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

def download_file(url,path):
    print (path)
    file=requests.get(url).content
    with open(path,'wb') as f:
        f.write(file)

def check_md5(file):
    cmd = 'md5 {0}'.format(file)
    md5_id = exec_command(cmd)
    print ("{0} md5 value is {1}".format(file, md5_id))