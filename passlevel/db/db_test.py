import pymssql
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

host = "10.128.34.249"
user = "BOSTON\ming.xiesh"
password ="Good_Luck999"
database="ET_Main"
timeout = 60
charset= "utf8"

def read_file(path):
    file = open(path, 'r')
    line = file.readlines()
    file.close()
    file_result = ''.join(line)
    return file_result

def connect_db():
    connect = pymssql.connect(host=host, user=user, password=password, database=database,
                              timeout=timeout, charset=charset)
    sql = "SELECT * FROM ET_Main.dbo.Members WHERE username = 'stest25539'"

    df = pd.read_sql(sql,connect)
    #print(df['MemberId'])
    #print(df.ix[0,0])
    memberid = df.ix[0,0]
    member_id_last=str(memberid)[-1]
    sql4 = read_file('sql4.txt')%(memberid)
    sql4 = sql4.replace("school_0", "school_" + member_id_last)
    print(sql4)
    df1 = pd.read_sql(sql4, connect)
    print(df1)

    choice = input("please choose the id which level you have done")
    id = df1.ix[int(choice),['id','extradata']]
    print(id)
    print(id['id'])
    print(id['extradata'])
    datevalue = eval(id['extradata'])
    print(datevalue["enrollDate"] - timedelta(days=100))
    print(type(datevalue))

    sql5 = read_file('sql5.txt')%(id['extradata'],id['id'],memberid)
    sql5 = sql5.replace("school_0", "school_" + member_id_last)



def main():
    connect_db()


if __name__ == '__main__':
    main()