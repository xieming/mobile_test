import configparser
import os
import time
import yaml

START_TIME = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
current_dir = os.path.split(os.path.realpath(__file__))[0]
WAIT_TIME = 8

conf_path = current_dir + "/contentini.conf"
yaml_path = current_dir + "/settings.yml"


CONFIG_READ = configparser.ConfigParser()
CONFIG_READ.read(conf_path)


PLATFORM= CONFIG_READ.get("plantform", "current_plantform")
PROJECT= CONFIG_READ.get("project", "current_project")
ENV = CONFIG_READ.get("envs", "current_env")
PRODUCT = CONFIG_READ.get("product", "current_product")



build_path = current_dir + "/builds/{}/{}/{}".format(PLATFORM, PROJECT, PRODUCT)
class AppPath:
    """class for client Ui test - AppPath parameter"""

    @staticmethod
    def get_app_filename(path):
        for dir_path, dir_names, file_names in os.walk(path):
            for name in file_names:
                if os.path.splitext(name)[1] == '.apk':
                    file_name = os.path.join(dir_path, name)

        return file_name




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










