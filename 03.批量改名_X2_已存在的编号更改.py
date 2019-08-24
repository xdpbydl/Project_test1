# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os, re
from openpyxl import load_workbook

srcDir = 'D:/Temp/orher/111/'           #源文件
targetDir = 'D:/Temp/orher/222/'        #目标文件
file_list = sorted(os.listdir(srcDir))  #获取源文件名

wb = load_workbook(r"D:/Temp/orher/26个班级.xlsx", data_only=True)
sh = wb["Sheet1"]

for i in file_list:
    file_name_0 = re.split('_',i)[0]
    # print(file_name)
    for n in (sh['i']):
        excle_name_0 = re.split('_', n.value)[0]
        if file_name_0 ==  excle_name_0:
            # print(excle_name_0,file_name_0)
            srcfile  = srcDir + i
            dstfile = targetDir + n.value + '.jpg'
            print(srcfile, '>>>>>>>>',dstfile)
            shutil.copyfile(srcfile, dstfile)





