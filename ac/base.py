import os

import requests
from pandas._libs import json
from ruamel.yaml import YAML
from ac.DB_hundler import DBcheck

from ac.dataGet import dataGet


from conf.globalConf import globalConf


class BaseTest():

    API=None
    cookie=None
    yaml = YAML()



    @staticmethod
    def getCookie():
        datas = {
            "name":"zhoumanzeng",
            "password":"123456"
        }
        response = requests.get('http://192.168.0.106:9999/getCookies', data=datas)
        data=response.content.decode('utf-8')
        jsonData = json.loads(data)
        cookie = 'ETMS_ACCESS_TOKEN='+jsonData['access_token']
        return cookie

    @staticmethod
    def setCookie():
        cookie = BaseTest.getCookie()
        globalConf.COOKIE=cookie

    @classmethod
    def setup_class(cls):
        cls.DB = DBcheck() #报错原因导入了模块没导入类 cls.__name__

        #先获取当前类名，然后拼路径
        dataFilePath= os.path.join(globalConf.DATA_FILE_PATH,'Test_ad_create.yaml')
        with open(dataFilePath,mode='r',encoding='utf-8') as file:
            yaml=YAML()
            yamlData = yaml.load(file.read())
            Api=yamlData['API']
            cls.API=Api
        #清数据库
        data = dataGet.get_clear_YamlData('Test_ad_create.yaml', 'DB_Clear')
        # cls.db.clear_tables(data)
        cls.DB.clear_tables(data)

        print("开始了")

    @classmethod
    def teardown_class(cls):
        cls.DB.close_conn()
        print('77777777777777777777777777777777777777777777')



    # def teardown_class(self):
    #     self.db.close_conn()
    #     print('关闭了')









if __name__ == '__main__':
    test = BaseTest()
    test.setup_class()