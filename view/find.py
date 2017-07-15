# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/find.ui'
#
# Created: Sun Apr  9 00:22:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(393, 127)
        self.buttonFind = QtGui.QPushButton(Dialog)
        self.buttonFind.setGeometry(QtCore.QRect(292, 88, 90, 28))
        self.buttonFind.setObjectName("buttonFind")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 381, 20))
        self.label_2.setObjectName("label_2")
        self.buttonClose = QtGui.QPushButton(Dialog)
        self.buttonClose.setGeometry(QtCore.QRect(190, 88, 90, 28))
        self.buttonClose.setObjectName("buttonClose")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 370, 32))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.buttonFind)
        Dialog.setTabOrder(self.buttonFind, self.buttonClose)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonFind.setText(QtGui.QApplication.translate("Dialog", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Enter text to be searched in feeds title", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

