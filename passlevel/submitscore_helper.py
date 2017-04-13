

import requests



class SubmitScoreHelperV1():
    def __init__(self, host):

        self.load_url = "http://{0}.englishtown.com/services/school/_tools/progress/SubmitScoreHelper.aspx?newengine=true&token=".format(host)
    def get_page(self, parameters):
        response=requests.post(url=self.load_url,data=parameters)
        return response.json()

    def get_score(self, activity_id):
        score_json = {
            'score': 100,
            'minutesSpent': 0,
            'activity_id': activity_id,
            'content': '',
            'siteVersion': '13-1'
        }
        response = self.get_page(score_json)

        return response

    def load_student_information(self, member_id):
        load_student_info_json = {
            'cmd': 'loadStudentInfo',
            'member_id': member_id,
            'token': ''
        }
        response = self.get_page(load_student_info_json)

        return response

    def load_unit_list(self, course_id, member_id):
        load_unit_list_json = {
            'cmd': 'loadUnitList',
            'course_id': course_id,
            'member_id': member_id,
            'token': ''
        }
        response = self.get_page( load_unit_list_json)

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
        response = self.get_page(unit_list_progress_json)

        return response

    def enroll_to_new_level_unit(self, member_id, course_id, unit_id):
        unit_list_progress_json = {
            'cmd': 'loadUnitProgress',
            'member_id': member_id,
            'course_id': course_id,
            'unit_id': unit_id,
            'hasEvc': 'false',
            'enrollToUnit': 'true',
            'resetUnit': 'false',
            'keepUnfinish': 'undefined',
            'token': ''
        }
        response = self.get_page(unit_list_progress_json)

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
        response = self.get_page(batch_save_activity_score_json)


        return response