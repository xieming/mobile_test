import os

current_dir = os.path.split(os.path.realpath(__file__))[0]

MAX_TIMES = 3
WAIT_TIME = 5

PLATFORM = "Android" # Android, IOS
PROJECT = "ENGAGE"  #TABLET,ENGAGE
PRODUCT = "englishtown"  # englishtown,corporate,smartenglish
ENV = "qa"      # qa,staging

build_path = current_dir + "/autotest/builds/{}/{}/{}".format(PLATFORM,PROJECT,PRODUCT)


class AppPath:
    """class for client Ui test - AppPath parameter"""

    @staticmethod
    def get_app_filename(path):
        for dir_path, dir_names, file_names in os.walk(path):
            for name in file_names:
                if os.path.splitext(name)[1] == '.apk':
                    file_name = os.path.join(dir_path, name)

        return file_name