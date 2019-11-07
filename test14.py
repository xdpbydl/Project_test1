# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketang/")

# 定位首页管理按钮：id=blog_nav_contact
js1 = 'document.getElementById("blog_nav_contact").click();'
driver.execute_script(js1)

# 输入账号
js2 = 'document.getElementsByClassName("form-control")[0].value="上海-悠悠";'
driver.execute_script(js2)

# 输入密码
js3 = 'document.getElementsByClassName("form-control")[1].value="xxx";'
driver.execute_script(js3)

# 勾选记住密码
js4 = 'document.getElementsByName("custom-control-label")[0].click();'
driver.execute_script(js4)

# 点击登录按钮
js5 = 'document.querySelectorAll("#signin")[0].click();'
driver.execute_script(js5)