# from passlevel.passleveltest import *
import urllib.error
import urllib.parse
import urllib.request
import re
import numpy as np

HOST = "qa"
username = "stest90644"


class PassLevelTest():
    def __init__(self):
        self.headers = {'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                        }
        self.load_url = "http://{0}.englishtown.com/services/school/_tools/progress/SubmitScoreHelper.aspx?newengine=true&token=".format(
            HOST)

    def get_page(self, url, parameters, headers):
        post_data = urllib.parse.urlencode(parameters).encode()
        request = urllib.request.Request(url, post_data, headers)
        response = urllib.request.urlopen(request)
        page = response.read()

        return page

    def load_student_information(self, username):
        load_student_info_json = {
            'cmd': 'loadStudentInfo',
            'member_id': username,
            'token': ''
        }
        response = self.get_page(self.load_url, load_student_info_json, self.headers)
        return response

    def show_unit_list_progress(self, member_id, course_id, unit_id):
        unit_list_progress_json = {
            'cmd': 'loadUnitProgress',
            'member_id': member_id,
            'course_id': course_id,
            'unit_id': unit_id,
            'hasEvc': 'false',
            'enrollToUnit': 'false',
            'resetUnit': 'false',
            'keepUnfinish': 'undefined',
            'token': ''
        }

        response = self.get_page(self.load_url, unit_list_progress_json, self.headers)

        return response

    def save_activity_score(self, member_id, course_id, unit_id, activity_ids, partner_code):
        batch_save_activity_score_json = {
            'cmd': 'batchSaveActivityScore',
            'member_id': member_id,
            'course_id': course_id,
            'unit_id': unit_id,
            'act_ids': activity_ids,
            'grade': '100',
            'keepUnfinish': '0',
            'hasEvc': 'false',
            'partnerCode': partner_code,
            'engineVersion': '2',
            'token': '',
            'isReview': ''
        }

        response = self.get_page(self.load_url, batch_save_activity_score_json, self.headers)

        return response

    def level_test(self):
        result = self.load_student_information(username).decode()
        menber_id = result.split('|')[3]
        partener = result.split('|')[4]
        final_unit = result.split('#')[-1]

        unit_id = final_unit[:final_unit.index("$")]
        course_id = final_unit[final_unit.index("|") + 1:]

        unitresponse= self.show_unit_list_progress(menber_id,course_id,unit_id).decode()
        matched_activity = re.compile(r'"Activities":\[(.*?)\]')
        matched_activity_id = re.compile(r'"ID":(\d+),')

        activity_id = re.findall(matched_activity, unitresponse)
        print(activity_id)

        activity = [re.findall(matched_activity_id, id) for id in activity_id]

        activity_arry = np.array(activity)
        print(activity_arry)
        activity_string = ""

        for row in activity_arry:
            activity_string += ",".join(row) + ","
        print(activity_string.rstrip(","))
        activity_ids = activity_string.rstrip(",")

        self.save_activity_score(menber_id,course_id,unit_id,activity_ids,partener)

def main():
    passlevetest=PassLevelTest()
    passlevetest.level_test()


if __name__ == '__main__':
    main()
