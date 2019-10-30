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
driver.implicitly_wait (30)
driver.get ("http://localhost/grwl/Login.aspx/")

# 输入
txtUser = driver.find_element_by_xpath ('//*[@id="txtUser"]')
txtUser.clear()
txtUser.send_keys ('admin')

# 使用JS来输入,对于 密码可能存在问题
# js_value = 'document.getElementById("txtPwd1").value="1"'
# driver.execute_script(js_value)



js = 'document.getElementById("txtPwd1").removeAttribute("readonly");'
driver.execute_script(js)
t.sleep(3)
pwd = driver.find_element_by_xpath ('//*[@id="txtPwd1"]')
pwd.clear()
pwd.send_keys('1')
# pwd.send_keys (Keys.RETURN)
driver.find_element_by_xpath('//*[@id="imgbtnLogin"]').click()
