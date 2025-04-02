# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_tasklist.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(331, 262)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 331, 241))
        self.button_add_new_task = QPushButton(self.centralwidget)
        self.button_add_new_task.setObjectName(u"button_add_new_task")
        self.button_add_new_task.setGeometry(QRect(240, 240, 51, 23))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(0, 240, 121, 22))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(120, 240, 121, 22))
        self.del_button = QPushButton(self.centralwidget)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setGeometry(QRect(290, 240, 41, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TaskTracker", None))
        self.button_add_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u044b\u0435", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0435", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.del_button.setText(QCoreApplication.translate("MainWindow", u"del", None))
    # retranslateUi

