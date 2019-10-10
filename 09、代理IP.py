# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import subprocess as sp
from lxml import etree
import requests
import random
import re


def get_proxys(page=1):
    # requests的Session可以自动保持cookie,不需要自己维护cookie内容
    S = requests.Session()
    # 西祠代理高匿IP地址
    target_url = 'http://www.xicidaili.com/nn/%d' % page
    # 完善的headers
    target_headers = {'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                      'Referer': 'http://www.xicidaili.com/nn/',
                      'Accept-Encoding': 'gzip, deflate, sdch',
                      'Accept-Language': 'zh-CN,zh;q=0.8',
                      }
    # get请求
    target_response = S.get(url=target_url, headers=target_headers)
    # utf-8编码
    target_response.encoding = 'utf-8'
    # 获取网页信息
    target_html = target_response.text
    # 获取id为ip_list的table
    bf1_ip_list = BeautifulSoup(target_html, 'lxml')
    bf2_ip_list = BeautifulSoup(str(bf1_ip_list.find_all(id='ip_list')), 'lxml')
    ip_list_info = bf2_ip_list.table.contents
    # 存储代理的列表
    proxys_list = []
    # 爬取每个代理信息
    for index in range(len(ip_list_info)):
        if index % 2 == 1 and index != 1:
            dom = etree.HTML(str(ip_list_info[index]))
            ip = dom.xpath('//td[2]')
            port = dom.xpath('//td[3]')
            protocol = dom.xpath('//td[6]')
            proxys_list.append(protocol[0].text.lower() + '#' + ip[0].text + '#' + port[0].text)
    # 返回代理列表
    return proxys_list


# def check_ip(proxies):
#     url = "http://www.baidu.com/"
#     # proxies = {"http": "http://x.x.x.x:端口号码"}
#     # 空白位置为测试代理ip和代理ip使用端口
#     # print(proxies)
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         # 响应头
#         res = requests.get(url, proxies=proxies, timeout=8, headers=headers)
#         # 发起请求
#         code = res.status_code
#         print(code)  # 返回响应码
#         if code == 200:
#             print(str(proxies.values()) + '可用')
#     #     else:
#     #         print('不可用返回代码%s' % code)
#     except:
#
#         print(str(proxies.values()) + '不可用!!!!!!!!!!!!!')

def check_ip(a):
    proxies = {"%s" % a[0]: "%s://%s:%s" % (a[0], a[1], a[2])}
    # print(type(proxies))
    try:
        requests.adapters.DEFAULT_RETRIES = 3

        res = requests.get(url="http://ip.webmasterhome.cn/", timeout=8, proxies=proxies)
        ccc = res.json()
        print(ccc)
        proxyIP = ccc



        print('##########'*20)
        print(proxyIP)
        print(type(proxyIP), type(a[1]))
        code = res.status_code
        print(code,proxyIP)  # 返回响应码
        if (proxyIP == a[1]):
            print("代理IP:'" + proxyIP + "'有效！"*20)
        else:
            print("代理IP无效！")
    except:
        print("代理IP无效！！！！！！！")

if __name__ == '__main__':
    proxys_list = get_proxys(1)
# print(proxys_list)
for i in proxys_list:
    a = i.split('#')
    print(a)
    check_ip(a)


