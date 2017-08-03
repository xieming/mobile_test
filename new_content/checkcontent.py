import threading
import queue
from globals import *
import re
import time
import json
import os
import sys
import requests
import numpy as np
import pandas as pd
from multiprocessing import Pool

__author__ = 'anderson'


THREAD_COUNT_FOR_GET_JSON_FILE = 1
THREAD_COUNT_FOR_CHECK_URL = 1
POST_ACTIVITY_BATCH_SIZE = 10
ASR_MINIMUM_SIZE = 10
DEFAULT_TIME_OUT = 30
HEAD_CONTENT_LENGTH = "Content-Length"

fail_media_url_list = []
media_url_list = set()

asr_error = []
exit_flag = 0




class LevelActivityStructure():
    def __init__(self, session_id, token, type):
        self.session_id = session_id
        self.token = token
        self.type = type

    def get_levels(self):
        STUDY_CONTEXT_PARAMS["serviceRequest"]["sessionId"] = self.session_id
        STUDY_CONTEXT_PARAMS["serviceRequest"]["token"] = self.token
        level_post = requests.session().post(url=HOST + STUDY_CONTEXT_PATH, json=STUDY_CONTEXT_PARAMS)
        courses = level_post.json()["serviceResponse"]["context"]
        if self.type == 'ge':
            enrollment = courses["enrollments"][0]
        if self.type == 'be':
            enrollment = courses["enrollments"][1]

        level_id = []

        all_levels = enrollment["levels"]

        for each_level in all_levels:
            level_id.append(each_level["levelId"])

        return level_id

    def get_activity(self, level_id):
        COURSE_STRUCTURE_PARAMS["serviceRequest"]["level"] = level_id
        COURSE_STRUCTURE_PARAMS["serviceRequest"]["sessionId"] = self.session_id
        COURSE_STRUCTURE_PARAMS["serviceRequest"]["token"] = self.token

        act_post = requests.session().post(url=HOST + COURSE_STRUCTURE_PATH, json=COURSE_STRUCTURE_PARAMS)
        activity_result = act_post.json()
        level = activity_result["serviceResponse"]["level"]["units"]

        unit_activity = []

        for each_unit in level:
            lesson_activity = []
            lessons = each_unit["lessons"]

            for each_lesson in lessons:
                module_activity = set()
                modules = each_lesson["modules"]

                for each_module in modules:

                    activities = each_module["activities"]
                    activity = []
                    for each_activity in activities:
                        activity.append(each_activity["activityId"])
                    module_activity.update(activity)
                lesson_activity.append(list(module_activity))
            unit_activity.append(lesson_activity)
        return unit_activity
#
#
class ActivityJsonStructure():
    def __init__(self, session_id, token):
        # threading.Thread.__init__(self)
        self.match_path = re.compile(r'"\w+Path":\s"(http:\/\/.*?)"', re.IGNORECASE)
        self.match_asr = re.compile(r'{"asr"+.*?}', re.IGNORECASE)
        self.asr_pattern = re.compile(r'<Dictionary>+(.*)?</Dictionary>', re.IGNORECASE)
        self.session_id = session_id
        self.token = token

    def get_json(self, activity_id):
        activity_content_params = {
            "serviceRequest":
                {
                    "activities": activity_id,
                    "countryCode": service_parameter['countryCode'],
                    "partnerCode": service_parameter['partnerCode'],
                    "siteVersion": service_parameter['siteVersion'],
                    "appVersion": service_parameter['appVersion'],
                    "culturecode": service_parameter['culturecode'],
                    "platform": service_parameter['platform'],
                    "sessionId": self.session_id,
                    "token": self.token,
                    "productId": service_parameter['productId']
                }
        }

        json_result = requests.session().post(url=HOST + ACTIVITY_CONTENT_PATH, json=activity_content_params)
        #print(json_result.content)
        json_file = json_result.json()

        return json_file

    def get_url(self, strings):
        url_list = re.findall(self.match_path, strings)

        media_url_list.update(url_list)

    def get_asr(self, keys, strings):
        asr_list = re.findall(self.match_asr, strings)

        if len(asr_list):
            for each_asr in asr_list:
                print(each_asr)

                check_asr(self.asr_pattern, each_asr, keys)

        # def run(self):
        #     while True:
        #         if ActivityJsonStructure.json_queue.empty():
        #             break
        #
        #         else:
        #             each_activity_id = ActivityJsonStructure.json_queue.get()
        #             json = self.get_json(each_activity_id)
        #             self.get_url(json)
        #             self.get_asr(each_activity_id, json)
        #
        #     ActivityJsonStructure.json_queue.task_done()
#
#
class MediaFile():
    def __init__(self):
        # threading.Thread.__init__(self)
        self.pattern = re.compile(r'http:\/\/+(.*).[(mp3)|(mp4)|(jpg)]$', re.IGNORECASE)


    def check_resource(self,url):
        url_status = 0

        if re.search(self.pattern, url):
            try:
                status = requests.head(url, allow_redirects=False).status_code
                if status != 200:
                    fail_media_url_list.append(url)
                    url_status += 1

            except:

                fail_media_url_list.append(url)
                url_status += 1

        else:
            fail_media_url_list.append(url)
            url_status += 1

        return url_status
