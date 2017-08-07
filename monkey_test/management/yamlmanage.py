import yaml
from globals import PLATFORM,current_dir,PRODUCT,PROJECT,ENV






class YAML():
    setting_path=current_dir + "/settings.yml"
    appium_config_path = current_dir + "/appium_config.yml"


# Write YAML file

    def write_yml(self,save_path,data):
        with open(save_path, 'w', encoding='utf8') as outfile:
            try:
                yaml.safe_dump(data, outfile, default_flow_style=False, allow_unicode=True)
            except yaml.YAMLError as exc:
                print(exc)

# Read YAML file


    def read_yml(self,load_path):
        with open(load_path, 'r') as stream:
            try:
                data_loaded = yaml.safe_load(stream)
                return data_loaded
            except yaml.YAMLError as exc:
                print(exc)

    def get_appium_config(self):
        return self.read_yml(self.appium_config_path)[PLATFORM]


    def get_package(self):
        return self.read_yml(self.setting_path)["package"][PRODUCT]

    def get_activity(self):
        return self.read_yml(self.setting_path)["activity"][PRODUCT]


    def get_users(self):
        users = self.read_yml(self.setting_path)[PROJECT][ENV][PRODUCT]
        print(users)
        return users









# if __name__ == '__main__':
#
#     yml = YAML()
#     files = yml.read_yml("/Users/anderson/testcode/mynewthinking/autotest/pages/pages.yml")
#     print(files)




