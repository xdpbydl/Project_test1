import pywifi
from pywifi import const  # 引用常量


def gic():
    wifi = pywifi.PyWiFi()
    # print(wifi)
    ifaces = wifi.interfaces()[0]
    # print(ifaces.name())  #无线网卡名称
    # print(ifaces.status())  # 无线网卡状态 0未连接 4已连接
    if ifaces.status() == const.IFACE_CONNECTED:
        print("已连接")
    else:
        print("未连接")


# 扫描附近的WIFI
def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]

    # 扫描WIFI
    ifaces.scan()
    res = ifaces.scan_results()
    print(len(res))
    for data in res:
        print(data.ssid)



if __name__ == '__main__':
    # gic()
    bies()