#
#         # def run(self):
#         #     while not exit_flag:
#         #         if MediaFile.url_queue.empty():
#         #             break
#         #
#         #         else:
#         #             url = MediaFile.url_queue.get()
#         #             status = self.check_resource(url)
#         #
#         #             if status == 0:
#         #                 #size = self.get_file_size(url)
#         #                 size = requests.head(url,allow_redirects=True).headers[HEAD_CONTENT_LENGTH]
#         #
#         #                 if size < 100:
#         #                     fail_media_url_list.append(url)
#         #
#         #     MediaFile.url_queue.task_done()
#
#

def check_asr(pattern, asr, key):
    if re.findall(pattern, asr):
        asr_one = re.search(pattern, asr)
        print(asr_one.group(1))

        if len(asr_one.group(1)) < ASR_MINIMUM_SIZE:
            asr_error.append(key)

    else:
        asr_error.append(key)
#
#
def write_result_report(fail_media_url_list):
    current_dir = os.path.split(os.path.realpath(__file__))[0]
    report_path = current_dir + "/result"
    end_time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    if not os.path.exists(report_path):
        os.makedirs(report_path)

    with open("%s/report.html" % (report_path), "w") as f:
        str_report_header = """
            <html>
                <head>
                    <title>Content media Files Check Report</title>
                    <style>
                        td {
                            word-wrap:break-word;word-break:break-all;
                        }
                    </style>
                </head>
                <div align='center'> Product: %s </div>
                <div align='center'> Environment: %s </div>
                <div align='center'> Begin Time: %s </div>
                <div align='center'> End Time: %s </div>
                <div align='center'> User: %s </div>

                <br>
                <table border='1' align='center' cellpadding=0 style='border-collapse: collapse' >
                <tr>
                    <td align='center'>%s</td>
                    <td align='center'>%s</td>
                </tr>""" % (
            PRODUCT, ENV, START_TIME, end_time_stamp, USERNAME, len(fail_media_url_list), len(asr_error))
        f.write(str_report_header)

        if len(asr_error) > 0:
            for each_fail_asr in asr_error:
                fail_text = """
                    <tr>
                        <td> Fail </td>
                        <td align='center'> <font color='red'>%s</td>
                    </tr>""" % (each_fail_asr)
                f.writelines(fail_text)

        if len(fail_media_url_list) > 0:
            for each_fail_url in fail_media_url_list:
                fail_text = """
                <tr>
                    <td> Fail </td>
                    <td align='center'>
                        <a href='%s' target='_blank'> <font color='red'>%s </a>
                    </td>
                </tr>""" % (each_fail_url, each_fail_url)
                f.writelines(fail_text)
        f.write("</table></html>")
#

def main():
    login_post = requests.session().post(url=HOST + LOGIN_PATH, json=LOGIN_PARAMS)
    result = login_post.json()
    session_id = result["serviceResponse"]["sessionId"]
    token = result["serviceResponse"]["token"]



    print("start to get levels, please wait for a moment-------")

    if SPIN == 'True' :
        type = "be"

    else:
        type = "ge"

    level_http = LevelActivityStructure(session_id, token, type)
    level = level_http.get_levels()  # just for debug levels = [20000507]
    print (level)



    if not os.path.exists('%s_activity.xlsx' % (PRODUCT)):

        # levels = [20000759]
        writer = pd.ExcelWriter('%s_activity.xlsx' % (PRODUCT))
        for i in range(len(level)):
            result = level_http.get_activity(level[i])
            get_ids = pd.DataFrame(result)
            get_ids.to_excel(writer, "%d" % (i))
        # haha.to_csv(path_or_buf="haha.csv",header=False)

    if os.path.exists("%s_activity.xlsx"%(PRODUCT)):
        for i in range(1):
            id_reader = pd.read_excel("%s_activity.xlsx"%(PRODUCT), sheetname=[i], index_col=None)
            #print(id_reader[i])

            ss = id_reader[i]

            def get_activity(x):
                for i in range(4):
                    activity_string = x.get(i).replace("[", "").replace("]", "").replace(" ", "")
                    #print(activity_string)

                    jsonfile = ActivityJsonStructure(session_id, token).get_json(activity_string.split(","))
                    ActivityJsonStructure(session_id, token).get_url(json.dumps(jsonfile))

                    if ASR == 'True':
                        ActivityJsonStructure(session_id, token).get_asr(activity_string.split(","), json.dumps(jsonfile))



            ss.apply(get_activity, axis=1)

            # serise1 = pd.Series(media_url_list)
            # serise1.to_csv("url.csv")
    #         get_urls = pd.DataFrame(media_url_list)
    #         urlwriter = pd.ExcelWriter('%s_url.xlsx' % (PRODUCT))
    #         get_urls.to_excel(urlwriter, "%s"%(i))
    #
    #
    # if os.path.exists('%s_url.xlsx' % (PRODUCT)):
    #     for i in range(1):
    #         url_reader = pd.read_excel('%s_url.xlsx' % (PRODUCT), sheetname=[i], index_col=None)
    #                 # print(id_reader[i])
    #
    #         urls = url_reader[i]
    #
    #         def check_urls(x):
    #
    #             if x.notnull:
    #                 print(x)
    #
    #                 MediaFile(x).check_resource()
    #
    #         urls.apply(check_urls, axis=1)
    #         print(fail_media_url_list)

    print(len(media_url_list))
    for x in list(media_url_list):

        MediaFile().check_resource(x)

    write_result_report(fail_media_url_list)

    print("-----------scan finished-----------")

    if (len(fail_media_url_list) + len(asr_error)) > 0:
        print ("Finished! total error number is: %s" % (len(fail_media_url_list) + len(asr_error)))

    else:
        print("no error found!")


if __name__ == '__main__':
    main()