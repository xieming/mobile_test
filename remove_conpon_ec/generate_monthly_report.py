import zeep
import arrow
import requests
from globals import name,year,month


host="mobilefirst"
member_id = name

clear_cache_tool_url = "http://smartuat2.englishtown.com/services/ecplatform/Tools/CacheClear/Clear"
headers = {'content-type': "application/x-www-form-urlencoded"}

basicinfo_data = {

    'cachetype': 'StudentBasicInfo',
    'paras': member_id

}

member_site_setting_data = {

    'cachetype': 'MemberSiteSettings',
    'paras': {"Member_id":member_id,"SiteArea":""}

}


def clear_cache_for_basicinfo(data):

    response =requests.post(url = clear_cache_tool_url, data=data, headers=headers)
    return response



wsdl = 'http://{}.englishtown.com/services/ecplatform/StudyPlanService.svc?wsdl'.format(host)
# client = zeep.Client(wsdl=wsdl, wsse=UsernameToken('SalesforceSmartUser', 'SalesforceSmartPwd'))
client = zeep.Client(wsdl=wsdl)

current_time = arrow.now()


import datetime


def join_group():

    client.service.JoinGroup(studentId = member_id)



def generate_monthly_report():

    client.service.UpdateMonthlyKeywordCount(studentId = member_id, cultureCode= 'zh-CN', year =year , month =month , forceSendNotification = True )


if __name__ == '__main__':
    clear_cache_for_basicinfo(basicinfo_data)
    clear_cache_for_basicinfo(member_site_setting_data)
    generate_monthly_report()