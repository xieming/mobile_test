import yaml
from globals import PLATFORM,current_dir,AppPath






class YAML():
    device_path=current_dir + "/autotest/public/device.yml"
    page_path = current_dir + "/autotest/pages/pages.yml"


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

    def current_device(self):
        return self.read_yml(self.device_path)[PLATFORM]


    def current_page(self,page):
        return self.read_yml(self.page_path)[PLATFORM][page]








# if __name__ == '__main__':
#
#     yml = YAML()
#     files = yml.read_yml("/Users/anderson/testcode/mynewthinking/autotest/pages/pages.yml")
#     print(files)




