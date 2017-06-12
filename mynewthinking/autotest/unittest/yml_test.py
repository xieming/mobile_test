import yaml


class YAML():
    # Write YAML file
    def write_yml(self, save_path, data):
        with open(save_path, 'w', encoding='utf8') as outfile:
            try:
                yaml.safe_dump(data, outfile, default_flow_style=False, allow_unicode=True)
            except yaml.YAMLError as exc:
                print(exc)

            # Read YAML file

    def read_yml(self, load_path):
        with open(load_path, 'r') as stream:
            try:
                data_loaded = yaml.safe_load(stream)
                return data_loaded
            except yaml.YAMLError as exc:
                print(exc)
# def main():
#     yamls = YAML()
#     result = yamls.read_yml("/Users/anderson/testcode/mynewthinking/autotest/unittest/test.yml")
#     print(result)
#     yaml_str = {
#     'name': '灰蓝',
#     'age': 0,
#     'job': 'Tester'
#     }
#     yamls.write_yml("/Users/anderson/testcode/mynewthinking/autotest/unittest/write_test.yml",yaml_str)
#
# if __name__ == '__main__':
#     main()

if __name__ == '__main__':
    yamls =YAML()
    # name = "fuck you"
    # result = yamls.read_yml("/Users/anderson/testcode/mynewthinking/autotest/unittest/test.yml")
    # final = result["LoginPage"]["Login"][0]["id"]
    # print(final)
    result = yamls.read_yml("/Users/anderson/testcode/mynewthinking/autotest/pages/pages.yml")["IOS"]["LoginPage"]
    print(result)
