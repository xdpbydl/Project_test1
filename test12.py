# coding=utf-8
# 编译日期：2019-11-14 16:26:20
# 版权所有：www.i-search.com.cn
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import *
import getopt
from sys import argv
import sys
import ubpa.ibrowse as ibrowse
import ubpa.iie as iie
import ubpa.ikeyboard as ikeyboard


class Open_SQL2008:

    def __init__(self, **kwargs):
        self.__logger = ILog (__file__)
        self.path = set_img_res_path (__file__)
        self.robot_no = ''
        self.proc_no = ''
        self.job_no = ''
        self.input_arg = ''
        if ('robot_no' in kwargs.keys ()):
            self.robot_no = kwargs['robot_no']
        if ('proc_no' in kwargs.keys ()):
            self.proc_no = kwargs['proc_no']
        if ('job_no' in kwargs.keys ()):
            self.job_no = kwargs['job_no']
        if ('input_arg' in kwargs.keys ()):
            self.input_arg = kwargs['input_arg']
            self.input_arg = self.input_arg.replace ("\\", "/")
        self.pwd = 'xKiMIyo='
        self.user = 'ZCAdmin'

    def approval(self):
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14160829843157,Note:')
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', url=r'http://localhost/grwl/Main.aspx',
                          selector=r'#TreeView1n1 > IMG:nth-of-type(1)', button=r'left', curson=r'center', times=1,
                          run_mode=r'unctrl', waitfor=10, scroll_view='no')
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14160906410160,Note:')
        time.sleep (0.5)
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', url=r'http://localhost/grwl/Main.aspx',
                          selector=r'#TreeView1t3', button=r'left', curson=r'center', times=1, run_mode=r'unctrl',
                          waitfor=10, scroll_view='no')
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14161050177162,Note:')
        time.sleep (0.5)
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', title=r'合同发起', selector=r'#btnAdd', button=r'left',
                          curson=r'center', times=1, run_mode=r'unctrl', waitfor=10, scroll_view='no')
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14161213450164,Note:')
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', title=r'合同发起', selector=r'#searchcn10291',
                          button=r'left', curson=r'center', times=1, run_mode=r'unctrl', waitfor=10, scroll_view='no')
        # 键盘输入
        self.__logger.debug ('Flow:approval,StepNodeTag:14161908967175,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='{DOWN}{ENTER}', waitfor=10)
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14162054646178,Note:')
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', title=r'合同发起', selector=r'#searchcn10270',
                          button=r'left', curson=r'center', times=1, run_mode=r'unctrl', waitfor=10, scroll_view='no')
        # 键盘输入
        self.__logger.debug ('Flow:approval,StepNodeTag:14162054646177,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='{DOWN}{ENTER}', waitfor=10)
        # 键盘输入
        self.__logger.debug ('Flow:approval,StepNodeTag:14162214581185,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='20191114_test_1{RSHIFT}', waitfor=10)
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14162330489186,Note:')
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', title=r'合同发起', selector=r'#searchcn10273',
                          button=r'left', curson=r'center', times=1, run_mode=r'unctrl', waitfor=10, scroll_view='no')
        # 键盘输入
        self.__logger.debug ('Flow:approval,StepNodeTag:14162330489187,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='{DOWN}{ENTER}', waitfor=10)
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14162354762195,Note:')
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', title=r'合同发起', selector=r'#searchcn10274img',
                          button=r'left', curson=r'center', times=1, run_mode=r'unctrl', waitfor=10, scroll_view='no')
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14162436852202,Note:')
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', title=r'请选择',
                          selector=r'#xgvData_DXDataRow0 > TD:nth-of-type(1)', button=r'left', curson=r'center',
                          times=1, run_mode=r'unctrl', waitfor=10, scroll_view='no')
        # 鼠标点击
        self.__logger.debug ('Flow:approval,StepNodeTag:14162447299204,Note:')
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer', title=r'请选择', selector=r'#btnSearchSelect',
                          button=r'left', curson=r'center', times=1, run_mode=r'unctrl', waitfor=10, scroll_view='no')

    def login(self):
        # 打开浏览器
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697138,Note:')
        ibrowse.open_browser (browser_type='ie', url="http://localhost/grwl/")
        # 热键输入
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697137,Note:')
        ikeyboard.key_send_cs (text='!{SPACE}', waitfor=10)
        # 键盘输入
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697136,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='X', waitfor=10)
        # 键盘输入
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697130,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='{TAB}', waitfor=10)
        # 键盘输入
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697131,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='ZCAdmin{LSHIFT}', waitfor=10)
        # 键盘输入
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697135,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text='{TAB}', waitfor=10)
        # 键盘输入
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697134,Note:')
        time.sleep (0.5)
        ikeyboard.key_send_cs (text=self.pwd, waitfor=10)
        # 鼠标点击
        self.__logger.debug ('Flow:login,StepNodeTag:14155052697139,Note:')
        time.sleep (0.5)
        iie.do_click_pos (win_title=r'合同管理系统 - Internet Explorer',
                          url=r'http://localhost/grwl/Login.aspx?ReturnUrl=%2fgrwl%2fdefault.aspx',
                          selector=r'#imgbtnLogin', button=r'left', curson=r'center', times=1, run_mode=r'unctrl',
                          waitfor=10, scroll_view='no')

    def Main(self):
        # 子流程:login
        self.__logger.debug ('Flow:Main,StepNodeTag:14155314001153,Note:')
        (temptemp) = self.login ()
        # 子流程:approval
        self.__logger.debug ('Flow:Main,StepNodeTag:14161350985170,Note:')
        (temptemp) = self.approval ()


if __name__ == '__main__':
    robot_no = ''
    proc_no = ''
    job_no = ''
    input_arg = ''
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt (argv, "hr:p:j:i:", ["robot = ", "proc = ", "job = ", "input = "])
    except getopt.GetoptError:
        print ('robot.py -r <robot> -p <proc> -j <job>')
    for opt, arg in opts:
        if opt == '-h':
            print ('robot.py -r <robot> -p <proc> -j <job>')
        elif opt in ("-r", "--robot"):
            robot_no = arg
        elif opt in ("-p", "--proc"):
            proc_no = arg
        elif opt in ("-j", "--job"):
            job_no = arg
        elif opt in ("-i", "--input"):
            input_arg = arg
    pro = Open_SQL2008 (robot_no=robot_no, proc_no=proc_no, job_no=job_no, input_arg=input_arg)
    pro.Main ()
