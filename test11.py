# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
import time, csv, random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time as t
data3 = time.localtime()
data = '%d-%d-%d' % (data3.tm_year, data3.tm_mon, data3.tm_mday)
# 无头浏览器
# options = Options ()
# options.headless = True
# driver = webdriver.Firefox (options=options)
# driver = webdriver.Firefox ()
driver = webdriver.Ie()
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
# cookies = driver.get_cookies ()
# print(cookies) #ie下存在问题
# driver.find_element_by_xpath('//*[@id="TreeView1t1"] and @title="合同发起"]').click()
# driver.find_element_by_css_selector('#TreeView1n1 > img:nth-child(1)').click()
ActionChains(driver).move_by_offset(38, 168).click().perform()
#
# print("!"*15)
t.sleep(1)
driver.find_element_by_css_selector('#TreeView1t3').click()     # 合同发起
driver.switch_to.frame('main_body')
driver.find_element_by_css_selector('#btnAdd').click()      # 添加

sel_1 = driver.find_element_by_xpath('//*[@id="searchcn10291"]')
Select(sel_1).select_by_index(5)  # 选择总部合同
sel_2 = driver.find_element_by_xpath('//*[@id="searchcn10270"]')
Select(sel_2).select_by_index(9)  # 选择合同模板
sel_3 = driver.find_element_by_xpath('//*[@id="searchcn10272"]')
sel_3.send_keys(data + "__test1")    # 填写合同名称

sel_1 = driver.find_element_by_xpath('//*[@id="searchcn10273"]')
Select(sel_1).select_by_index(5)  # 选择合同类型

print("#"*15)
