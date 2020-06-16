# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os, re
import pandas as pd
from openpyxl import load_workbook

srcDir = u'E:/TEMP/0.1 TEST/1111/'  # 源文件
targetDir = u'E:/TEMP/0.1 TEST/2222/'  # 目标文件
file_list = sorted(os.listdir(srcDir))  # 获取源文件名

# wb = load_workbook(r"E:\TEMP\0.1 TEST\1111\data.xlsx", data_only=True)
# sh = wb["Sheet1"]
data = []

for i in file_list:
    new = 'L' + i
    shutil.copyfile(srcDir + i, targetDir + new)
    en = re.split('[_.]', i)[:-1]
    data.append(en)
# arr1 = ['id', '姓名', '性别', '手机号码']
# data = pd.Series(arr1)

print(data, type(data), len(data))
data1 = pd.DataFrame(data)
data1.to_excel(targetDir + 'excel_to_python.xlsx', sheet_name='Sheet1')
