import os
import re
import subprocess
import time

current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))


class iosinformation():
    def exec_command(self, cmd):
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutdata, stderrdata) = result.communicate()
        # print("Result is:%s") % stdoutdata
        if (re.search("No device found", str(stdoutdata)) or re.search("Could not connect", str(stdoutdata))):
            print "Please connet it agian, or add permission like: brew install libimobiledevice --HEAD,sudo chmod -R 777 /var/db/lockdown/"
        else:
            return stdoutdata

    def Get_UUID(self):
        cmd = 'idevice_id -l'
        uuid = self.exec_command(cmd)
        return uuid

    def Get_Device_Name(self):
        cmd = 'ideviceinfo -k DeviceName'
        device_name = self.exec_command(cmd)
        return device_name

    def Get_Device_information(self):
        cmd = 'ideviceinfo -k ProductVersion'
        device_information = self.exec_command(cmd)
        return device_information

    def Get_Device_Product_type(self):
        cmd = 'ideviceinfo -k ProductType'
        product_type = self.exec_command(cmd)
        return product_type

    def List_All_Pakages(self, uuid):
        cmd = 'ideviceinstaller -u {0}'.format(uuid)

        print cmd
        all_pakages = self.exec_command(cmd)

        return all_pakages

    def List_All_Logs(self, uuid):
        all_logs = "idevicesyslog -u {0}".format(uuid)
        return all_logs

    def Take_Screenshot(self):
        current_dir = os.path.split(os.path.realpath(__file__))[0]
        cmd1 = "idevicescreenshot {0} + '/' + screenshot-DATE.tiff".format(current_dir)
        cmd2 = "sips - s format png {0}.tiff - -out {1}.png".format(current_time, current_time)
        self.exec_command(cmd1)
        print "ok"
        # self.exec_command(cmd2)

    def Install_Ipa(self, ipa):
        cmd = 'ideviceinstaller -i {0}'.format(ipa)
        result = self.exec_command(cmd)
        return result

    def Uninstall_Ipa(self, appid):
        cmd1 = 'ideviceinstaller -l'
        cmd2 = 'ideviceinstaller -U {0}'.format(appid)
        result = self.exec_command(cmd1)
        appids=[]
        for id in result.split('\n'):
            if re.search('-',id):
                str = id[0:id.find("-")].strip()
                appids.append(str)

            else:
                pass
        print appids
        if appid in appids:
            result = self.exec_command(cmd2)
        else:
            print "The appid dosen't exit in the devices"



        # cmd2 = 'ideviceinstaller -u appid'.format(appid)
        # result = self.exec_command(cmd)
        # return result


def main():
    ios = iosinformation()

    uuid = ios.Get_UUID()
    print " uuid is {0}".format(uuid)
    device = ios.Get_Device_Name()
    print " device is {0}".format(device)
    device_info = ios.Get_Device_information()
    print " device_info is {0}".format(device_info)
    product_type = ios.Get_Device_Product_type()
    print " product_type is {0}".format(product_type)
    # all_pakagas = ios.List_All_Pakages(uuid)
    # print " all_pakagas is {0}".format(all_pakagas)
    ios.Take_Screenshot()
    ios.Install_Ipa('/Users/anderson/testcode/python/flask/uploads/englishtown_corporate_daily-190-2016.07.15.ipa')
    #ios.Uninstall_Ipa("com.ef.engage.englishtown.uat.dailydebug")



if __name__ == '__main__':
    main()