# coding=utf-8
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import IniFile


class IEDriverCrawler:

    def __init__(self):
        # 通过配置文件获取IEDriverServer.exe路径
        configfile = os.path.join (os.getcwd (), 'config.conf')
        cf = IniFile.ConfigFile (configfile)
        IEDriverServer = cf.GetValue ("section", "IEDriverServer")
        # 每抓取一页数据延迟的时间，单位为秒，默认为5秒
        self.pageDelay = 5
        pageInteralDelay = cf.GetValue ("section", "pageInteralDelay")
        if pageInteralDelay:
            self.pageDelay = int (pageInteralDelay)

        os.environ["webdriver.ie.driver"] = IEDriverServer
        self.driver = webdriver.Ie (IEDriverServer)

    def CatchData(self, id, firstUrl, nextUrl, restUrl):
        '''
        抓取数据
        :param id: 要获取元素标签的ID
        :param firstUrl: 首页Url
        :param nextUrl: 下一页URL
        :param restUrl: 下一页URL的组成部分
        :return:
        '''
        # 加载首页
        self.driver.get (firstUrl)
        # 打印标题
        print (self.driver.title)
        # id = "J_albumFlowCon"
        element = self.driver.find_element_by_id (id)
        txt = element.text.encode ('utf8')
        # 打印获取的信息
        print (txt)
        print (' ')
        time.sleep (20)  # 延迟20秒,
        # 由于有多页数据，为了测试，只取出几页数据
        for i in range (2, 4):
            print (' ')
            time.sleep (20)  # 延迟20秒,
            url = nextUrl + str (i) + restUrl
            self.driver.get (url)
            element = self.driver.find_element_by_id (id)
            txt = element.text.encode ('utf8')
            print (txt)
        self.driver.close ()
        self.driver.quit ()

    def CatchDatabyClickNextButton(self, id, firstUrl):
        '''
        抓取数据
        :param id: 要获取元素标签的ID
        :param firstUrl: 首页Url
        :return:
        '''
        start = time.clock ()
        # 加载首页
        self.driver.get (firstUrl)
        # 打印标题
        print (self.driver.title)
        # id = "J_ItemList"
        firstPage = self.driver.find_element_by_id (id)
        txt = firstPage.text.encode ('utf8')
        self.printTxt (1, txt)

        # 获取总页数
        name = 'filterPageForm'
        totalPageElement = self.driver.find_element_by_name (name)
        txt = totalPageElement.text.encode ('utf8')  # ui-page-next
        pattern = re.compile (r'\d+')
        flist = re.findall (pattern, txt)
        pageCount = 1
        if flist and len (flist) > 0:
            pageCount = int (flist[0])
        if pageCount > 1:
            pageCount = 10  # 先爬三页
            for index in range (2, pageCount + 1):
                time.sleep (self.pageDelay)  # 延迟五秒
                nextElement = self.driver.find_element_by_xpath ("//a[@class='ui-page-next']")
                nextUrl = nextElement.get_attribute ('href')
                self.driver.get (nextUrl)
                # ActionChains(self.driver).click(element)
                dataElement = self.driver.find_element_by_id (id)
                txt = dataElement.text.encode ('utf8')  # ui-page-next
                print (' ')
                self.printTxt (index, txt)

        self.driver.close ()
        self.driver.quit ()
        end = time.clock ()
        print (' ')
        print ("抓取每页数据后延迟 %d 秒" % self.pageDelay)
        print ("总共抓取了 %d页数据" % pageCount)
        print ("整个过程用时间: %f 秒" % (end - start))

    def printTxt(self, pageIndex, stringTxt):
        '''
        打印抓取的每页数据
        :param pageIndex:页数
        :param stringTxt:每页抓取的数据
        :return:
        '''
        if stringTxt.find ('¥') > -1:
            itemList = stringTxt.split ('¥')
            print ('第' + str (pageIndex) + '页数据')
            print (' ')
            for item in itemList:
                if len (item) > 0:
                    its = item.split ('\n')
                    if len (its) >= 4:
                        print ('单价：        ¥%s' % its[0])
                        print ('品牌：        %s' % its[1])
                        print ('销售店铺名称： %s' % its[2])
                        print ('成交量：      %s' % its[3])
                        print (' ')


# 测试抓取淘宝数据
# obj = IEDriverCrawler()
# firstUrl = "https://ai.taobao.com/search/index.htm?pid=mm_26632323_6762370_25910879&unid=&source_id=search&key=%E6%89%8B%E6%9C%BA&b=sousuo_ssk&clk1=&prepvid=200_11.251.246.148_396_1490081427029&spm=a231o.7712113%2Fa.a3342.1"
# nextUrl='https://ai.taobao.com/search/index.htm?pid=mm_26632323_6762370_25910879&unid=&source_id=search&key=%E6%89%8B%E6%9C%BA&b=sousuo_ssk&clk1=&prepvid=200_11.251.246.157_19825_1490081412211&spm=a231o.7076277.1998559105.1&page='
# # url='https://ai.taobao.com/search/index.htm?pid=mm_26632323_6762370_25910879&unid=&source_id=search&key=%E6%89%8B%E6%9C%BA&b=sousuo_ssk&clk1=&prepvid=200_11.251.246.148_396_1490081427029&spm=a231o.7712113%2Fa.a3342.1&page=2&pagesize=120'
# # url='https://ai.taobao.com/search/index.htm?pid=mm_26632323_6762370_25910879&unid=&source_id=search&key=%E6%89%8B%E6%9C%BA&b=sousuo_ssk&clk1=&prepvid=200_11.251.246.148_396_1490081427029&spm=a231o.7712113%2Fa.a3342.1&page=3&pagesize=120'
# restUrl = '&pagesize=120'
# obj.CatchData("J_albumFlowCon",firstUrl,nextUrl,restUrl)

# 测试抓取天猫数据
obj = IEDriverCrawler ()
firstUrl = "https://list.tmall.com/search_product.htm?q=%CA%D6%BB%FA&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton"
obj.CatchDatabyClickNextButton ("J_ItemList", firstUrl)
