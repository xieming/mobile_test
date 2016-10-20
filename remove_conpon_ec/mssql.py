__author__ = 'ming.xiesh'  
  
#!/usr/bin/env python  
#coding=utf-8  
import sys  
import pymssql  
import ConfigParser  

class MSSQL:

    def __init__(self):
        cf = ConfigParser.ConfigParser()
        #read config
        cf.read("ini.conf")
        self.host = cf.get("dbsetting", "host")
        self.user = cf.get("dbsetting", "user")
        self.password = cf.get("dbsetting", "password") 
        self.db = cf.get("dbsetting", "database")
        self.timeout = cf.get("dbsetting", "timeout")  
        self.charset = cf.get("dbsetting", "charset")
		
    def __get_connection(self):
        
        if not self.db:
            raise(NameError, "No specified database.")

        connect = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.db,
                                    timeout=self.timeout, charset=self.charset)
  
        return connect
    def exec_query(self, query):
        """
            Execute the query and fetch all the results.
        :param query: the query string
        :param query_kwargs: the format parameters for the query
        :return: all the results
        """
        with self.__get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def exec_query_and_fetch_first(self, query):
        """
            Execute the query and fetch the first result.
        :param query: the query string
        :param query_kwargs: the format parameters for the query
        :return: the first result
        """
        with self.__get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchone()

    def exec_query_and_fetch_last(self, query):
        """
            Execute the query and fetch the last result.
        :param query: the query string
        :param query_kwargs: the format parameters for the query
        :return: the last result
        """
        try:
            rows = self.exec_query(query)

            return len(rows),rows[len(rows)-1]
        except:
            connection.rollback()
            raise

        

    def exec_non_query(self, query):
        """
            Execute the non query.
        :param query: the query string
        :param query_kwargs: the format parameters for the query
        """

        with self.__get_connection() as connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
            except:
                connection.rollback()
                raise