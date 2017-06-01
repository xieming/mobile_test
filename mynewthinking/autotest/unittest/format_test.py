import yaml

yaml_str = """
name: 灰蓝
age: 0
job: Tester
"""

y = yaml.load(yaml_str)
print (y)



python_obj = {"name": u"灰蓝",
              "age": 0,
              "job": "Tester"
              }

y = yaml.dump(python_obj, default_flow_style=False)
print (y)