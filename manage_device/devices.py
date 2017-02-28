from bs4 import BeautifulSoup
import numpy as np
from utils import check_time, format_email_address_for_user
from login import login
from globals import MAX_DAY

device_overtime_information = {}


def makeTableContentList(table):
    result = []
    allrows = table.findAll('tr')
    # print allrows

    for row in allrows:
        line = []
        allcols = row.findAll('td')
        for i in allcols:
            print(i)
            if i.findAll('div'):
                line.append(i.div.text.encode().decode())

            else:
                line.append(i.text.encode().decode())
        result.append(line)
    return result


def get_overtime_device_and_user():
    device_page = login()

    soup = BeautifulSoup(device_page, "lxml")
    tables = soup.findAll('table')

    Android_table = makeTableContentList(tables[0])
    Android_table.pop(0)

    android_array = np.array(Android_table)
    print(android_array)

    for i in range(len(Android_table)):
        if android_array[i][7] != "\xa0" and android_array[i][8] != "\xa0":
            if check_time(android_array[i][8]) > MAX_DAY:
                print(android_array[i][7].strip())
                device_overtime_information[android_array[i][1].strip()] = android_array[i][7].strip()

    ios_table = makeTableContentList(tables[1])
    ios_table.pop(0)

    ios_array = np.array(ios_table)
    print(ios_array)

    for i in range(len(ios_table)):
        if ios_array[i][5] != "\xa0" and ios_array[i][6] != "\xa0":
            if check_time(ios_array[i][6]) > MAX_DAY:
                print(ios_array[i][5].strip())
                device_overtime_information[ios_array[i][1].strip()] = ios_array[i][5].strip()


if __name__ == '__main__':
    get_overtime_device_and_user()
    format_email_address_for_user(device_overtime_information)
    print(device_overtime_information)
