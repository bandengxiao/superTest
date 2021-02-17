import json

import requests

from conf.globalConf import globalConf




def post(datas,url):

    header={
        "Cookie":globalConf.COOKIE,
        "Content-Type":"application/x-www-form-urlencoded"
    }

    return requests.post(url=url,data=datas,headers=header)

    # post = requests.post(url=url, headers=header, data=datas)
    #
    # return post


if __name__ == '__main__':
    print()