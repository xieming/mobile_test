from devicemanage import open_genemotion
from servermanage import start_appium_server,close_appium_server,kill_adb_port


def setup_env():
    kill_adb_port()
    open_genemotion()
    start_appium_server()
