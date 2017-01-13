

import jenkins
import os
import urllib2


class Constants(object):
    ANDROID_BUILD_SERVER = 'http://10.128.42.155:8080'
    ANDROID_APK_SHORT_NAME = {'B2B': 'engage-corporate',
                              'B2C': 'engage-englishtown'}


class BuildMode(object):
    DEBUG = 'debug'
    RELEASE = 'release'


class AndroidBuildJobs(object):
    ANDROID_DAILY_BUILD = 'engage-android-snapshot'
    ANDROID_RELEASE_BUILD = 'engage-android-release'


def get_android_last_successful_build(android_job_name, env, is_B2B, mode=BuildMode.DEBUG):
    returned_apk_name = ''
    returned_apk_full_path = ''

    android_build_server = jenkins.Jenkins(Constants.ANDROID_BUILD_SERVER)
    last_successful_build_number = android_build_server.get_job_info(android_job_name)['lastSuccessfulBuild']['number']
    build_info = android_build_server.get_job_info(android_job_name, last_successful_build_number)
    build_number_root_url = build_info['lastSuccessfulBuild']['url']

    if is_B2B:
        short_apk_name = Constants.ANDROID_APK_SHORT_NAME['B2B'] + '-' + env + '-' + mode
    else:
        short_apk_name = Constants.ANDROID_APK_SHORT_NAME['B2C'] + '-' + env + '-' + mode

    all_build_facts = build_info['lastSuccessfulBuild']['artifacts']
    for fact in all_build_facts:
        if short_apk_name in fact['fileName']:
            returned_apk_name = fact['fileName']
            returned_apk_full_path = build_number_root_url + 'artifact/' + fact['relativePath']
            break

    if returned_apk_name == '':
        assert False, "Failed to find successful build."

    return returned_apk_name, returned_apk_full_path


def download_apk(apk_build_name, apk_full_path):
    home_dir = os.getcwd()
    path = home_dir + '\\' + 'apk_files'
    if not os.path.exists(path):
        os.makedirs(path)

    path = path + '\\' + apk_build_name
    f = urllib2.urlopen(apk_full_path)
    data = f.read()
    with open(path, 'wb') as code:
        code.write(data)

    if not os.path.exists(path):
        assert False, "Failed to download to local path."

    return path