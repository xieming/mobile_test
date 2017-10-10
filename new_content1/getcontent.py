import re

import requests

from globals import *

THREAD_COUNT_FOR_GET_JSON_FILE = 1
THREAD_COUNT_FOR_CHECK_URL = 8
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
        # print(json_result.content)
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


def check_resource(url):
    pattern = re.compile(r'http:\/\/+(.*).[(mp3)|(mp4)|(jpg)]$', re.IGNORECASE)

    url_status = 0
    print(url)

    if re.search(pattern, url):
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
