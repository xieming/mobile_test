__author__ = 'ming.xiesh'

import sys
import pymssql
import mssql
import re
import time
import os
from optparse import OptionParser

v1_num = 24


def get_sql(obj, mark):
    sql_sentence = obj[obj.find(mark) + len(mark):obj.find(mark + "_end")].strip()
    return sql_sentence

def get_menber_id(db, sql):
    result = db.exec_query_and_fetch_first(sql)
    return result[0], str(result[0])[-1],result[15]
	
def get_scaduedclass_id(db, sql):
    result = db.exec_query_and_fetch_first(sql)
    return result[0]
	
def remove_coupon(db, sql, n):
    for time in range(1, n + 1):
        db.exec_non_query(sql)
        print time

def write_log(file_name, content):
    file_object = open(file_name, 'a')
    file_object.write(content)
    file_object.close()

def read_file(path):
    file = open(path, 'r')
    line = file.readlines()
    file.close()
    file_result = ''.join(line)
    return file_result

def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage)
    parser.add_option("-n", "--name", dest="name", action="store", help="The user's name")
    parser.add_option("-a", "--amount",dest="amount",
                      action="store", type="int", default=1,
                      help="The amount of each unit you will earn for each coupon type")

    (options,args)= parser.parse_args()
    name = options.name
    num = options.amount

    if os.path.exists(os.getcwd() + "//remove_coupon_log.txt"):
        os.remove(os.getcwd() + "//remove_coupon_log.txt")
    if not os.path.exists(os.getcwd() + "//ec_coupon.sql"):
        print "no sql file found!"
    else:
        sql = read_file("ec_coupon.sql")
        member_id_sql = get_sql(sql, "--step1").replace("%s",name)
        db = mssql.MSSQL()
        member_id, member_id_last, parten_type = get_menber_id(db, member_id_sql)

        print "member id is: %s, partener type is: %s" % (member_id,parten_type)

        sql = sql.replace("school_0", "school_" + member_id_last)
        version_sql = get_sql(sql, "--step2")
        version_sql = version_sql % (member_id)

        version_result = db.exec_query(version_sql)

        version = 0
        if re.search("student.platform.version", str(version_result)):
            version = 2
        else:
            version = 1

        print "The accout: %s version is: %s" % (name, version)

        course_id_sql = get_sql(sql, "--step6")

        coupon_type ={ }
        if parten_type =="Mini" or "Indo":
            ranges = [1,2,3,4]
        else:
            ranges = [1,2,3]

        for x in ranges:

            class_sql = course_id_sql %(x)
            class_id = get_scaduedclass_id(db, class_sql)
            coupon_type[x] = class_id
        print coupon_type
        if parten_type =="Mini" or "Indo":
            coupon_type.update({6: coupon_type[4]})
        #course_id = oboe_sql.replace("%s", str(member_id))

        oboe_sql = get_sql(sql, "--step7")
        oboe_sql = oboe_sql.replace("%s", str(member_id))

        #coupon_type = {1: 3060099, 2: 3060100, 3: 3060101, 6: 3060101}
        #coupon_type = {1: 3021570, 2: 3021724,3: 3021732, 6: 3021732}

        write_log("remove_coupon_log.txt", name + " Start to remove" + time.strftime("%Y%m%d%H%M%S") + '\r\n')
		
        if version == 1:
		
            school_sql = get_sql(sql, "--step3")
            school_sql = school_sql % (member_id)
            db.exec_non_query(school_sql)
			
            for type in coupon_type:
                query_sql = oboe_sql % (coupon_type[type],type)
                write_log("remove_coupon_log.txt", query_sql + '\r\n')
                if num ==1:
                    remove_coupon(db, query_sql, 3)
                else:
                    remove_coupon(db, query_sql, v1_num)

        if version == 2:
            course_sql = get_sql(sql, "--step4")
            course_sql = course_sql % (member_id)
            level, results = db.exec_query_and_fetch_last(course_sql)
            print level
            print results

            print "start to check !"
            check_level = db.exec_query(course_sql)
            print check_level
        
            studentCouseId = results[0]
            ExtraData = results[11].replace("2016","2015")
            #print ExtraData
        
            extra_sql = get_sql(sql, "--step5")
            extra_sql = extra_sql % (ExtraData, studentCouseId, member_id)
            #print extra_sql
            db.exec_non_query(extra_sql)
            for type in coupon_type:
                query_sql = oboe_sql % (coupon_type[type],type)
                write_log("remove_coupon_log.txt", query_sql + '\r\n')
                if num ==1:
                    remove_coupon(db, query_sql, 3)
                else:
                    remove_coupon(db, query_sql, level * 6)

        print "Done!"
        write_log("remove_coupon_log.txt", "Finished!" + time.strftime("%Y%m%d%H%M%S"))


if __name__ == '__main__':
    main()