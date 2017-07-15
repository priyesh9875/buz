# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/headline.ui'
#
# Created: Sun Apr  9 04:34:36 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 34)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelDate = QtGui.QLabel(Form)
        self.labelDate.setObjectName("labelDate")
        self.horizontalLayout.addWidget(self.labelDate)
        self.labelHeadline = QtGui.QLabel(Form)
        self.labelHeadline.setObjectName("labelHeadline")
        self.horizontalLayout.addWidget(self.labelHeadline)
        self.horizontalLayout.setStretch(1, 2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDate.setText(QtGui.QApplication.translate("Form", "10 Jan 2017", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHeadline.setText(QtGui.QApplication.translate("Form", "Headline text", None, QtGui.QApplication.UnicodeUTF8))

