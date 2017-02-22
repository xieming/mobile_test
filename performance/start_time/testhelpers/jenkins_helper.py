from enumeration import *
from globals import current_app_info
import requests,re
from utils import *


Builds = []

class Build_jenkins:

    def __init__(self):
        self.Jenkins_download_url = JENKINS_HOST + "/view/Engage/job/{0}/lastSuccessfulBuild/api/json".format(current_app_info.app_job)


    def get_build_info(self):
        builds = requests.get("http://"+self.Jenkins_download_url)

        #for each in builds.json():
        print (builds.json()['url'])

        for each in builds.json()["artifacts"]:
            #print (each['relativePath'])
            Builds.append(each['relativePath'])

        search_build = re.findall("engage/build/outputs/apk/engage-{}-{}-{}.*?.apk".format(Product.to_name(current_app_info.app_product),current_app_info.app_env,current_app_info.app_type),','.join(Builds))
        if search_build:
            # print(Product.to_name(current_app_info.app_product))
            # print(search_build)
            apk_url = builds.json()['url'] +"artifact/"+ search_build[0]
            apk_name=search_build[0].split("/")[-1]
            return apk_url,apk_name

        else:
            print ("cannot find the build ")
        #     Builds.append(each['relativePath'])
        # m=re.findall(".*.apk",''.join(Builds))
        # Builds.append(m.group())
        # if Builds != []:
        #     print(Builds)
        #


    def download_build(self):
        url,name = self.get_build_info()
        print (url)
        check_folder(apk_path)
        download_file(url,apk_path+name)





#Build_jenkins().download_build()