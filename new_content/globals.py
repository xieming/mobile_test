import configparser
import os
import time
import yaml

START_TIME = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
current_dir = os.path.split(os.path.realpath(__file__))[0]

conf_path = current_dir + "/contentini.conf"
yaml_path = current_dir + "/settings.yml"

CONFIG_READ = configparser.ConfigParser()
CONFIG_READ.read(conf_path)


ENV = CONFIG_READ.get("envs", "current_env")
PRODUCT = CONFIG_READ.get("product", "product")
USERNAME = CONFIG_READ.get("user", "name")
PASSWORD = CONFIG_READ.get("user", "pwd")

class YAML():
    # Write YAML file
    @staticmethod
    def write_yml(save_path, data):
        with open(save_path, 'w', encoding='utf8') as outfile:
            try:
                yaml.safe_dump(data, outfile, default_flow_style=False, allow_unicode=True)
            except yaml.YAMLError as exc:
                print(exc)

            # Read YAML file
    @staticmethod
    def read_yml(load_path):
        with open(load_path, 'r') as stream:
            try:
                data_loaded = yaml.safe_load(stream)
                return data_loaded
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def read_settings_yml():
        return YAML.read_yml(yaml_path)

HOST = "http://" + YAML.read_settings_yml()['env'][ENV] + ".englishtown.com"
service_parameter = YAML.read_settings_yml()[PRODUCT]

LOGIN_PATH = YAML.read_settings_yml()['api']['login']
STUDY_CONTEXT_PATH = YAML.read_settings_yml()['api']['studycontext']
COURSE_STRUCTURE_PATH = YAML.read_settings_yml()['api']['coursestructure']
ACTIVITY_CONTENT_PATH = YAML.read_settings_yml()['api']['activitycontent']



session_id = ""
token = ""
level_id = ""
activity_id = []

LOGIN_PARAMS = {
    "serviceRequest":
        {
            "appVersion": service_parameter['appVersion'],
            "password": PASSWORD,
            "platform": service_parameter['platform'],
            "productId": service_parameter['productId'],
            "userName": USERNAME
        }
}


STUDY_CONTEXT_PARAMS = {
    "serviceRequest":
        {
            "appVersion": service_parameter['appVersion'],
            "culturecode": service_parameter['culturecode'],
            "platform": service_parameter['platform'],
            "productId": service_parameter['productId'],
            "sessionId": session_id,
            "token": token
        }
}

COURSE_STRUCTURE_PARAMS = {
    "serviceRequest":
        {
            "level": level_id,
            "countryCode": service_parameter['countryCode'],
            "partnerCode": service_parameter['partnerCode'],
            "siteVersion": service_parameter['siteVersion'],
            "appVersion": service_parameter['appVersion'],
            "culturecode": service_parameter['culturecode'],
            "platform": service_parameter['platform'],
            "productId": service_parameter['productId'],
            "sessionId": session_id,
            "token": token
        }
}








