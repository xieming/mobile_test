__author__ = 'anderson'

#-*- coding: UTF-8 -*-
import requests

import re
import sys
import pymysql
import time

import sys
import json

conn = pymysql.connect(host="localhost",user="root",passwd="root",db="douban",charset="utf8")
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS douban')
sql = """CREATE TABLE douban( id int primary key not null auto_increment,title text,actor text ,rating char(20))"""

cur.execute(sql)



url = 'https://movie.douban.com/j/chart/top_list?type=10&interval_id=100:90&action=&start=20&limit=100'
req = request(url)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
req.add_header('User-Agent' ,user_agent)
try:
    response = urlopen(req)
except HTTPError as e:
    print ('The server couldn.')
    print ('Error code:',e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason:',e.reason)
html = response.read().decode('utf-8')

lp= re.compile(r'movie.douban.com.*?subject.*?\\d+')
link=lp.findall(html)





for i in link:
    i=(i.replace('\\\\',''))

    url ='https://'+ i
    req = Request(url)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
    req.add_header('User-Agent' ,user_agent)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print ('The server couldn\\.')
        print ('Error code:',e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason:',e.reason)
    html = response.read().decode('utf-8')




    p1 = re.compile(r'<span property="v:itemreviewed">(.*?)</span>')
    p2=re.compile(r'"v:starring">(.*?)</a>')
    p3=re.compile(r'<strong class="ll rating_num" property="v:average">(.*?)</strong>')
    t =p1.findall(html)
    a=p2.findall(html)
    r=p3.findall(html)
    sql2='INSERT INTO douban VALUES(null,"%s","%s","%s")'
    l=[]
    l.append([t,a,r])

    cur.executemany(sql2,l)
    conn.commit()
    for j in t:
        print("writting"+j)
    time.sleep(0.5)
