import yaml
from globals import  current_dir,host



class YAML():
    setting_path=current_dir + "/data.yml"



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

    def get_api(self,tag):
        content=self.read_yml(self.setting_path)
        path=content['servicepath']['path'] + tag
        data = content[tag]
        return path,data


if __name__ == '__main__':
    path,data = YAML().get_api("studycontext")
    print(path)
    print(data)
