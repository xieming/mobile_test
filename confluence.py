#!/usr/bin/python


from bs4 import BeautifulSoup

# for change encoding
import sys

# for login in confluence
import xmlrpc.client

import os
import collections
import imp
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import sys

Emails = []


def check_time(start_day):
    start_time = datetime.datetime.strptime(start_day.decode(), '%Y-%m-%d')

    current_time = datetime.datetime.now()

    return (current_time - start_time).days


# def mkdir(path):
#     path = path.strip()
#
#     path = path.rstrip("\\")
#
#     isExists = os.path.exists(path)
#
#     if not isExists:
#         print(path + ' create successfully!')
#         os.makedirs(path)
#         return True
#     else:
#         print(path + ' exists!')
#         return False


def makeTableContentList(table):
    result = []
    allrows = table.findAll('tr')
    #print allrows

    for row in allrows:
        line = []
        #result.append(row)
        # exclude the strike one
        # if row.findAll('s'):
        #     continue

        allcols = row.findAll('td')
        rowIndex = 0
        for i in allcols:
            if i.findAll('div'):
                line.append(i.div.text.encode())

            else:
                line.append(i.text.encode())


        # print "rowIndex = ",rowIndex
        # print "allcols = ",allcols

        # for col in allcols:
        #     # print "col",col
        #     thestrings = [unicode(s) for s in col.findAll(text=True)]
        #     thetext = ''.join(thestrings)
        #
        #     result[-1].append(thetext)
            rowIndex += 1
        result.append(line)
    return result

def get_all_email(ID,type):
    login_page = "https://confluence.englishtown.com/"
    devive_page = "https://confluence.englishtown.com/pages/viewpage.action?pageId=673644924"
    driver = webdriver.PhantomJS()
    #driver = webdriver.Firefox()
    driver.get(login_page)
    driver.find_element_by_id('os_username').send_keys("ming.xiesh")
    driver.find_element_by_id('os_password').send_keys("Good_Luck777")
    driver.find_element_by_id('loginButton').click()
    driver.get(devive_page)
    print (driver.title)

    if type == "Android":
        path = "//div[2]/table/tbody/tr[{}]/td[8]/div//a"
    elif type == "IOS":
        path = "//div[3]/table/tbody/tr[{}]/td[6]/div//a"
    if ID:
        print(ID)
        for id in ID:
            print('each')
            print(id)

            ele = driver.find_element_by_xpath(path.format(id))

            time.sleep(1)
            print (ele.text.replace(" ",".")+"@ef.com")
            Emails.append(ele.text.replace(" ",".")+"@ef.com")
    driver.quit()
    print(Emails)




def loadConfluencePage(pageID):
    # login Confluence
    CONFLUENCE_URL = "https://confluence.englishtown.com/rpc/xmlrpc"
    CONFLUENCE_USER_NAME = "ming.xiesh"  # use your Confluence user Name
    CONFLUENCE_PASSWORD = "Good_Luck777"  # use your Confluence password

    # get this from the page url while editing
    # e.g. ../editpage.action?pageId=132350005 <-- here
    # PAGE_ID = "4686604"

    client = xmlrpc.client.Server(CONFLUENCE_URL, verbose=0)
    auth_token = client.confluence2.login(CONFLUENCE_USER_NAME, CONFLUENCE_PASSWORD)
    page = client.confluence2.getPage(auth_token, pageID)

    htmlContent = page['content']

    client.confluence2.logout(auth_token)

    return htmlContent


def count(item):
    result = {}
    for each in item:
        print(each.decode())
        if each not in result:
            result[each] = 0
        result[each] += 1
    return result


def sort_by_count(d):
    d=collections.OrderedDict(sorted(list(d.items()),key = lambda t: -t[1]))
    return d

def check_tables(result):

    index = 1
    ID = []
    for kk in result[1:]:
        print(kk[-3].decode())

        if kk[-3].decode() != "\xa0" and kk[-2].decode() != "\xa0":
            #
            # print (kk[-2].decode())
            # print (check_time(kk[-2]))

            if check_time(kk[-2]) > 60:
                # print ("why")
                ID.append(index)
                print("ok %s" % (kk[0]))
                # print("nok %s" % (kk[-2]))
                # print("nok %s" % (kk[-3]))
        else:
            pass

        index = index + 1

    return ID
        # print result




def main():

    pageID = "673644924"
    htmlContent = loadConfluencePage(pageID)

    soup = BeautifulSoup(htmlContent)
    #print soup.prettify()

    tables = soup.findAll('table')



    types = ["Android","IOS"]

    for type in types:
        if type == "Android":
            Android_result = makeTableContentList(tables[0])
            print(Android_result)
            ID=check_tables(Android_result)
        elif type =="IOS":
            IOS_result = makeTableContentList(tables[1])
            ID=check_tables(IOS_result)
        print (ID)
        get_all_email(ID, type)


    #     makeFile(result)
    #         # print "result = "
    #         # print result
    #
    # print "Make Over! Have a nice day!"

    android_mobile_number = 0
    android_tablet_number = 0

    print("android number is: {}".format(len(Android_result) -1 ))

    type = []
    i =0
    for detail in Android_result:

        if i is not 0:
            print (detail)

            type.append(detail[5])
    #         # if table[7].fainAll('a class'):
    #         #     name = table[7].text
    #         #
    #         #     print name
    #         #
    #         #
    #         #
    #         # else:
    #         #     name = table[7].text
    #         #
    #         #     print name
    #
        if b'Tablet' in detail:
            android_tablet_number +=1
        if  b'Phone' in detail:
            android_mobile_number +=1

        #


        i +=1

    print("tablet number is : {}".format(android_tablet_number))
    print("mobile number is : {}".format(android_mobile_number))
    #
    ios_mobile_number = len(IOS_result) - 1
    print("ios phone is: {}".format(ios_mobile_number))

    print(type)
    ll =count(type)

    print(ll)
    gg = sort_by_count(ll)
    print(gg)

if __name__ == "__main__":
    main()