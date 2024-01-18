# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(667, 614)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setFocusPolicy(Qt.NoFocus)
        Form.setAcceptDrops(False)
        icon = QIcon(QIcon.fromTheme(u"applications-system"))
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy1.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy1)
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 30, 251, 31))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 30, 51, 31))
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(False)
        self.label.setFont(font)
        self.label.setFocusPolicy(Qt.TabFocus)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setIndent(-1)
        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(416, 30, 71, 31))
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBox.setSpecialValueText(u"")
        self.spinBox.setMaximum(65535)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(395, 30, 16, 31))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 90, 101, 24))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 90, 75, 24))
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 140, 580, 380))
        self.spinBox_2 = QSpinBox(self.tab)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(520, 30, 42, 31))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(16)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(570, 30, 31, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 30, 431, 31))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 30, 31, 31))
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(510, 30, 75, 31))
        self.textBrowser_2 = QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(30, 80, 580, 440))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(280, 230, 75, 24))
        self.textBrowser_3 = QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(30, 280, 580, 240))
        self.layoutWidget = QWidget(self.tab_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 30, 331, 201))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)
        self.comboBox.setModelColumn(0)

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 50)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 40)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_3)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 50)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox_4 = QComboBox(self.layoutWidget)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setEditable(True)

        self.horizontalLayout_3.addWidget(self.comboBox_4)

        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 50)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8bfe\u8bbe", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"IP:127.0.0.1", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76ee\u6807:", None))
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.label_2.setText(QCoreApplication.translate("Form", u":", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"TCP SYN Flood", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"UDP Flood", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u7ebf\u7a0b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"TCP/UDP", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"URL:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u653b\u51fb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"HTTP", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u542f\u52a8", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7f51\u5361\uff1a", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u7f51\u5361", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u653b\u51fb\u65b9\u5f0f:", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u653b\u51fb\u6a21\u5f0f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u653b\u51fb\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5192\u5145\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"ARP", None))
    # retranslateUi

