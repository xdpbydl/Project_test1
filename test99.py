from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('htp://f.python3.vip/webauto/sample4.html')