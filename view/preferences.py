# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preferences.ui'
#
# Created: Sun Apr 23 02:46:06 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 320)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 531, 30))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 300, 20))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtGui.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(331, 43, 120, 32))
        self.spinBox.setMaximum(999999999)
        self.spinBox.setProperty("value", 500)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(11, 90, 531, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 154, 111, 20))
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtGui.QSpinBox(self.tab)
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 150, 120, 32))
        self.spinBox_2.setProperty("value", 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(40, 121, 351, 25))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(304, 152, 78, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.checkBox_2 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 30, 141, 25))
        self.checkBox_2.setObjectName("checkBox_2")
        self.commandLinkButton = QtGui.QCommandLinkButton(self.tab_3)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 70, 175, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/delete.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.tab_3)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(220, 70, 175, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/refresh.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Feed cache handler", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Max number of items to be saved per feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Feeds Update", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Refresh interval", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "Update on startup", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Hours", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Dialog", "Work offline", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("Dialog", "Purge storage", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton_2.setText(QtGui.QApplication.translate("Dialog", "Update feeeds", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog", "More", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
