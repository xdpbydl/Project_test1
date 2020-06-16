# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os, re
import pandas as pd
from openpyxl import load_workbook

srcDir = u'E:/TEMP/0.1 TEST/1111/'  # 源文件
targetDir = u'E:/TEMP/0.1 TEST/2222/'  # 目标文件
file_list = sorted(os.listdir(srcDir))  # 获取源文件名
excel_file = 'E:/TEMP/0.1 TEST/2222/111.xlsx'
excel_data = pd.read_excel(excel_file, sheet_name='Sheet1')

for e in excel_data.values:
    yn = 0
    for f in file_list:
        m = re.split(u'.jpg', f)[0]
        # print(e[1], m)
        if e[1].replace(' ', '') == m.replace(' ', ''):           # .replace(' ', '')去中间空格
            e_A = [str(i) for i in e]           # 字符串join不支持int
            new = 'L' + '_'.join(e_A) + '.jpg'
            shutil.copyfile(srcDir + f, targetDir + new.replace(' ', ''))
            yn = 1
        elif yn == 0:
            print(m + '  文件中没有联系方式！————————')
    if yn == 0:         # excel中不存在的文件
        print(e[1] + '没有图片！————————')

            #
            # # wb = load_workbook(r"E:\TEMP\0.1 TEST\1111\data.xlsx", data_only=True)
            # # sh = wb["Sheet1"]
            # data = []
            #
            # for i in file_list:
            #     new = 'L' + i
            #     shutil.copyfile(srcDir + i, targetDir + new)
            #     en = re.split('[_.]', i)[:-1]
            #     data.append(en)
            # # arr1 = ['id', '姓名', '性别', '手机号码']
            # # data = pd.Series(arr1)
            #
            # print(data, type(data), len(data))
            # data1 = pd.DataFrame(data)
            # data1.to_excel(targetDir + 'excel_to_python.xlsx', sheet_name='Sheet1')
