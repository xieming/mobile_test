import os

current_dir = os.path.split(os.path.realpath(__file__))[0]

MAX_TIMES = 3

WAIT_MINI_TIME = 1
WAIT_TIME = 5
WAIT_LONG_TIME = 10
WAIT_MAX_TIME = 20

PLATFORM = "Android"  # Android, IOS
PROJECT = "ENGAGE"  # TABLET,ENGAGE
PRODUCT = "englishtown"  # englishtown,corporate,smartenglish
ENV = "qa"  # qa,staging

build_path = current_dir + "/autotest/builds/{}/{}/{}".format(PLATFORM, PROJECT, PRODUCT)


class AppPath:
    """class for client Ui test - AppPath parameter"""

    @staticmethod
    def get_app_filename(path):
        for dir_path, dir_names, file_names in os.walk(path):
            for name in file_names:
                if os.path.splitext(name)[1] == '.apk':
                    file_name = os.path.join(dir_path, name)

        return file_name


def get_current_package():
    package_name = {
        "englishtown": "com.ef.core.engage.englishtown",
        "corporate": "com.ef.core.engage.corporate",
        "smartenglish": "om.ef.core.engage.smartenglish"
    }[PRODUCT]
    return package_name
