import threading
import time
import socket

import socketserver

# class proc_socket_server:
#
#     def __init__(self):
#         super().__init__()
#
#     def socket_server(self):
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.bind(('192.168.146.156', 6688))
#         server.listen(5)
#         print(u'waiting for connect')
#         connect, (host, port) = server.accept()
#         print(u'the client %s:%s has connect.' % (host, port))
#
#         while True:
#             send_data = proc_file.proc_Qthread_fuction().sys_proc_uploading()
#             connect.sendall(bytes(send_data, encoding='utf-8'))
#             # time.sleep(1000)
#
#             # data = connect.recv(1024)
#             # if data == b'quit' or data == b'':
#             #     print(b'the client has quit')
#             #     break
#             # else:
#             #     print(data)
#             # connect.send(b'0')
#             # data = proc_file.proc_Qthread_fuction().sys_proc_uploading
#             # print(data)
#             # connect.sendall(data)
#             # connect.send(b'123')
#
#         # server.close()

# --------------------------------------------------------
# one to anythings


import socketserver

LOCALHOST = '192.168.3.13'
PORT = 6688


class proc_server(socketserver.BaseRequestHandler):
    # 定义handle方法，函数名只能是handle
    def handle(self):
        connect = self.request
        print(connect)
        while True:
            try:
                send_data = "123"
                connect.sendall(bytes(send_data, encoding='utf-8'))
            except Exception as e:
                pass


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer((LOCALHOST, PORT), proc_server)
    server.serve_forever()


