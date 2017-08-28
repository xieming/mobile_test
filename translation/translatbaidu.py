import requests
import hashlib

import random
import json

appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'

myurl = '/api/trans/vip/translate'
host = 'http://api.fanyi.baidu.com'
q = 'where are you going?'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)


def md5hex(word):
    sign = appid + word + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode())
    return m1.hexdigest()


def trans(word, sign, fr='en', to='zh'):
    word_num = len(word)
    if word_num > 160:
        print("over 160")
    else:

        url = myurl + '?appid=' + appid + '&q=' + word + '&from=' + fr + '&to=' + to + '&salt=' + str(
            salt) + '&sign=' + sign

        try:
            result = requests.post(host + url)
            if result.status_code == 200:
                trans_data = json.loads(result.text)
                trans_data = trans_data['trans_result'][0]['dst']
                print(trans_data)
            else:
                print("please check you url")
        except:
            print("error")


if __name__ == '__main__':
    ss = md5hex(q)
    trans(q, ss)
