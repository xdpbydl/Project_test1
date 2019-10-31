# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time, csv, random
from selenium.webdriver.common.by import By

# 无头浏览器
# options = Options ()
# options.headless = True
# driver = webdriver.Firefox (options=options)
driver = webdriver.Firefox ()
# driver = webdriver.Ie()
driver.implicitly_wait (30)
driver.get ("https://www.lagou.com/")

# 选择广州站
# driver.find_element_by_xpath ('/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/ul/li[4]/a').click ()
cty = '广州站'
cty1 = driver.find_element_by_xpath ('/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a')
cty2 = driver.find_element_by_xpath ('/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/ul/li[4]/a')

if cty1.text == cty:
    cty1.click ()
elif cty2.text == cty:
    cty2.click ()

# 输入关键词
key = driver.find_element_by_xpath ('//*[@id="search_input"]')
key.clear ()
key.send_keys ('JAVA高级')
key.send_keys (Keys.RETURN)
page_NO = driver.find_element_by_xpath ('/html/body/div[5]/div[2]/div[1]/div[3]/div[2]/div/span[5]').text

# 关闭广告
try:
    driver.find_element_by_xpath ('//*[@id="foot-fix-close"]').click ()
except:
    print("无广告…………")
    pass
# 获取当前窗口句柄
lagou_handle = driver.current_window_handle
output = open ('e:\data.csv', 'w', encoding='utf-8-sig', newline='')
for m in range (int (page_NO)):
    print ('第%d页数据爬取中' % (m + 1) + "--" * 10)
    for i in range (15):
        aa = '/html/body/div[5]/div[2]/div[1]/div[3]/ul/li[%d]' % (i + 1)
        try:
            position = driver.find_element_by_xpath (aa + '/div[1]/div[1]/div[1]/a/h3').text
            region = driver.find_element_by_xpath (aa + '/div[1]/div[1]/div[1]/a/span/em').text
            time_o = driver.find_element_by_xpath (aa + '/div[1]/div[1]/div[1]/span').text
            Abbreviation = driver.find_element_by_xpath (aa + '/div[1]/div[2]/div[1]/a').text
            salary = driver.find_element_by_xpath (aa + '/div[1]/div[1]/div[2]/div/span').text
            experience = driver.find_element_by_xpath (aa + '/div[1]/div[1]/div[2]/div').text
            introduce = driver.find_element_by_xpath (aa + '/div[1]/div[2]/div[2]').text
            keys = driver.find_element_by_xpath (aa + '/div[2]/div[1]').text
            welfare = driver.find_element_by_xpath (aa + '/div[2]/div[2]').text
        except:
            time_o, Abbreviation, salary, experience, introduce, keys, welfare = 0, 0, 0, 0, 0, 0, 0
            pass

        # # 滚动到指定元素
        time.sleep (1)
        new_page = driver.find_element_by_xpath (aa + '/div[1]/div[1]/div[1]/a/h3')
        driver.execute_script ("arguments[0].scrollIntoView(false);", new_page)
        new_page.click ()

        # 获取所有窗口句柄
        handles = driver.window_handles
        # print (handles)

        # 获取新窗口
        new_handle = None
        for handle in handles:
            if handle != lagou_handle:
                new_handle = handle

        # 输出当前窗口句柄（
        # print ('switch to ', handle)
        driver.switch_to.window (new_handle)

        Duty = driver.find_element (By.CLASS_NAME, 'job-detail').text

        time.sleep (random.randint (3, 5))
        driver.close ()
        time.sleep (random.randint (1, 3))
        # 切换回窗口
        driver.switch_to.window (lagou_handle)

        writer = csv.writer (output)
        writer.writerow ([position, region, time_o, Abbreviation, salary, experience, introduce, keys, welfare, Duty])
        print('第%d页,%d' % ((m + 1), i + 1) + "--" * 10)
        print (position, region, time_o, Abbreviation, salary, experience, introduce, keys, welfare, Duty)

    down = driver.find_element_by_xpath ('/html/body/div[6]/div/div[1]/div[2]/div[2]/p')
    driver.execute_script ("arguments[0].scrollIntoView(false);", down)
    time.sleep (random.randint (3, 5))
    driver.find_element (By.CLASS_NAME, 'pager_next').click ()

