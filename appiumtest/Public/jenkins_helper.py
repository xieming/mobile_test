#
#
# import jenkins
# import os
# import urllib2
#
#
# class Constants(object):
#     ANDROID_BUILD_SERVER = 'http://10.128.42.155:8080'
#     ANDROID_APK_SHORT_NAME = {'B2B': 'engage-corporate',
#                               'B2C': 'engage-englishtown'}
#
#
# class BuildMode(object):
#     DEBUG = 'debug'
#     RELEASE = 'release'
#
#
# class AndroidBuildJobs(object):
#     ANDROID_DAILY_BUILD = 'engage-android-snapshot'
#     ANDROID_RELEASE_BUILD = 'engage-android-release'
#
#
# def get_android_last_successful_build(android_job_name, env, is_B2B, mode=BuildMode.DEBUG):
#     returned_apk_name = ''
#     returned_apk_full_path = ''
#
#     android_build_server = jenkins.Jenkins(Constants.ANDROID_BUILD_SERVER)
#     last_successful_build_number = android_build_server.get_job_info(android_job_name)['lastSuccessfulBuild']['number']
#     build_info = android_build_server.get_job_info(android_job_name, last_successful_build_number)
#     build_number_root_url = build_info['lastSuccessfulBuild']['url']
#
#     if is_B2B:
#         short_apk_name = Constants.ANDROID_APK_SHORT_NAME['B2B'] + '-' + env + '-' + mode
#     else:
#         short_apk_name = Constants.ANDROID_APK_SHORT_NAME['B2C'] + '-' + env + '-' + mode
#
#     all_build_facts = build_info['lastSuccessfulBuild']['artifacts']
#     for fact in all_build_facts:
#         if short_apk_name in fact['fileName']:
#             returned_apk_name = fact['fileName']
#             returned_apk_full_path = build_number_root_url + 'artifact/' + fact['relativePath']
#             break
#
#     if returned_apk_name == '':
#         assert False, "Failed to find successful build."
#
#     return returned_apk_name, returned_apk_full_path
#
#
# def download_apk(apk_build_name, apk_full_path):
#     home_dir = os.getcwd()
#     path = home_dir + '\\' + 'apk_files'
#     if not os.path.exists(path):
#         os.makedirs(path)
#
#     path = path + '\\' + apk_build_name
#     f = urllib2.urlopen(apk_full_path)
#     data = f.read()
#     with open(path, 'wb') as code:
#         code.write(data)
#
#     if not os.path.exists(path):
#         assert False, "Failed to download to local path."
#
#     return path
import os
import re
import shutil
import subprocess
import time
import yaml

import lib.Utils as U



current_dir = os.path.split(os.path.realpath(__file__))[0]

def exec_command(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (stdoutdata, stderrdata) = result.communicate()
    if (re.search("error", str(stdoutdata))):
        print "error occur!"
    else:
        return stdoutdata

def get_url(url, folder_name):
    os.chdir(folder_name)
    if not os.path.exists(folder_name):
        print "please check you folder"
    if os.listdir(folder_name):
        for file in os.listdir(folder_name):
            if file.endswith('.apk'):
                os.remove(file)


    cmd = 'curl -O {}'.format(url)
    exec_command(cmd)
    os.chdir(os.path.split(__file__)[0])


# dir = os.path.split(__file__)[0].replace('Public', 'Data')
#
# ini = U.ConfigIni()
# apk_path = dir + ini.get_ini('test_device', 'device')
# print apk_path

# def install_apks(apk_name):
#     cmd = 'adb install {0}'.format(apk_name)
#     print cmd
#     result = exec_command(cmd)
#     print result
#     if (re.search("success", result)):
#         print "install success!"
#     else:
#         print "install fail!"

def download():
    dir = os.path.split(__file__)[0].replace('Public', 'Data')

    ini = U.ConfigIni()
    apk_path = dir + ini.get_ini('apk_location', 'apk_path')
    print apk_path

    apk_url = ini.get_ini('apk_url', 'apk_jenkins_url')
    apk_name = apk_url.split("/")[-1]
    with open(dir + ini.get_ini('apk_info', 'apk_info_path'), 'w') as f:
        yaml.dump(apk_name, f)
        f.close()
    get_url(apk_url,apk_path)

def main():

    download()

if __name__ == '__main__':
    main()