import threading
import queue
import configparser
import re
import time
import json
import os
import sys
import requests
import numpy as np
import pandas as pd
from globals import *

__author__ = 'anderson'

START_TIME = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
PRODUCT = str(sys.argv[1])
USER_NAME = str(sys.argv[2])
PASSWORD = str(sys.argv[3])
CONFIG_READ = configparser.ConfigParser()
CONFIG_READ.read("setting_ini.conf")

if re.search(r'engage', PRODUCT, re.IGNORECASE):
    PRODUCT_NAME = "engage"
elif re.search(r'ec', PRODUCT, re.IGNORECASE):
    PRODUCT_NAME = "ec"
print("the product is: %s \n" % (PRODUCT_NAME))

CULTURE_CODE = CONFIG_READ.get(PRODUCT_NAME, "culturecode")
COUNTRY_CODE = CONFIG_READ.get(PRODUCT_NAME, "countryCode")
PARTNER_CODE = CONFIG_READ.get(PRODUCT_NAME, "partnerCode")
SITE_VERSION = CONFIG_READ.get(PRODUCT_NAME, "siteVersion")
APP_VERSION = CONFIG_READ.get(PRODUCT_NAME, "appVersion")
PRODUCT_ID = CONFIG_READ.get(PRODUCT_NAME, "productId")
PLATFORM = CONFIG_READ.get(PRODUCT_NAME, "platform")

INPUT_ENV = "qa"

if re.search(r'UAT', INPUT_ENV, re.IGNORECASE):
    ENV = CONFIG_READ.get("envs", "uat")
elif re.search(r'QA', INPUT_ENV, re.IGNORECASE):
    ENV = CONFIG_READ.get("envs", "qa")
elif re.search(r'Staging', INPUT_ENV, re.IGNORECASE):
    ENV = CONFIG_READ.get("envs", "staging")
elif re.search(r'Live', INPUT_ENV, re.IGNORECASE):
    ENV = CONFIG_READ.get("envs", "live")
else:
    raise Exception("ENVIORNMENT Error!")

print("the env is: %s" % (ENV))
print("the user is: %s" % (USER_NAME))

HOST = "http://" + ENV + ".englishtown.com"
LOGIN_PATH = CONFIG_READ.get("path", "login")
STUDY_CONTEXT_PATH = CONFIG_READ.get("path", "studycontext")
COURSE_STRUCTURE_PATH = CONFIG_READ.get("path", "coursestructure")
ACTIVITY_CONTENT_PATH = CONFIG_READ.get("path", "activitycontent")
SAVE_PROGRESS_PATH = CONFIG_READ.get("path", "saveprogress")

THREAD_COUNT_FOR_GET_JSON_FILE = 1
THREAD_COUNT_FOR_CHECK_URL = 1
POST_ACTIVITY_BATCH_SIZE = 10
ASR_MINIMUM_SIZE = 10
DEFAULT_TIME_OUT = 30
HEAD_CONTENT_LENGTH = "Content-Length"

fail_media_url_list = []
media_url_list = []
session_id = ""
token = ""
level_id = ""
activity_id = []
progress =[]
asr_error = []
exit_flag = 0

LOGIN_PARAMS = {
    "serviceRequest":
        {
            "appVersion": APP_VERSION,
            "password": PASSWORD,
            "platform": PLATFORM,
            "productId": PRODUCT_ID,
            "userName": USER_NAME
        }
}

STUDY_CONTEXT_PARAMS = {
    "serviceRequest":
        {
            "appVersion": APP_VERSION,
            "culturecode": CULTURE_CODE,
            "platform": PLATFORM,
            "productId": PRODUCT_ID,
            "sessionId": session_id,
            "token": token
        }
}

COURSE_STRUCTURE_PARAMS = {
    "serviceRequest":
        {
            "level": level_id,
            "countryCode": COUNTRY_CODE,
            "partnerCode": PARTNER_CODE,
            "siteVersion": SITE_VERSION,
            "appVersion": APP_VERSION,
            "culturecode": CULTURE_CODE,
            "platform": PLATFORM,
            "productId": PRODUCT_ID,
            "sessionId": session_id,
            "token": token
        }
}

