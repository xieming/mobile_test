__author__ = 'anderson'

import lib.Utils as U
import random
import platform


class Sp:
    def __init__(self, device):
        self.device = device

    def __start_driver(self, aport, bpport):
        """
        clear logcat and appium all process
        :return:
        """
        if platform.system() == 'Windows':

            import subprocess
            subprocess.Popen("appium -p %s -bp %s -U %s" %
                             (aport, bpport, self.device), shell=True)

        else:
            appium = U.cmd("appium -p %s -bp %s -U %s" %
                           (aport, bpport, self.device))  # start appium
            while True:
                appium_line = appium.stdout.readline().strip()
                U.Logging.debug(appium_line)
                if 'listener started' in appium_line:
                    break

    def start_appium(self):
        """
        start appium
        p:appium port
        bp:bootstrap port
        :return: return appium port parameters
        """

        aport = random.randint(4700, 4900)
        bpport = random.randint(4700, 4900)
        self.__start_driver(aport, bpport)

        U.Logging.debug(
            'start appium :p %s bp %s device:%s' %
            (aport, bpport, self.device))
        U.sleep(10)
        return aport

    def main(self):
        """
        :return: start appium
        """
        return self.start_appium()


if __name__ == '__main__':
    s = Sp('A7J5T15A28007700')
    s.main()