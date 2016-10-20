__author__ = 'ming.xiesh'

# !/usr/bin/env python
# encode='utf-8'

import json
import re
import urllib
import urllib2
from optparse import OptionParser

'''
This tool use for:
1. Pass a whole level quickly
2. Pass a level test quickly
This tool only for EC v1.0 account, and only on UAT and QA environment.
If you want to test level move on, you can improve efficiency

By the way, this tool dependent on the tool SubmitScoreHelper
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
}
host = "uat1"
#host = "qa"
ini_url = "http://{0}.englishtown.com/services/school/_tools/progress/SubmitScoreHelper.aspx?newengine=true&token=".format(
    host)
ini_para = {}

load_url = "http://{0}.englishtown.com/services/school/_tools/progress/SubmitScoreHelper.aspx".format(host)


def get_activity_score(activity_list):
    score_list = []
    for activity_id in activity_list:
        score = {
            "score": 100,
            "minutesSpent": 0,
            "activity_id": activity_id,
            "content": "",
            "siteVersion": "13-1"
        }
        score_list.append(score)
    activity_score = {"activityScores": score_list}
    print activity_score
    return activity_score


def get_cookie(url, para, headers):
    postData = urllib.urlencode(para)
    req = urllib2.Request(url, postData, headers=headers)
    response = urllib2.urlopen(req)
    thePage = response.read()
    return thePage


def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage)
    # parser.add_option("-n", "--name", dest="name", action="store", help="The user's name")
    parser.add_option("-l", "--level", dest="level",
                      action="store", type="int", default=0,
                      help="The start level")

    (options, args) = parser.parse_args()
    level = options.level
    get_cookie(ini_url, ini_para, headers)
    user_name = raw_input("please input your user name: ")
    load_para = {
        "cmd": "loadStudentInfo",
        "member_id": user_name,
        "token": ""
    }
    levels_page = get_cookie(load_url, load_para, headers)

    match_course = levels_page.split("$")
    print match_course

    menber = match_course[0].split("|")
    menber_id = menber[3]
    partener = menber[4]
    print partener
    level_1 = menber[5]
    match_course.pop(0)
    lists = []
    for list in match_course:
        m = re.search(r'#(\d{3})', str(list))
        if m:
            lists.append(m.group(1))
    lists.insert(0, level_1)
    print lists
    print "get course done"
    course_id = lists[int(level)]
    load_unit_list = {
        "cmd": "loadUnitList",
        "course_id": course_id,
        "member_id": menber_id,
        "token": ""
    }
    unit_page = get_cookie(load_url, load_unit_list, headers)
    print unit_page
    unit_list = unit_page.split("$")
    print unit_list

    units = []
    for unit in unit_list:
        m = re.search(r'\d{4}', str(unit))
        if m:
            units.append(m.group(0))
    print units
    print "get units done"
    level_test = raw_input("Are you want to do level test? yes|no")
    if level_test == 'yes':
        search = units
    else:
        search = units[0:6]

    for unit_id in search:
        unit_list_progress = {
            "cmd": "loadUnitProgress",
            "member_id": menber_id,
            "course_id": course_id,
            "unit_id": unit_id,
            "hasEvc": "false",
            "enrollToUnit": "false",
            "resetUnit": "false",
            "keepUnfinish": "undefined",
            "token": ""
        }
        progress_page = get_cookie(load_url, unit_list_progress, headers)
        print progress_page
        ss = json.loads(progress_page)
        print ss["Lessons"]
        lessons = str(ss["Lessons"])
        match_pattern = re.compile(r"'Activities':\s\[(.*?)\]")
        match_pat = re.compile(r"'ID':\s(\d+),")
        activity_id = re.findall(match_pattern, lessons)
        print activity_id
        activity_list = []
        for id in activity_id:
            activity = re.findall(match_pat, id)
            activity_list.append(activity)

        print activity_list

        act_list = str(activity_list).replace('[', '').replace(']', '')
        act_list = act_list.replace('\'', '')
        print act_list
        submit = {
            "cmd": "batchSaveActivityScore",
            "member_id": menber_id,
            "course_id": course_id,
            "unit_id": unit_id,
            "act_ids": act_list,
            "grade": "100",
            "keepUnfinish": "0",
            "hasEvc": "false",
            "partnerCode": partener,
            "engineVersion": "2",
            "token": "",
            "isReview": ""
        }
        print submit
        submit_page = get_cookie(load_url, submit, headers)
        print submit_page
        progress_page = get_cookie(load_url, unit_list_progress, headers)
        print progress_page
    print "Done!"


if __name__ == '__main__':
    main()
