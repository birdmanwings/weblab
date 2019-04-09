from socket import *
from time import *

if __name__ == '__main__':
    port = 12000
    server_addr = 'localhost'
    client_sock = socket(AF_INET, SOCK_DGRAM)  # 创建客户端套接字
    client_sock.settimeout(1)  # 设置超时时间为1s
    for i in range(10):  # 发送10个ping
        begin_time = time()
        try:
            send_data = 'a' * 64  # 发送64bytes的数据
            client_sock.sendto(send_data.encode(), (server_addr, port))  # 发送ping，将str类型编码转换为bytes
            message, address = client_sock.recvfrom(2048)  # 接收返回消息，2048为指定接收的最大数据量
            rrt = '%.3f' % (1000 * (time() - begin_time))
            print('{} bytes from {}: udp_seq={} time={}ms'.format(len(message), address, i, rrt))
        except timeout:
            print('time out: udp_seq={}'.format(i))
