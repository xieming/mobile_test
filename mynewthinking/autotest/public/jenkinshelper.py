from globals import *
from enumeration import Product, Project
import requests, re, os
import shutil
from ptest.plogger import preporter
from utilities.string_helper import convert_list_to_string

JENKINS_HOST_ANDROID = "http://10.128.42.155:8080"


class Jenkins:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        if current_app_info.app_project == Project.TABLET:
            self.build_name = Product.to_name_tablet(current_app_info.app_product)
            self.type = 'efekta'

            if current_app_info.app_product == Product.EC:
                self.Jenkins_build_url = JENKINS_HOST_ANDROID + "/view/Efekta%20(LEAN)/job/efekta-android-daily/lastSuccessfulBuild/api/json"
                self.build_name = 'efec'
            else:
                self.Jenkins_build_url = JENKINS_HOST_ANDROID + "/view/Efekta%20(LEAN)/job/dla-efekta-android/lastSuccessfulBuild/api/json"

        else:
            self.build_name = Product.to_name_engage(current_app_info.app_product)
            self.type = Project.ENGAGE
            self.Jenkins_build_url = JENKINS_HOST_ANDROID + "/view/Engage/job/engage-android-snapshot/lastSuccessfulBuild/api/json"

    def get_build_url(self):
        preporter.info(self.Jenkins_build_url)

        try:
            builds_urls = requests.get(self.Jenkins_build_url)

            builds = [each_build['relativePath'] for each_build in builds_urls.json()['artifacts']]
            preporter.info(builds)
            current_build = re.findall(
                "{}/build/outputs/apk/{}-{}-{}-debug.*?.apk".format(self.type, self.type, self.build_name,
                                                                    current_app_info.app_env),
                convert_list_to_string(builds, ','))

            preporter.info(current_build)

            if current_build:
                apk_url = builds_urls.json()['url'] + "artifact/" + current_build[0]
                apk_name = current_build[0].split("/")[-1]
                preporter.info(apk_url)
                preporter.info(apk_name)
                return apk_url, apk_name

            else:
                preporter.info("cannot find the build")

        except:
            preporter.info(
                "cannot access the {url} of jenkins, please check your jenkins!".format(url=self.Jenkins_build_url))

    def check_folder(sef, folder):
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)

    def is_apk_exist(self, path):
        if os.path.isfile(path) and path.endswith('apk'):
            preporter.info("{file} exist".format(file=path))
            return True

        else:
            preporter.info("{file} does't exist".format(file=path))
            return False

    def download_file(self, url, path):
        try:
            file = requests.get(url).content
            with open(path, 'wb') as f:
                f.write(file)
        except:
            preporter.info("Download file from jenkins {url} fail, please check your jenkins".format(url=url))

    def download_build(self):
        apk_url, apk_name = self.get_build_url()
        self.check_folder(self.apk_path)
        self.download_file(apk_url, self.apk_path + "/" + apk_name)

        if self.is_apk_exist(self.apk_path + "/" + apk_name):
            preporter.info("Download file {file} success!".format(file=self.apk_path + "/" + apk_name))

        else:
            preporter.info("Download file {file} fail!".format(file=self.apk_path + "/" + apk_name))