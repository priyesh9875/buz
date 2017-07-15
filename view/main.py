# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/main.ui'
#
# Created: Sun Apr 23 02:48:00 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 502)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridFrame = QtGui.QFrame(self.centralwidget)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridFrame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandNewSubscription = QtGui.QCommandLinkButton(self.gridFrame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/new_sub.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandNewSubscription.setIcon(icon)
        self.commandNewSubscription.setObjectName("commandNewSubscription")
        self.horizontalLayout.addWidget(self.commandNewSubscription)
        self.commandNewFolder = QtGui.QCommandLinkButton(self.gridFrame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandNewFolder.setIcon(icon1)
        self.commandNewFolder.setObjectName("commandNewFolder")
        self.horizontalLayout.addWidget(self.commandNewFolder)
        self.commandUpdate = QtGui.QCommandLinkButton(self.gridFrame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/refresh.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandUpdate.setIcon(icon2)
        self.commandUpdate.setObjectName("commandUpdate")
        self.horizontalLayout.addWidget(self.commandUpdate)
        self.commandFind = QtGui.QCommandLinkButton(self.gridFrame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/find.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandFind.setIcon(icon3)
        self.commandFind.setObjectName("commandFind")
        self.horizontalLayout.addWidget(self.commandFind)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.gridFrame, 0, 0, 1, 1)
        self.mainContainer = QtGui.QGridLayout()
        self.mainContainer.setObjectName("mainContainer")
        self.gridLayout_5.addLayout(self.mainContainer, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 28))
        self.menubar.setObjectName("menubar")
        self.menuSubscription = QtGui.QMenu(self.menubar)
        self.menuSubscription.setObjectName("menuSubscription")
        self.menuFeeds = QtGui.QMenu(self.menubar)
        self.menuFeeds.setObjectName("menuFeeds")
        self.menuSearch = QtGui.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewSubscription = QtGui.QAction(MainWindow)
        self.actionNewSubscription.setIcon(icon)
        self.actionNewSubscription.setIconVisibleInMenu(True)
        self.actionNewSubscription.setObjectName("actionNewSubscription")
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setIcon(icon2)
        self.actionUpdate.setIconVisibleInMenu(True)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionRemove = QtGui.QAction(MainWindow)
        self.actionRemove.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/delete.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon4)
        self.actionRemove.setIconVisibleInMenu(True)
        self.actionRemove.setObjectName("actionRemove")
        self.actionProperties = QtGui.QAction(MainWindow)
        self.actionProperties.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/properties.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProperties.setIcon(icon5)
        self.actionProperties.setIconVisibleInMenu(True)
        self.actionProperties.setObjectName("actionProperties")
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/preferences.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon6)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionNewFolder = QtGui.QAction(MainWindow)
        self.actionNewFolder.setIcon(icon1)
        self.actionNewFolder.setIconVisibleInMenu(True)
        self.actionNewFolder.setObjectName("actionNewFolder")
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/import.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon7)
        self.actionImport.setIconVisibleInMenu(True)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport_2 = QtGui.QAction(MainWindow)
        self.actionExport_2.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/export.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_2.setIcon(icon8)
        self.actionExport_2.setIconVisibleInMenu(True)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setEnabled(True)
        self.actionSearch.setIcon(icon3)
        self.actionSearch.setIconVisibleInMenu(True)
        self.actionSearch.setObjectName("actionSearch")
        self.actionFAQ = QtGui.QAction(MainWindow)
        self.actionFAQ.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/faq.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFAQ.setIcon(icon9)
        self.actionFAQ.setIconVisibleInMenu(True)
        self.actionFAQ.setObjectName("actionFAQ")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/about.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon10)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionWorkOffline = QtGui.QAction(MainWindow)
        self.actionWorkOffline.setCheckable(True)
        self.actionWorkOffline.setEnabled(False)
        self.actionWorkOffline.setObjectName("actionWorkOffline")
        self.menuSubscription.addAction(self.actionPreferences)
        self.menuSubscription.addSeparator()
        self.menuSubscription.addAction(self.actionNewSubscription)
        self.menuSubscription.addAction(self.actionNewFolder)
        self.menuSubscription.addSeparator()
        self.menuSubscription.addSeparator()
        self.menuSubscription.addAction(self.actionImport)
        self.menuSubscription.addAction(self.actionExport_2)
        self.menuSubscription.addSeparator()
        self.menuSubscription.addSeparator()
        self.menuSubscription.addAction(self.actionWorkOffline)
        self.menuSubscription.addSeparator()
        self.menuSubscription.addSeparator()
        self.menuSubscription.addAction(self.actionExit)
        self.menuFeeds.addAction(self.actionUpdate)
        self.menuFeeds.addAction(self.actionRemove)
        self.menuFeeds.addAction(self.actionProperties)
        self.menuSearch.addAction(self.actionSearch)
        self.menuHelp.addAction(self.actionFAQ)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSubscription.menuAction())
        self.menubar.addAction(self.menuFeeds.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Buzz: Priyesh kumar", None, QtGui.QApplication.UnicodeUTF8))
        self.commandNewSubscription.setText(QtGui.QApplication.translate("MainWindow", "New S&ubscription...", None, QtGui.QApplication.UnicodeUTF8))
        self.commandNewFolder.setText(QtGui.QApplication.translate("MainWindow", "&New Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.commandUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.commandFind.setText(QtGui.QApplication.translate("MainWindow", "&Find...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSubscription.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFeeds.setTitle(QtGui.QApplication.translate("MainWindow", "F&eeds", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSearch.setTitle(QtGui.QApplication.translate("MainWindow", "&Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSubscription.setText(QtGui.QApplication.translate("MainWindow", "New S&ubscription...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSubscription.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setShortcut(QtGui.QApplication.translate("MainWindow", "F5, Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setText(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFolder.setText(QtGui.QApplication.translate("MainWindow", "&New folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFolder.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "&Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_2.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("MainWindow", "Search All &Feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFAQ.setText(QtGui.QApplication.translate("MainWindow", "FAQ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkOffline.setText(QtGui.QApplication.translate("MainWindow", "Work offline", None, QtGui.QApplication.UnicodeUTF8))

import res_rc