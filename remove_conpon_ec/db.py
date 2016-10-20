#coding=utf-8
'''
Created on Nov 21, 2013

@author: Jamous Fu
'''
import pymssql

class MSSQLHelper:

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
 
    def __GetConnect(self):
        if not self.db:
            raise(NameError, "No specified database.")

        self.conn = pymssql.connect(host=self.host, user=self.user, \
            password=self.password, database=self.db, charset="utf8")
        
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "Failed to connect to the database.")
        else:
            return cur
 
    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        self.conn.close()
        return resList
 
    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()