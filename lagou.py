#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup

# for change encoding
import sys

# for login in confluence
import xmlrpclib

import os


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
            if i.find('p'):
                line.append(i.p.text.encode('utf-8'))
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

    for table in tables:
        #print table
        result = makeTableContentList(table)
        print result
    #     makeFile(result)
    #         # print "result = "
    #         # print result
    #
    # print "Make Over! Have a nice day!"


if __name__ == "__main__":
    main()