SAVE_PROGRESS_PARAMS = {

    "serviceRequest":
        {
            "partnerCode": PARTNER_CODE,
            "countryCode": COUNTRY_CODE,
            "siteVersion": SITE_VERSION,
            "appVersion": APP_VERSION,
            "culturecode": CULTURE_CODE,
            "platform": PLATFORM,
            "productId": PRODUCT_ID,
            "sessionId": session_id,
            "token": token,
            "progress": progress
        }

}

class LevelActivityStructure():
    def __init__(self, session_id, token):
        self.session_id = session_id
        self.token = token
        self.type = type


    def get_activity(self, level_id):
        COURSE_STRUCTURE_PARAMS["serviceRequest"]["level"] = level_id
        COURSE_STRUCTURE_PARAMS["serviceRequest"]["sessionId"] = self.session_id
        COURSE_STRUCTURE_PARAMS["serviceRequest"]["token"] = self.token

        act_post = requests.session().post(url=HOST+COURSE_STRUCTURE_PATH, json=COURSE_STRUCTURE_PARAMS)
        activity_result=act_post.json()
        level = activity_result["serviceResponse"]["level"]["units"]

        unit_activity = []


        for each_unit in level:
            lesson_activity = []
            lessons = each_unit["lessons"]

            for each_lesson in lessons:
                # module_activity = []
                modules = each_lesson["modules"]

                modules_id = []

                for each_module in modules:

                    # moduleid = each_module["moduleId"]
                    modules_id.append(each_module["moduleId"])
                #     activity =[]
                #     for each_activity in activities:
                #         activity.append(each_activity["activityId"])
                #     module_activity.append(activity)
                lesson_activity.append(modules_id)
            unit_activity.append(lesson_activity)
        return unit_activity

    def save_progress(self,progress):
        SAVE_PROGRESS_PARAMS["serviceRequest"]["progress"] = progress
        SAVE_PROGRESS_PARAMS["serviceRequest"]["sessionId"] = self.session_id
        SAVE_PROGRESS_PARAMS["serviceRequest"]["token"] = self.token

        requests.session().post(url=HOST+SAVE_PROGRESS_PATH, json=SAVE_PROGRESS_PARAMS)

def get_system_time():
    milliseconds = int(round(time.time()))
    return milliseconds

TIME_SHIFT_MILLISECONDS = 300

def prepare_progress_data(module_list):
    start_date_time = get_system_time()
    completion_date_time = start_date_time + TIME_SHIFT_MILLISECONDS


    progress = []

    for module in module_list:
        progress_node = {}
        progress_node['completionDateTime'] = completion_date_time
        progress_node['startDateTime'] = start_date_time
        progress_node['moduleId'] = module
        progress_node['score'] = 100
        progress_node['hasPassed'] = True
        progress.append(progress_node)

    return progress



def main():
    login_post = requests.session().post(url = HOST+LOGIN_PATH, json =LOGIN_PARAMS)
    result = login_post.json()
    session_id = result["serviceResponse"]["sessionId"]
    token = result["serviceResponse"]["token"]

    print("start to get levels, please wait for a moment-------")

    if PRODUCT_NAME == "ec":
        levels = ec_level_list_ids
    else:
        levels = dla_level_list_ids

    if not os.path.exists('%s.xlsx'%(PRODUCT_NAME)):
        writer = pd.ExcelWriter('%s.xlsx'%(PRODUCT_NAME))
        for i in range(16):
            result=LevelActivityStructure(session_id, token).get_activity(levels[i])
            get_ids = pd.DataFrame(result,index=range(6), columns=range(4))
            get_ids.to_excel(writer, "%d"%(i+1))
            #haha.to_csv(path_or_buf="haha.csv",header=False)

    print("please input the index+1 (1..16) of level you want to pass-------")
    index = input()
    id_reader = pd.read_excel('%s.xlsx'%(PRODUCT_NAME),sheetname=[int(index)],index_col=None)

    modules_data = id_reader[int(index)]


    def printvalue(x):

        for i in range(4):

            s = x.get(i).replace("[","").replace("]","").replace(" ","")


            t = s.split(",")
            progress = prepare_progress_data(t)
            LevelActivityStructure(session_id, token).save_progress(progress)



    modules_data.apply(printvalue,axis =1)





if __name__ == '__main__':
    main()
