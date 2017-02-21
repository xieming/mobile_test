from

class Build_jenkins:

    def __init__(self):
        self.Jenkins_download_url = JENKINS_HOST + "/view/Engage/job/{}/lastSuccessfulBuild/api/json".format(current_app_info.app_job)


    def get_build(self):



    def download_build(self):