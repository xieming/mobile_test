__author__ = 'anderson'

import lib.Utils as U
import GetDevice


def check_environment():
    appium = U.cmd("appium -v")
    appium_version = appium.stdout.readlines()[0].strip()
    if '1.' not in appium_version:
        U.Logging.error('appium not in computer')
        exit()
    else:
        U.Logging.info('appium version is %s ' %appium_version)

    if not GetDevice.get_device():
        U.Logging.error('the computer is not connected to any devices')
        exit()
    else:
         U.Logging.info('Device is connecting')

if __name__ == '__main__':
    check_environment()