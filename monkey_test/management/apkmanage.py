from ptest.assertion import assert_not_equals

from globals import *
from public.jenkinshelper import Jenkins


def download_apk():
    jenkins = Jenkins(build_path)
    jenkins.download_build()

if __name__ == '__main__':
    jenkins = Jenkins(build_path)
    jenkins.download_build()
    build = [x for x in os.listdir(build_path)]
    assert_not_equals(build, [])




