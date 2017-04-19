import pymssql
import pandas as pd
import numpy as np

host = "10.128.34.249"
user = "BOSTON\ming.xiesh"
password ="Good_Luck999"
#host = "CNS-ETDEVDB\INST1"
#user = "etownreader"
#password = "fishing22"
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

    name = input("please input the name")
    if "@" in name:
        sql = "SELECT * FROM ET_Main.dbo.Members WHERE email = '%s'" % (name)
    else:
        sql = "SELECT * FROM ET_Main.dbo.Members WHERE username = '%s'"%(name)

    df = pd.read_sql(sql,connect)
    #print(df['MemberId'])
    #print(df.ix[0,0])
    memberid = df.ix[0,0]
    writingsql = read_file('writingsql.txt')%(memberid)

    print(writingsql)
    df1 = pd.read_sql(writingsql, connect)
    result = df1.loc[:,['Quiz_id','LevelName']]
    print(result)

    connect.close()

def main():
    connect_db()



if __name__ == '__main__':
    main()