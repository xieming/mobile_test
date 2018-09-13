import os

current_dir = os.path.split(os.path.realpath(__file__))[0]

sql_log = current_dir + "/remove_coupon_log.txt"
sql_file = current_dir + "/study_plan_ec_coupon.sql"

import mssql
import re

db = mssql.MSSQL()

name = "23960220"

user_info = {}

import arrow

datetime_now = arrow.utcnow()
datetime_a_month_ago = datetime_now.shift(months=-1).format('YYYY-MM-DD HH:mm:ss')
year = datetime_now.datetime.year
month = datetime_now.shift(months=-1).datetime.month
day = datetime_now.datetime.day

print(datetime_a_month_ago)


def read_file(path):
    with open(path, 'r') as f:
        line = f.readlines()

    file_result = ''.join(line)
    return file_result


if os.path.exists(sql_log):
    os.remove(sql_log)
if not os.path.exists(sql_file):
    print("no sql file found!")
else:
    sql = read_file(sql_file)


def get_sql(obj, mark):
    sql_sentence = obj[obj.find(mark) + len(mark):obj.find(mark + "_end")].strip()
    return sql_sentence


def get_menber_id():
    if "stest" in name:
        member_sql = get_sql(sql, "--step0").replace("%s", name)
        user_info["username"] = name

    else:
        member_sql = get_sql(sql, "--step0").replace("UserName", "MemberId").replace("%s", name)
        user_info["memberid"] = name

    result = db.exec_query_and_fetch_first(member_sql)
    user_info["memberid"] = result[0]
    user_info["partner"] = result[1]
    user_info["memberidlast"] = str(result[0])[-1]

    return result[0], result[1]


def update_user_actived_time(memberid):
    account_actived_sql = get_sql(sql, "--step1").format(datetime_a_month_ago, datetime_a_month_ago, memberid,
                                                         datetime_a_month_ago, memberid)
    db.exec_non_query(account_actived_sql)


def update_study_plan_actived_time(memberid):
    st_actived_sql = get_sql(sql, "--step2").format(datetime_a_month_ago, memberid)
    db.exec_non_query(st_actived_sql)


def get_course_item(memberid):
    course_item_sql = get_sql(sql, "--step3").format(user_info["memberidlast"], memberid)
    result = db.exec_query_and_fetch_first(course_item_sql)
    course_id = result[0]
    extradata = result[7]
    return course_id, extradata


def update_course_extradata(memberid):
    course_item_sql = get_sql(sql, "--step3").format(user_info["memberidlast"], memberid)
    result = db.exec_query_and_fetch_first(course_item_sql)
    course_id = result[0]
    extradate = result[7]
    return course_id, extradate


def update_course_item(couseid, extra):
    st_actived_sql = get_sql(sql, "--step4").format(user_info["memberidlast"], datetime_a_month_ago,
                                                    datetime_a_month_ago, str(extra), couseid)
    db.exec_non_query(st_actived_sql)


def get_offline_course_item():
    course_type = {}

    for i in user_info["coupon_type"]:
        st_actived_sql = get_sql(sql, "--step5").format(i, user_info["partner"],
                                                        str(year) + "-" + str(month) + "-" + str(day),
                                                        str(year) + "-" + str(month) + "-" + "28")
        result = db.exec_query_and_fetch_first(st_actived_sql)
        course_type[i] = result[0]

    print(coupon_type)
    return course_type


def take_offline_course_item(course_type):
    for i in user_info["coupon_type"]:
        st_actived_sql = get_sql(sql, "--step6").format(course_type[i], user_info["memberid"], i)
        print(st_actived_sql)
        db.exec_non_query(st_actived_sql)


if __name__ == "__main__":

    a, b = get_menber_id()
    print(a, b)
    print(user_info)
    coupon_type = ()
    if b == 'Cool':
        coupon_type = (1, 2, 3)
    elif b == 'Mini':
        coupon_type = (1, 2, 4)
    user_info["coupon_type"] = coupon_type
    update_user_actived_time(a)
    c, d = get_course_item(a)
    out = re.sub('\d+-(\d\d)-', str(year) + "-" + str(month) + "-", d)
    update_course_item(c, out)
    g = get_offline_course_item()
    print(g)
    take_offline_course_item(g)
