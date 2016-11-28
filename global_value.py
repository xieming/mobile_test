import os
import re
import shutil
import subprocess
import time


URL = {
    "apk_old_old": "http://10.128.42.155:8080/view/Engage/job/engage-android-release/21/artifact/engage/build/outputs/apk/engage-englishtown-qa-release.apk",
    "apk_old": "http://10.128.42.155:8080/view/Engage/job/engage-android-release/35/artifact/engage/build/outputs/apk/engage-englishtown-qa-release.apk",
    "apk_new": "http://10.128.42.155:8080/view/Engage/job/engage-android-release/37/artifact/engage/build/outputs/apk/engage-englishtown-qa-release.apk"
}

# MD5_URL = {
#     old_apk: "",
#     new_apk: "",
# }

current_dir = os.path.split(os.path.realpath(__file__))[0]
report_path = current_dir + "/apk/"
old_path = current_dir + "/old/"
new_path = current_dir + "/new/"



