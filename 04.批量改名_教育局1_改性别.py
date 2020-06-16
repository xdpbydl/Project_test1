# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os, re
import pandas as pd
from openpyxl import load_workbook

srcDir = u'E:/TEMP/0.1 TEST/3333/'  # 源文件
targetDir = u'E:/TEMP/0.1 TEST/2222/'  # 目标文件
file_list = sorted(os.listdir(srcDir))  # 获取源文件名
excel_file = 'E:/TEMP/0.1 TEST/2222/111.xlsx'
excel_data = pd.read_excel(excel_file, sheet_name='Sheet1')
num = 0

for e in excel_data.values:
    num += 1
    for f in file_list:
        m = re.split(u'.jpg', f)[0].replace(' ', '')        # .replace(' ', '')去空格
        if e[1].replace(' ', '') == m:          # .replace(' ', '')去空格
            excel_data.iloc[num-1, 2] = '女'
            print(m, excel_data.iloc[num-1, 2])
            excel_data.to_excel(targetDir + 'excel_to_python.xlsx', sheet_name='Sheet1', index=False)
