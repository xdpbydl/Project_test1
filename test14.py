import socket,socks,requests

socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",9150)
socket.socket = socks.socksocket
a = requests.get ("http://checkip.amazonaws.com").text
print(a)