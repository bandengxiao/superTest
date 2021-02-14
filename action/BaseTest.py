import os

import pytest
import requests
from pandas._libs import json
from ruamel.yaml import YAML

from conf.globalConf import globalConf


class baseTest():

    API=None
    cookie=None

    @staticmethod
    def getCookie():
        datas = {
            "name":"zhoumanzeng",
            "password":"123456"
        }
        response = requests.get('http://192.168.225.107:9999/getCookies', data=datas)
        data=response.content.decode('utf-8')
        jsonData = json.loads(data)
        cookie = 'ETMS_ACCESS_TOKEN='+jsonData['access_token']
        return cookie

    @staticmethod
    def setCookie():
        cookie = baseTest.getCookie()
        globalConf.COOKIE=cookie

    @classmethod
    def setup(cls):
        #先获取当前类名，然后拼路径
        dataFilePath= os.path.join(globalConf.DATA_FILE_PATH,cls.__name__+'.yaml')
        with open(dataFilePath,mode='r',encoding='utf-8') as file:
            yaml=YAML()
            yamlData = yaml.load(file.read())
            Api=yamlData['API']
            cls.API=Api




if __name__ == '__main__':
    baseTest.setup_class()