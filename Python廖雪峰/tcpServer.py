# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
# 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，
# 随后的通信就靠这个Socket连接了。
# 一个Socket：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。

# 该服务器程序接收客户端连接，把客户端发过来的字符串加上Hello再发回去

import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # 连接建立后，服务器首先发一条欢迎消息
    sock.send(b'Welcome!')
    while True:
        # 等待客户端数据，并加上Hello再发送给客户端
        data = sock.recv(1024)
        time.sleep(1)
        # 如果客户端发送了exit字符串，就直接关闭连接
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接
    # accept()会等待并返回一个客户端的连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    # 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
