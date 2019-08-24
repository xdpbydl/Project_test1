# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os
from openpyxl import load_workbook

srcDir = 'D:/Temp/orher/111/'
targetDir = 'D:/Temp/orher/222/'
file_list = sorted(os.listdir(srcDir))

file_list_iter = iter(file_list)

# for index1, file_name in enumerate(file_list):
#     for name in file_name:
#         print(name, end="")
#     print("")
#
wb = load_workbook(r"D:/Temp/orher/26个班级.xlsx", data_only=True)
sh = wb["Sheet1"]

for index, item in enumerate(sh["I2":"I51"]):
    for cell in item:
        print(cell)
        name = cell.value
        # print(name)
        srcfile = srcDir + next(file_list_iter)
        dstfile = targetDir + name + ".jpg"
        print(srcfile , "》》》》》", name + ".jpg")

        shutil.copyfile(srcfile, dstfile)
