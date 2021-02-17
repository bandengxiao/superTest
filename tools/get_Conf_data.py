import configparser
import os
from configparser import RawConfigParser


def getConfigData(fileName,setction,key):

    parser = configparser.ConfigParser()
    #parser = configparser.RawConfigParser
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'%s%s' % (os.sep,'conf')+os.sep+fileName

    parser.read(path,encoding='utf-8')
    # print(parser.get(setction,key))
    return parser.get(setction,key,raw=True)






if __name__ == '__main__':
    getConfigData('db.conf','db','host')