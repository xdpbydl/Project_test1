# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time, csv, random
from selenium.webdriver.common.by import By
import time as t

# 无头浏览器
# options = Options ()
# options.headless = True
# driver = webdriver.Firefox (options=options)
driver = webdriver.Firefox ()
# driver = webdriver.Ie()
driver.implicitly_wait (20)
driver.get ("http://127.0.0.1/grwl/Login.aspx")
driver.maximize_window ()


# 输入
txtUser = driver.find_element_by_xpath ('//*[@id="txtUser"]')
txtUser.clear()
txtUser.send_keys ('ZCAdmin')

# 使用JS来输入,对于 密码可能存在问题
# js_value = 'document.getElementById("txtPwd1").value="1"'
# driver.execute_script(js_value)

driver.switch_to.active_element.send_keys(Keys.TAB)
time.sleep(0.3)
driver.switch_to.active_element.send_keys('1')
time.sleep(0.3)


# js = 'document.getElementById("txtPwd1").removeAttribute("readonly");'
# driver.execute_script(js)
# t.sleep(3)
# pwd = driver.find_element_by_xpath ('//*[@id="txtPwd1"]')
# pwd.clear()
# pwd.send_keys('aaaa')
# # pwd.send_keys (Keys.RETURN)
driver.find_element_by_xpath('//*[@id="imgbtnLogin"]').click()

t.sleep(3)
cookies = driver.get_cookies ()
# print(cookies) #ie下存在问题
driver.find_element_by_css_selector('#TreeView1n1 > img:nth-child(1)').click()
driver.find_element_by_css_selector('#TreeView1t3').click()     #合同发起
driver.switch_to_frame ('mainFrame')
# driver.find_element_by_css_selector('#btnAdd').click()      #添加
driver.find_element_by_xpath("/html/body/form/div[5]/div[2]/table/tbody/tr/td/span/input[1]").click()
print("#"*15)
