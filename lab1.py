import sys
import _thread
from socket import *

not_found_html = "<h1>404 NOT FOUND!</h1>"


def request_parser(request):  # 解析request请求
    lines = request.split('\n')
    request_line = lines[0].split()
    header_lines = dict()
    for each in lines[1:]:
        if each.strip() != "":
            key = each[:each.find(':')]
            value = each[each.find(':') + 1:].strip()
            header_lines[key] = value
    return [request_line, header_lines]


def generate_response(request_header):  # 根据html头获取文件
    method, url, http_version = request_header[0]
    url = './static{}'.format(url)  # 获取static文件夹下的文件
    status = 200
    phase = {
        200: "OK",
        404: "NOT FOUND"
    }
    data = ''
    try:
        with open(url, 'rt') as fr:
            data = fr.read()
    except IOError:
        status = 404
        data = not_found_html
    return """HTTP/1.1 {} {}\r\nConnection: close\r\nContent-type: {}\r\n\r\n{}""".format( \
        status, phase[status], 'text/html', data)


def process_connection(conn_sock, addr):
    request = conn_sock.recv(1024).decode()  # 接收TCP数据
    request_header = request_parser(request)
    response = generate_response(request_header)
    conn_sock.send(response.encode('utf-8'))
    print('{} process finish! closing...'.format(addr))
    conn_sock.close()


if __name__ == '__main__':
    server_port = int(sys.argv[1])  # 获取服务器端口号
    server_socket = socket(AF_INET, SOCK_STREAM)  # 建立套接字
    server_socket.bind(('', server_port))  # 绑定端口号
    server_socket.listen(1000)  # 设置监听数目
    while True:
        conn_sock, addr = server_socket.accept()  # 建立TCP连接
        _thread.start_new_thread(process_connection, (conn_sock, addr))  # 多线程
