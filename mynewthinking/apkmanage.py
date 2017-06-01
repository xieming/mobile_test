__author__ = 'anderson'
from globals import *
import requests, re, os
import shutil
from ptest.plogger import preporter


def get_build_url(self):
    preporter.info(self.Jenkins_build_url)
    builds_urls = requests.get(self.Jenkins_build_url)

    builds = [each_build['relativePath'] for each_build in builds_urls.json()['artifacts']]
    preporter.info(builds)
    current_build = re.findall(
            "{}/build/outputs/apk/{}-{}-{}-{}.*?.apk".format(self.type, self.type, self.build_name,
                                                             current_device_info.device_env,
                                                             current_device_info.build_type), ','.join(builds))

    preporter.info(current_build)

    if current_build:
        apk_url = builds_urls.json()['url'] + "artifact/" + current_build[0]
        apk_name = current_build[0].split("/")[-1]
        preporter.info(apk_url)
        preporter.info(apk_name)
        return apk_url, apk_name

    else:
        preporter.info("cannot find the build ")

def check_folder(sef, folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

def download_file(self, url, path):
    file = requests.get(url).content
    with open(path, 'wb') as f:
            f.write(file)

def download_build(self):
    apk_url, apk_name = self.get_build_url()
    self.check_folder(apk_path)
    self.download_file(apk_url, apk_path + apk_name)
