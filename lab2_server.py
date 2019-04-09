import random
from socket import *

# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_DGRAM指定了这个Socket的类型是UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址
serverSocket.bind(('127.0.0.1', 12000))

while True:
    # 产生一个0到10之间的随机数
    rand = random.randint(0, 10)
    # 从套接口上读取数据，参数为缓冲区大小
    message, address = serverSocket.recvfrom(1024)
    # 通过打印我们可以看到UDP客户端socket的端口是不确定，系统随机分配的
    print("收到来自 %s 的报文: (%s)" % (address, message))
    # 把接收到的信息全部转为大写
    print("随机数是: %d" % rand)
    message = message.upper()
    # 如果随机数小于4，服务端无应答,客户端就会超时
    if rand < 4:
        continue
    serverSocket.sendto(message, address)
