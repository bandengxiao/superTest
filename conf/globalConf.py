import os


class globalConf():

    BasePath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    fileBasePath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]+"%s%s" % (os.sep,'data')

    COOKIE=''

    DATA_FILE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'%s%s' % (os.sep,'data')



if __name__ == '__main__':
     print(os.path.dirname(os.path.abspath(__file__)))
     print(globalConf.DATA_FILE_PATH)