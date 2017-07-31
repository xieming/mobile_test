from devicemanage import open_genemotion
from servermanage import start_appium_server,close_appium_server,kill_adb_port
from apkmanage import download_apk
from autotest.public.utils import start_process_by_command


def setup_env():
    download_apk()
    open_genemotion()
    start_appium_server()
    #kill_adb_port()


def clear_catch(package):
    cmd = "adb shell pm clear {}".format(package)
    start_process_by_command(cmd)
