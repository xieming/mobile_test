import os
import re
import shutil
import subprocess
import time



englishtown_url = "http://10.128.42.155:8080/view/Engage/job/engage-android-release/{0}/artifact/engage/build/outputs/apk/engage-englishtown-live-release.apk"
corporate_url = "http://10.128.42.155:8080/view/Engage/job/engage-android-release/{0}/artifact/engage/build/outputs/apk/engage-corporate-live-release.apk"

current_dir = os.path.split(os.path.realpath(__file__))[0]
report_path = current_dir + "/apk/"
old_path = current_dir + "/old/"
new_path = current_dir + "/new/"


def exec_command(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (stdoutdata, stderrdata) = result.communicate()
    if (re.search("error", str(stdoutdata))):
        print "error occur!"
    else:
        return stdoutdata

def check_folder(name):
    if os.path.exists(name):
        # os.removedirs(report_path)
        shutil.rmtree(name)

    else:
        pass
    os.makedirs(name)


def get_url(url,folder_name):
    cmd = 'curl -O {0}'.format(url)
    os.chdir(folder_name)
    exec_command(cmd)
    os.chdir(current_dir)


def check_md5(file):
    cmd = 'md5 {0}'.format(file)
    md5_id = exec_command(cmd)
    print "{0} md5 value is {1}".format(file, md5_id)


def find_devices():
    rst = os.popen('adb devices').read()
    devices = re.findall(r'(.*?)\s+device',rst)
    if len(devices) > 1:
        Ids = devices[1:]
    else:
        Ids = []
    return Ids

def find_apks():
    apks = []
    for c in os.listdir(os.getcwd()):
        if os.path.isfile(c) and c.endswith('.apk'):
            apks.append(c)
    return apks

def upgrade_englishtown(old_folder,new_folder):
    old_version = raw_input("please input the old build number")
    new_version = raw_input("please input the new build number")
    old_apk_name = englishtown_url.format(old_version).split("/")[-1]
    get_url(englishtown_url.format(old_version),old_folder)
    new_apk_name = englishtown_url.format(new_version).split("/")[-1]
    get_url(englishtown_url.format(new_version),new_folder)
    return old_apk_name, new_apk_name

def upgrade_corporate(old_folder,new_folder):
    old_version = raw_input("please input the old build number")
    new_version = raw_input("please input the new build number")
    old_apk_name = corporate_url.format(old_version).split("/")[-1]
    get_url(corporate_url.format(old_version),old_folder)
    new_apk_name = corporate_url.format(new_version).split("/")[-1]
    get_url(corporate_url.format(new_version),new_folder)
    return old_apk_name, new_apk_name

def install_apks(apk_name):
    cmd = 'adb install {0}'.format(apk_name)
    print cmd
    result = exec_command(cmd)
    print result
    if (re.search("success", result)):
        print "install success!"
    else:
        print "install fail!"



def main():

    choose = raw_input("please select the type you want: 1:md5,2:upgrade_englishtown,3:upgrade_corporate")
    if choose == '1':
        build_id = raw_input("please input the build number")
        check_folder(report_path)
        get_url(englishtown_url.format(build_id),report_path)
        get_url(corporate_url.format(build_id),report_path)
        if os.path.exists(report_path):
            for file in os.listdir(report_path):
                check_md5(report_path  + file)
        else:
            "please check your network!"
    elif choose == '2':
        check_folder(old_path)
        check_folder(new_path)
        (old_apk,new_apk) =upgrade_englishtown(old_path,new_path)
        print "old apk is : %s" % old_apk
        install_apks(old_path + old_apk)
        print "new apk is : %s" % new_apk
        install_apks(new_path+new_apk)


    elif choose == '3':
        check_folder(old_path)
        check_folder(new_path)
        (old_apk, new_apk) = upgrade_corporate(old_path,new_path)
        print "old apk is : %s" % old_apk
        install_apks(old_path + old_apk)
        print "new apk is : %s" % new_apk
        install_apks(new_path+new_apk)

    else:
        print "please select again"




if __name__ == '__main__':
    main()
