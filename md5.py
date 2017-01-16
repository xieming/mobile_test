import os
import re
import shutil
import subprocess
import time

PATH = lambda p: os.path.abspath(p)

englishtown_url = "http://10.128.42.155:8080/view/Engage/job/engage-android-release/{0}/artifact/engage/build/outputs/apk/engage-englishtown-live-release.apk"
corporate_url = "http://10.128.42.155:8080/view/Engage/job/engage-android-release/{0}/artifact/engage/build/outputs/apk/engage-corporate-live-release.apk"
smartenglish_url = "http://10.128.42.155:8080/view/Engage/job/engage-android-release/{0}/artifact/engage/build/outputs/apk/engage-smartenglish-live-release.apk"

current_dir = os.path.split(os.path.realpath(__file__))[0]
report_path = current_dir + "/apk/"
old_path = current_dir + "/old/"
new_path = current_dir + "/new/"
product = raw_input("please input the product")
if product =="b2c":
    url = englishtown_url
    package = "com.ef.core.engage.englishtown"
if product =="b2b":
    url = corporate_url
    package = "com.ef.core.engage.corporate"
if product =="ec":
    url = smartenglish_url
    package = "com.ef.core.engage.smartenglish"


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
        print "Please connect devices"
        Ids = []
    return Ids

def getdeviceinfo():
        cmd = 'adb shell cat /system/build.prop'
        cmd1 = 'adb shell dumpsys window displays |head -n 3'
        deviceinfo = os.popen(cmd)
        resolution = exec_command(cmd1)
        infoList = deviceinfo.readlines()
        #print infoList

        dict ={}

        param = ['ro.product.manufacturer','ro.build.version.release','ro.build.version.sdk','ro.product.model','ro.product.brand','ro.product.locale.language','ro.product.locale.region']

        for info in infoList:
            for each_param in param:
                if str(each_param) in str(info):
                    k = info.split('=')[0]
                    s = k.split('.')
                    dict[s[-1]] = info.split('=')[1].strip()
        print dict.items()
        print resolution



def find_apks():
    apks = []
    for c in os.listdir(os.getcwd()):
        if os.path.isfile(c) and c.endswith('.apk'):
            apks.append(c)
    return apks

def find_package(package):
    cmd = 'adb shell pm list package -3 | grep {0}'.format(package)
    package_name = exec_command(cmd)
    return package_name

# def upgrade_englishtown(old_folder,new_folder):
#     old_version = raw_input("please input the old build number")
#     new_version = raw_input("please input the new build number")
#     old_apk_name = englishtown_url.format(old_version).split("/")[-1]
#     get_url(englishtown_url.format(old_version),old_folder)
#     new_apk_name = englishtown_url.format(new_version).split("/")[-1]
#     get_url(englishtown_url.format(new_version),new_folder)
#     return old_apk_name, new_apk_name

def upgrade_app(old_folder,new_folder):
    old_version = raw_input("please input the old build number")
    new_version = raw_input("please input the new build number")

    old_apk = url.format(old_version).split("/")[-1]
    get_url(url.format(old_version),old_folder)
    new_apk = url.format(new_version).split("/")[-1]
    get_url(url.format(new_version),new_folder)
    print "old apk is : %s" % old_apk
    install_apk(old_path + old_apk)
    print "new apk is : %s" % new_apk
    install_apk(new_path+new_apk)

def intall_apk(apkname):
    cmd = 'adb install {0}'.format(apk_name)
    result = exec_command(cmd)
    if (re.search("success", result)):
        print "install success!"
    else:
        print "install fail!"

def install_apks(version,name=report_path):

    if find_package(package) != "":
        print "App Already exist,remove it!"
        uninstall_apks
    apk_name = url.format(version).split("/")[-1]
    cmd = 'adb install {0}'.format(name + apk_name)
    check_folder(name)
    result = exec_command(cmd)
    if (re.search("success", result)):
        print "install success!"
    else:
        print "install fail!"

def uninstall_apks():

    if find_package(package) == "":
        print "Nothing to uninstall"
    else:
        cmd = 'adb uninstall {0}'.format(package)
        result = exec_command(cmd)
        if (re.search("success", result)):
            print "uninstall success!"
        else:
            print "uninstall fail!"

def screenshot():
    path = PATH(os.getcwd() + "/screenshot")
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
        os.makedirs(path)
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    print "success"



def main():

    choose = raw_input("please select the type you want: 1:md5,2:install,3:uninstall,4:upgrade,5:screenshot,6:devices")
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
    # elif choose == '2':


    #     # check_folder(new_path)
    #     # upgrade_englishtown(old_path,new_path)
    #     # print "old apk is : %s" % old_apk
    #     # install_apks(old_path + old_apk)
    #     # print "new apk is : %s" % new_apk
    #     # install_apks(new_path+new_apk)


    # elif choose == '3':
    #     # pg = find_package("smart")
    #     # print pg
    #     getdeviceinfo()
    #     screenshot()


    else:
        print "please select again"




if __name__ == '__main__':
    main()
