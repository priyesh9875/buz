# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/details.ui'
#
# Created: Sun Apr  9 02:46:47 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(606, 475)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 604, 473))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.labelFeed = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelFeed.setWordWrap(True)
        self.labelFeed.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelFeed.setObjectName("labelFeed")
        self.horizontalLayout_2.addWidget(self.labelFeed)
        self.toolButton = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/open_url.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.gridLayout_2.setRowStretch(1, 10)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFeed.setText(QtGui.QApplication.translate("Form", "--", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
