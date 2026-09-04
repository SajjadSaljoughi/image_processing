# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(447, 489)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_load_encrypt = QPushButton(self.centralwidget)
        self.pushButton_load_encrypt.setObjectName(u"pushButton_load_encrypt")
        self.pushButton_load_encrypt.setGeometry(QRect(10, 80, 131, 41))
        self.label_encrypt = QLabel(self.centralwidget)
        self.label_encrypt.setObjectName(u"label_encrypt")
        self.label_encrypt.setGeometry(QRect(160, 40, 251, 181))
        self.pushButton_encrypt = QPushButton(self.centralwidget)
        self.pushButton_encrypt.setObjectName(u"pushButton_encrypt")
        self.pushButton_encrypt.setGeometry(QRect(10, 150, 131, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(8, 10, 431, 20))
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet(u"background-color : green")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(8, 240, 431, 20))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"background-color : red")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_load_decrypt = QPushButton(self.centralwidget)
        self.pushButton_load_decrypt.setObjectName(u"pushButton_load_decrypt")
        self.pushButton_load_decrypt.setGeometry(QRect(10, 270, 131, 41))
        self.pushButton_secret_key = QPushButton(self.centralwidget)
        self.pushButton_secret_key.setObjectName(u"pushButton_secret_key")
        self.pushButton_secret_key.setGeometry(QRect(10, 330, 131, 41))
        self.label_decrypt = QLabel(self.centralwidget)
        self.label_decrypt.setObjectName(u"label_decrypt")
        self.label_decrypt.setGeometry(QRect(160, 270, 251, 171))
        self.pushButton_decrypt = QPushButton(self.centralwidget)
        self.pushButton_decrypt.setObjectName(u"pushButton_decrypt")
        self.pushButton_decrypt.setGeometry(QRect(10, 390, 131, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 447, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_load_encrypt.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.label_encrypt.setText("")
        self.pushButton_encrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Encryption", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Decryption", None))
        self.pushButton_load_decrypt.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.pushButton_secret_key.setText(QCoreApplication.translate("MainWindow", u"Secret Key", None))
        self.label_decrypt.setText("")
        self.pushButton_decrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
    # retranslateUi

