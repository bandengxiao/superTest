
import logging.config

import os
import time

from tools import get_Conf_data


class loggerConfig():

    def __init__(self):
        self.strftime = time.strftime("%Y-%m-%d", time.localtime())
        self.fileName=str(self.strftime)+'-'+get_Conf_data.getConfigData('log.conf','conf','name')
        self.formats=get_Conf_data.getConfigData('log.conf','conf','format')
        self.leval=get_Conf_data.getConfigData('log.conf','conf','level')


    def get_logger(self):
        if self.leval == 'INFO':
            self.leval=logging.INFO
        else:
            self.leval=logging.INFO
        # logging.basicConfig(level=self.leval,format=self.formats)
        logger = logging.getLogger('superfans')
        logger.setLevel(level=self.leval)#logger也需要设置日志级别，如果不设置，不能成功写日志到文件
        handler=logging.FileHandler(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'%s%s%s' % (os.sep,'logs',os.sep)+self.fileName
                                    ,encoding='utf-8'
                                    ,delay=True
                                    )
        handler.setLevel(self.leval)
        formatter = logging.Formatter(self.formats)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger


log=loggerConfig().get_logger()

if __name__ == '__main__':
    log.warning('测试本类')