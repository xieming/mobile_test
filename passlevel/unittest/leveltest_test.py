#from passlevel.passleveltest import *
import urllib.error
import urllib.parse
import urllib.request
import re
import numpy as np

HOST = "qa"
url = "http://{0}.englishtown.com/services/school/_tools/progress/SubmitScoreHelper.aspx?newengine=true&token=".format(HOST)
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    'X-Requested-With': 'XMLHttpRequest'
}

username = "stest90644"
load_student_info_json = {
    'cmd': 'loadStudentInfo',
    'member_id': username,
    'token': ''
}

course_id=""
member_id=""
unit_id=""
activity_ids=""
partner_code=""


#load_unit_list_json = {
#   'cmd': 'loadUnitList',
#    'course_id': course_id,
#    'member_id': member_id,
#    'token': ''
# }

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


def get_page(url, parameters, headers):
    post_data = urllib.parse.urlencode(parameters).encode()
    request = urllib.request.Request(url, post_data, headers=headers)
    response = urllib.request.urlopen(request)
    page = response.read()
    return page

def just_test():
    print("start")
    #leveltest = PassLevelForEcV1("qa", 11, "Stest88933")
    #leveltest.pass_level_test()
    response = get_page(url, load_student_info_json, headers)
    result=response.decode()
    menber_id = result.split('|')[3]
    partener = result.split('|')[4]
    final_unit = result.split('#')[-1]
    print(final_unit)
    print(type(final_unit))
    unit_id = final_unit[:final_unit.index("$")]
    course_id = final_unit[final_unit.index("|")+1:]
    print(unit_id)
    print(course_id)
    unit_list_progress_json['course_id']= course_id
    unit_list_progress_json['member_id'] =menber_id
    unit_list_progress_json['unit_id'] = unit_id
    unitresponse = get_page(url, unit_list_progress_json, headers)
    lastunit=unitresponse.decode()
    print(lastunit)
    matched_activity = re.compile(r'"Activities":\[(.*?)\]')
    matched_activity_id = re.compile(r'"ID":(\d+),')


    activity_id = re.findall(matched_activity, lastunit)
    print(activity_id)

    activity = [re.findall(matched_activity_id, id) for id in activity_id]
    #print (activity)

    activity_arry = np.array(activity)
    print(activity_arry)
    activity_string =""

    for row in activity_arry:
        activity_string += ",".join(row) +","
    print(activity_string.rstrip(","))
    activity_ids =activity_string.rstrip(",")

    #print(activity_string)
    #print(activity_arry.shape)

    #activity_page = json.loads(lastunit)
    #print(activity_page)
    #acitivity_json = activity_page['Lessons']
    #print(type(acitivity_json[0]))






def main():
    just_test()


if __name__ == '__main__':
    main()