# driver.close ()
driver.quit ()

##################################################################################################
# elem_user = driver.find_element_by_name("userid")
# elem_user.clear()
# elem_user.send_keys("150881732061")
# elem_pwd = driver.find_element_by_name("psw")
# elem_pwd.send_keys("1y20050917@1")
# time.sleep(5)
# elem_pwd.send_keys(Keys.RETURN)
# time.sleep(3)
# driver.find_element_by_css_selector('input[value="进入系统"]').click()
# time.sleep(3)
# driver.find_element_by_css_selector("#A2").click()
# driver.find_element_by_css_selector(".WEBItc_list_con1 > ul:nth-child(1) > li:nth-child(9) > a:nth-child(1)").click()
# time.sleep(2)
#
# driver.switch_to_frame('mainFrame')
# driver.find_element_by_link_text('学生调班').click()
#
# aabb = '/html/body/div[1]/div[2]/div/table/tbody[1]/tr'
# no = 0
#
# output = open('data.csv', 'w', newline='')
# for m in range(200):
#     table = driver.find_element_by_id('xstb_list')
#     table_rows = len(table.find_elements_by_tag_name('tr'))
#     # print (u"总行数：", len (table_rows))
#     # table_rows=len(driver.find_elements_by_tag_name ('tr'))
#     print("循环到%s页，本页%s行,共获取%s" % (str(m + 1), str(table_rows - 2), str(no)))
#
#     for i in range(1, table_rows - 1):
#
#         try:
#             s_no = driver.find_element_by_xpath(aabb + '[%s]/td[2]' % (str(i))).text
#             s_name = driver.find_element_by_xpath(aabb + '[%s]/td[3]/div' % (str(i))).get_attribute('title')
#             s_panji = driver.find_element_by_xpath(aabb + '[%s]/td[5]' % (str(i))).text
#             s_ic = driver.find_element_by_xpath(aabb + '[%s]/td[6]' % (str(i))).text
#             s_sex = driver.find_element_by_xpath(aabb + '[%s]/td[7]' % (str(i))).text
#             s_pap = driver.find_element_by_xpath(aabb + '[%s]/td[8]/div' % (str(i))).get_attribute('title')
#             s_tel = driver.find_element_by_xpath(aabb + '[%s]/td[9]/div' % (str(i))).get_attribute('title')
#
#         except:
#             try:
#                 s_pap = driver.find_element_by_xpath(aabb + '[%s]/td[1]/div' % (str(i))).get_attribute('title')
#                 s_tel = driver.find_element_by_xpath(aabb + '[%s]/td[2]/div' % (str(i))).get_attribute('title')
#                 ##(多家长)
#                 s_no, s_name, s_panji, s_ic, s_sex = '', '', '', '', ''
#             except:
#                 pass
#
#         no += 1
#         writer = csv.writer(output)
#         writer.writerow([no, s_no, s_name, s_panji, s_ic, s_sex, s_pap, s_tel])
#         print(no, s_no, s_name, s_panji, s_ic, s_sex, s_pap, s_tel)
#
#     output.flush()
#     top = driver.find_element_by_link_text('下一页')
#     driver.execute_script("arguments[0].scrollIntoView(false);", top)
#     top.click()
#     # driver.execute_script ("arguments[0].scrollIntoView(false);", target)
#     el_list = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/table/tbody[2]/tr/td")
#     page = el_list.find_element_by_xpath("//input[@name='rollhidden']").get_attribute('value')
#     print("当前第%s页" % str(page) + "----" * 20)
#     # print ("----当前---%s---页" % page)
#     # print (int (page) != m + 2)
#
# # time.sleep(5000)
# output.close()
# driver.close()
# driver.quit()
#
