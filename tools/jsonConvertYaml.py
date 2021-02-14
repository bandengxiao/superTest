import json

from ruamel import yaml
from ruamel.yaml import YAML


class jsonConver():

    @staticmethod
    def jsonConvertToYaml(): #json数据转化为yaml数据
        file=open('convertData.json', mode='r', encoding='utf-8')
        data=file.read()
        jsonData=json.loads(data)

        file.close()
        #创建yaml对象

        with open('convertYaml.yaml', mode='w', encoding='utf-8') as file:
            file.write(yaml.dump(jsonData,allow_unicode=True))
            file.close()

if __name__ == '__main__':
        jsonConver.jsonConvertToYaml()