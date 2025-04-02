# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
################################################################################
## Form generated from reading UI file 'form_addtask.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget,QDialog)

class Ui_AddTaskForm(QDialog):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(273, 200)
        MainWindow.setMinimumSize(QSize(273, 200))
        MainWindow.setMaximumSize(QSize(273, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_type_task_box = QComboBox(self.centralwidget)
        self.input_type_task_box.addItem("")
        self.input_type_task_box.addItem("")
        self.input_type_task_box.addItem("")
        self.input_type_task_box.setObjectName(u"input_type_task_box")
        self.input_type_task_box.setGeometry(QRect(10, 140, 121, 22))
        self.input_date_task_box = QDateEdit(self.centralwidget)
        self.input_date_task_box.setObjectName(u"input_date_task_box")
        self.input_date_task_box.setGeometry(QRect(140, 140, 121, 22))
        self.input_taskname_line = QLineEdit(self.centralwidget)
        self.input_taskname_line.setObjectName(u"input_taskname_line")
        self.input_taskname_line.setGeometry(QRect(10, 10, 251, 20))
        self.input_addinfo_textline = QTextEdit(self.centralwidget)
        self.input_addinfo_textline.setObjectName(u"input_addinfo_textline")
        self.input_addinfo_textline.setGeometry(QRect(10, 40, 251, 91))
        self.button_add_task = QPushButton(self.centralwidget)
        self.button_add_task.setObjectName(u"button_add_task")
        self.button_add_task.setGeometry(QRect(90, 170, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Add task", None))
        self.input_type_task_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u044b\u0435", None))
        self.input_type_task_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0435", None))
        self.input_type_task_box.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))

#if QT_CONFIG(accessibility)
        self.input_taskname_line.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.input_taskname_line.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.input_taskname_line.setInputMask("")
        self.input_taskname_line.setText("")
        self.button_add_task.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

