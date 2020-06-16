from tkinter import *
from pywifi import const
import time, pywifi


# 测试连接
def wificonnect():
    pass


def reaPwd():
    # 获取WIFI名称
    wifiname = entry.get()
    path = r"E:\Python\learning\Project_test1\wifipwd.txt"
    file = open(path, 'r')
    while True:
        try:
            # 读取密码本，一行一行读
            mystr = file.readline()
            #  测试连接
            # bool = wificonnect()
            if bool:
                print("密码正确", mystr)
            else:
                print("密码错误", mystr)
        except:
            pass



# 创建窗口
root = Tk()
# 窗口标题
root.title('WiFi破解')
# # 窗口的大小,小写的x
# root.geometry('500x400')
# # 窗口的位置
# root.geometry('+550+266')
# 合并窗口大小、位置
root.geometry('500x400+550+266')
# 标签增加
label = Label(root, text='输入要破解的WIFI名称：')
# 位置 定位 ，网格的布局
label.grid(row=0, column=0)

# 输入控件
entry = Entry(root, font=('微软雅黑', 22))
entry.grid(row=0, column=1)

# 列表框控件
text = Listbox(root, font=('微软雅黑', 15), width=40, height=10)
# columnspan 组件所跨越的列数
text.grid(row=1, columnspan=2)

# 按钮    commad为点击按钮所触发的事件
button = Button(root, text="开始破解", width=20, height=2, commad=reaPwd())
button.grid(row=2, columnspan=2)
# 显示窗口
root.mainloop()
