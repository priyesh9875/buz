# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/newSubscription.ui'
#
# Created: Sun Apr  9 00:22:13 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 230)
        self.buttonAdd = QtGui.QPushButton(Dialog)
        self.buttonAdd.setGeometry(QtCore.QRect(440, 190, 90, 28))
        self.buttonAdd.setObjectName("buttonAdd")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 9, 530, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.buttonClose = QtGui.QPushButton(Dialog)
        self.buttonClose.setGeometry(QtCore.QRect(330, 190, 90, 28))
        self.buttonClose.setObjectName("buttonClose")
        self.lineUrl = QtGui.QLineEdit(Dialog)
        self.lineUrl.setGeometry(QtCore.QRect(20, 140, 510, 32))
        self.lineUrl.setObjectName("lineUrl")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 381, 20))
        self.label_3.setObjectName("label_3")
        self.lineName = QtGui.QLineEdit(Dialog)
        self.lineName.setGeometry(QtCore.QRect(20, 70, 510, 32))
        self.lineName.setObjectName("lineName")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 381, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineName, self.lineUrl)
        Dialog.setTabOrder(self.lineUrl, self.buttonAdd)
        Dialog.setTabOrder(self.buttonAdd, self.buttonClose)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add new Subscription", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "New Subscription", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Enter subscription url", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Enter subscription name", None, QtGui.QApplication.UnicodeUTF8))

