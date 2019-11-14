# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Ie()
driver.get("http://www.baidu.com")
time.sleep(0.5)

driver.find_element_by_id("kw").send_keys("Selenium2")
#driver.find_element_by_name("wd").send_keys("Selenium2")
driver.find_element_by_id("su").click()
