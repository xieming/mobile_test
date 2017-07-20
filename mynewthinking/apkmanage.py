from globals import *

from autotest.public.jenkinshelper import Jenkins



def download_apk():
    jenkins = Jenkins(build_path)
    jenkins.download_build()

# def current_apk_name():
#     apk = AppPath.get_app_filename(current_dir)
#     return apk

