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
# driver = webdriver.Firefox()
driver = webdriver.Ie()
driver.implicitly_wait (20)
driver.get ("http://127.0.0.1/grwl/Login.aspx")
driver.maximize_window ()
# 获取当前窗口句柄
handle = driver.current_window_handle

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
# pwd.send_keys (Keys.RETURN)

print("3"*20)
# driver.find_element_by_xpath('//*[@id="imgbtnLogin"]').click()

driver.find_element_by_id('imgbtnLogin').send_keys(Keys.ENTER)
# driver.find_element_by_css_selector('#imgbtnLogin').click()


time.sleep(2)
# cookies = driver.get_cookies ()
# print(cookies) #ie下存在问题
# driver.find_element_by_xpath('//*[@id="TreeView1t1"] and @title="合同发起"]').click()
# driver.find_element_by_css_selector('#TreeView1n1 > img:nth-child(1)').click()
# 展开合同发起
# ActionChains(driver).move_by_offset(38, 168).click().perform()
driver.find_element_by_id('TreeView1n1').send_keys(Keys.ENTER)
print("4"*20)
#
# print("!"*15)
# 点击合同发起
t.sleep(1)
driver.find_element_by_id('TreeView1t3').send_keys(Keys.ENTER)    # 开始 合同发起
print("5"*20)
driver.switch_to.frame('main_body')
driver.find_element_by_id('btnAdd').send_keys(Keys.ENTER)      # 添加
print("6"*20)

sel_1 = driver.find_element_by_xpath('//*[@id="searchcn10291"]')
Select(sel_1).select_by_index(5)  # 选择总部合同
sel_2 = driver.find_element_by_xpath('//*[@id="searchcn10270"]')
Select(sel_2).select_by_index(9)  # 选择合同模板
t.sleep(1)
sel_3 = driver.find_element_by_xpath('//*[@id="searchcn10272"]')
sel_3.send_keys(data + "__test1")    # 填写合同名称
t.sleep(1)
sel_1 = driver.find_element_by_xpath('//*[@id="searchcn10273"]')
Select(sel_1).select_by_index(5)  # 选择合同类型

# 选择缔约方

driver.find_element_by_id('searchcn10274img').send_keys(Keys.ENTER)
# handles = driver.window_handles
# print(handle, handles)
# # 获取新窗口
# new_handle = None
# for handle in handles:
#     if handle != handle:
#         new_handle = handle
#
# # 输出当前窗口句柄（
# # print ('switch to ', handle)
# driver.switch_to.window(new_handle)
driver.switch_to.frame('form1')
try:
    driver.find_element_by_id('xgvData_DXDataRow0').send_keys(Keys.ENTER)
except:
    print("未执行1" * 15)
try:
    driver.find_element_by_id('btnSearchSelect').send_keys(Keys.ENTER)
except:
    print("未执行2" * 15)

print("#"*15)
