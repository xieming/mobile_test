__author__ = 'anderson'

import subprocess
import pandas as pd
import numpy as np
import yaml

def get_file():

    filename = './apks.yml'
    f = open(filename)
    s = yaml.load(f)
    f.close()
    print(s['apk'][0]['activity'])

def get_device_list():
    result = subprocess.check_output('VBoxManage list vms', shell=True).decode()
    device_list = result.split('\n')
    devices= np.array(device_list)
    print(devices)
    translated_dataframe = pd.DataFrame(devices)

    writer = pd.ExcelWriter('devices.xlsx')
    translated_dataframe.to_excel(writer,'android')
    writer.save()


if __name__ == '__main__':
    # get_device_list()
    get_file()