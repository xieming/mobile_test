
import os
import subprocess
import re


def exec_command(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (stdoutdata, stderrdata) = result.communicate()
    if (re.search("error", str(stdoutdata))):
        print "error occur!"
    else:
        return stdoutdata

def get_url(url):
    cmd = 'curl -O {0}'.format(url)
    exec_command(cmd)

url = "http://www.listeningexpress.com/englishsongs/72/02 Rhythm Of Rain.mp3"

get_url(url)