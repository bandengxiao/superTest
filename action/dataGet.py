import json
import os

from ruamel.yaml import YAML

from conf.globalConf import globalConf


class dataGet():

    @staticmethod
    def getYamlData(fileName,key):
        #获取文件绝对路径
        filePath=globalConf.fileBasePath+"%s%s" % (os.sep,fileName)
        #读取数据
        with open(filePath,mode='r',encoding='utf-8') as file:
            yamlData=file.read()
            yaml=YAML(typ='safe')
            #获取指定数据
            data=yaml.load(yamlData)['cases'][key]

            case_data=dict.values(data)
            case_num=len(case_data)
            print(case_data)
            caseName=[]
            inputData=[]
            expectResult=[]
            expectDB=[]
            tuples=()
            for every_case in case_data:
                caseName.append(every_case["caseName"])
                inputData.append(json.dumps(every_case["inputData"]))
                expectResult.append(every_case["expected_result"])
                expectDB.append(every_case["expected_DB_data"])
                # tuples=(every_case["caseName"],every_case["inputData"],every_case["expected_result"],every_case["expected_DB_data"])
            input_list = list(zip(caseName, inputData, expectResult, expectDB,))
            file.close()
            # print(list(tuples))
            print(input_list)
            return input_list

            # for i in range(1,len(data)+1):
            #     caseName.append(str(data[str(i)]['caseName']))
            #     #inputData.append(data[str(i)]['inputData'])
            #     inputData.append(data[str(i)]['inputData'])
            #     #print(json.dumps(data[str(i)]['inputData']))
            #     expectResult.append(data[str(i)]['expected_result'])
            #     expectDB.append(data[str(i)]['expected_DB_data'])
            #
            # listData = list(zip(caseName, inputData, expectResult, expectDB))
            # file.close()
            #
            # return listData
            #print(list(zip(caseName, inputData, expectResult, expectDB)))

    @staticmethod
    def convertInputData(data):
        inputData={}
        for key,val in dict.items(data):
            if key == 'objective':
                print(val)


if __name__ == '__main__':
   dataGet.getYamlData('Test_ad_create.yaml','normal')

