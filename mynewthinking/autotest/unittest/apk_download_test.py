
from globals import *

from autotest.public.jenkinshelper import Jenkins


import os

from ptest.assertion import assert_not_equals
from ptest.decorator import TestClass, Test

@TestClass(run_mode='singleline')
class DownloadApk:
    @Test()
    def download_engage_apk(self):
        jenkins = Jenkins(build_path)
        jenkins.download_build()
        build = [x for x in os.listdir(build_path)]
        assert_not_equals(build, [])