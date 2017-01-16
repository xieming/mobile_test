#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup

# for change encoding
import sys

# for login in confluence
import xmlrpclib

import os
import collections


def mkdir(path):
    path = path.strip()

    path = path.rstrip("\\")

    isExists = os.path.exists(path)

    if not isExists:
        print path + ' create successfully!'
        os.makedirs(path)
        return True
    else:
        print path + ' exists!'
        return False


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
                line.append(i.div.text.encode('utf-8'))

            else:
                line.append(i.text.encode('utf-8'))

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


def makeFile(tableContentList):
    className = tableContentList[0][0]

    outputFile = file("output/" + className + ".cs", "w")

    # start to write file

    # write header
    outputFile.write("using UnityEngine;\n")
    outputFile.write("using System.Collections;\n\n")
    outputFile.write("public class " + className + "\n{\n")

    # write members
    rowCounter = 0
    for row in tableContentList:
        if row and rowCounter > 0:  # rowCounter == 0 is className

            # --------format---------
            beginSpaces = "    public    "
            typeString = "{:<12}".format(row[0])
            memberName = "{:<30}".format(row[1] + ";")
            comments = ""

            if len(row[2]) > 1:
                comments = "    //" + row[2]

            s = beginSpaces + typeString + memberName + comments + "\n"

            outputFile.write(s)

        rowCounter += 1

    # write tail
    outputFile.write("}\n")

    outputFile.close()


def setDefaultEncodingUTF8():
    reload(sys)
    sys.setdefaultencoding('utf-8')


def loadConfluencePage(pageID):
    # login Confluence
    CONFLUENCE_URL = "https://confluence.englishtown.com/rpc/xmlrpc"
    CONFLUENCE_USER_NAME = "ming.xiesh"  # use your Confluence user Name
    CONFLUENCE_PASSWORD = "Good_Luck777"  # use your Confluence password

    # get this from the page url while editing
    # e.g. ../editpage.action?pageId=132350005 <-- here
    # PAGE_ID = "4686604"

    client = xmlrpclib.Server(CONFLUENCE_URL, verbose=0)
    auth_token = client.confluence2.login(CONFLUENCE_USER_NAME, CONFLUENCE_PASSWORD)
    page = client.confluence2.getPage(auth_token, pageID)

    htmlContent = page['content']

    client.confluence2.logout(auth_token)

    return htmlContent


def count(item):
    result = {}
    for each in item:
        print each
        if each not in result:
            result[each] = 0
        result[each] += 1
    return result


def sort_by_count(d):
    d=collections.OrderedDict(sorted(d.items(),key = lambda t: -t[1]))
    return d


def main():
    # change Encoding to UTF8
    #setDefaultEncodingUTF8()

    # htmlContent = loadConfluencePage(pageID)
    # print htmlContent


    #make output directory
    mkdir(sys.path[0] + "/output")

    # there are two pages contain data model
    pageID = "673644924"



    print "Make data in page with id: ", pageID

    htmlContent = loadConfluencePage(pageID)

    soup = BeautifulSoup(htmlContent)
    #print soup.prettify()

    tables = soup.findAll('table')

    tables.pop()
    print len(tables)

    result_table = []
    for table in tables:
        #print table
        result = makeTableContentList(table)
        print result
        result_table.append(result)
    #     makeFile(result)
    #         # print "result = "
    #         # print result
    #
    # print "Make Over! Have a nice day!"

    android_mobile_number = 0
    android_tablet_number = 0

    print "androd number is: {}".format(len(result_table[0]) -1 )

    type = []
    i =0
    for detail in result_table[0]:

        if i is not 0:

            type.append(detail[5])
            # if table[7].fainAll('a class'):
            #     name = table[7].text
            #
            #     print name
            #
            #
            #
            # else:
            #     name = table[7].text
            #
            #     print name

        if 'Tablet' in detail:
            android_tablet_number +=1
        if  'Phone' in detail:
            android_mobile_number +=1

        #


        i +=1

    print "tablet number is : {}".format(android_tablet_number)
    print "mobile number is : {}".format(android_mobile_number)

    ios_mobile_number = len(result_table[0]) - 1
    print "ios phone is: {}".format(ios_mobile_number)

    print type
    ll =count(type)

    print ll
    gg = sort_by_count(ll)
    print gg

if __name__ == "__main__":
    main()