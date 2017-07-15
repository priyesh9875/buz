# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/newFolder.ui'
#
# Created: Sun Apr  9 00:22:16 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 161)
        self.buttonAdd = QtGui.QPushButton(Dialog)
        self.buttonAdd.setGeometry(QtCore.QRect(444, 120, 90, 28))
        self.buttonAdd.setObjectName("buttonAdd")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 38, 381, 20))
        self.label_2.setObjectName("label_2")
        self.buttonClose = QtGui.QPushButton(Dialog)
        self.buttonClose.setGeometry(QtCore.QRect(340, 120, 90, 28))
        self.buttonClose.setObjectName("buttonClose")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 510, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2.setBuddy(self.lineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.buttonAdd)
        Dialog.setTabOrder(self.buttonAdd, self.buttonClose)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add new folder", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "New Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Enter folder name", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

