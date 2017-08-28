import re
import requests
from globals import ENV,host,username,password
from yamlmanage import YAML


class REQUEST():
    token = None
    sessionId = None

    def get_token(self,username,password):
        path, data = YAML().get_api("login")
        data['serviceRequest']['userName']=username
        data['serviceRequest']['password'] = password

        url = host + path
        response = requests.post(url=url,json=data)
        print(response)

        if response.status_code == 200:
            print("login succuss")
            self.token= response.json()["serviceResponse"]["token"]
            self.sessionId=response.json()["serviceResponse"]["sessionId"]
        else:
            print("login fail, please check your account")

    def get_response(self,tag,level=20000524):
        path, data = YAML().get_api(tag)
        if self.sessionId is None or self.token is None:
            self.get_token(username,password)

        data['serviceRequest']['sessionId']=self.sessionId
        data['serviceRequest']['token'] = self.token
        if tag == "coursestructure":
            data['serviceRequest']['level'] = level

        url = host + path
        response = requests.post(url=url,json=data)
        if response.status_code == 200:
            if tag == "studycontext":
                result = response.json()["serviceResponse"]["context"]["blurbTranslations"]
            else:
                result = response.json()["serviceResponse"]["blurbTranslations"]

            print(result)
            return result

        else:
            print("fail")

def get_ids(obj):
    final = []
    for i in obj:
        final.append(i['id'])

    return final


if __name__ == '__main__':
    study = REQUEST().get_response("studycontext")
    print (get_ids(study))
    course = REQUEST().get_response("coursestructure")
    print(get_ids(course))




