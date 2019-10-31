# coding=utf-8

from selenium import webdriver
import time
import json


def get_cookies(test_url):
    # 保存cookies的文件
    file = 'cookies.json'
    # 打开需要获取cookies的网站
    driver = webdriver.Ie ()
    driver.implicitly_wait (5)
    driver.get (test_url)
    driver.maximize_window ()
    # 网站打开后，在时间内手动执行登录操作
    time.sleep (60)
    # 登录成功后，获取cookies并保存为json格式
    cookies = driver.get_cookies ()
    fp = open (file, 'w')
    json.dump (cookies, fp)
    fp.close ()
    # 关闭浏览器
    driver.close ()


if __name__ == "__main__":
    url = 'http://127.0.0.1/grwl/Login.aspx/'
    get_cookies (url)