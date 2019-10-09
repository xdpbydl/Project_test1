import random
import requests
import re

'''
利用访问http://icanhazip.com/返回的IP进行测试
说明：利用的http://icanhazip.com/返回的IP进行校验，如返回的是代理池的IP，说明代理有效，否则实际代理无效
'''

# 代理ip池
PROXIES_NEW = {}

lens = len(PROXIES_NEW['https'])
print(lens)
num = 1
while num <= lens:


    try:
        requests.adapters.DEFAULT_RETRIES = 3
        proxies = PROXIES_NEW['https']

        IP = random.choice(proxies)
        # print(IP)
        # print(type(IP))
        b = re.findall('//(\d+\.\d+\.\d+\.\d+):', IP)[0]
        b = b.replace('.', '')
        print(b)
        # thiProxy = "http://" + IP
        # thisIP = "".join(IP.split(":")[0:1])
        # print(thisIP)
        res = requests.get(url="http://icanhazip.com/", timeout=8, proxies={"https": "https://113.140.1.82:53281"})
        proxyIP = res.text
        # print(proxyIP)
        a = proxyIP.replace('.', '')
        print(a)
        if int(a) == int(b):
            print("代理IP:'" + proxyIP + "'有效！")
        else:
            print("返回不是代理池中的ip，代理IP无效！")
    except:
        print("代理IP无效！")
        print(111)
    # else:
    #     print('success')
    num += 1
