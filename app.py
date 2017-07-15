'''
Buzz: RSS, ATOM feed reader
Author: Priyesh kumar

app.py 
    - Entry files
    - Initializes all components and connect signals and slots
'''

from PySide import QtCore, QtGui
import sys

import inspect
import os
import sqlite3
import re

    
# Append current path so that sub folders can access sibling packages
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.sys.path.append(currentdir)

# Import ui files
from view import main

# Import controller files
from controller.preferences import PreferencesDialog
from controller.find import FindDialog
from controller.details import DetailsForm
from controller.newFolder import NewFolderDialog
from controller.newSubscription import NewSubscriptionDialog
from controller.about import AboutDialog
from controller.treeView import TreeWidget
from controller.listView import ListWidget

from helpers import constants

class MainApp(QtGui.QMainWindow, main.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        # Connect menu items to their respective slots
        self.actionPreferences.triggered.connect(self.openPreferences)
        self.actionAbout.triggered.connect(self.openAbout)
        self.actionSearch.triggered.connect(self.openFind)
        self.actionNewFolder.triggered.connect(self.openNewFolder)
        self.actionNewSubscription.triggered.connect(self.openNewSubscription)
        self.commandNewFolder.clicked.connect(self.openNewFolder)
        self.commandFind.clicked.connect(self.openFind)
        self.commandNewSubscription.clicked.connect(self.openNewSubscription)


        # Tree section to show feeds Subscription list
        self.treeWidget = TreeWidget()
        self.mainContainer.addWidget(self.treeWidget, 0, 0)

        listContainer = QtGui.QGridLayout()

        # List section to show highlights of selected Subscription
        self.listWidget = ListWidget()
        # self.listWidget.refreshList()

        # Detail section to show selected feed content
        self.detailswidget = DetailsForm()

        listContainer.addWidget(self.listWidget, 0,0)
        listContainer.addWidget(self.detailswidget, 1,0)

        
        self.mainContainer.addLayout(listContainer, 0, 1)
        self.mainContainer.setColumnStretch(1,2)

        
        # Attaching list/tree signals
        self.listWidget.listWidget.currentRowChanged.connect(self.handleListItemChange)
        self.treeWidget.treeWidget.currentItemChanged.connect(self.treeItemClicked)
        self.treeWidget.treeWidget.itemClicked.connect(self.treeItemClicked)

        self.actionUpdate.triggered.connect(self.treeWidget.updateItem)
        self.commandUpdate.clicked.connect(self.treeWidget.updateItem)
        
  
    def treeItemClicked(self, current=None, next=None):
        '''
        Update list section whenever Subscription is clicked/changes
        '''
        node =  self.treeWidget.treeWidget.currentItem()
        if node.item_type == constants.TREE_ITEM_ROOT:
            return
        self.listWidget.updateList(node.feeds)

    def handleListItemChange(self, index):
        '''
        Updates detail section whenever feed highlight is clicked/changed
        '''
        try:
            if index == -1:
                return

            self.statusBar().showMessage("Index:" + str(index))
                
            currentItem =  self.listWidget.listWidget.currentItem()
            node = self.listWidget.listWidget.itemWidget(currentItem)
            if node:
                node.markRead()
                self.detailswidget.updateData(node.item)
        except Exception as e:
            print ("Exception:", e)
            pass



    def openPreferences(self):
        """Signal handler for preferences menu """
        try:
            self.statusBar().showMessage("Preferences")
            dialog = QtGui.QDialog(self)
            dialog.setWindowTitle("Preferences")
            p = PreferencesDialog(dialog)
            p.show()
            dialog.exec_()
            self.statusBar().showMessage("")            
        except Exception as e:
            self.statusBar().showMessage("Exception: " +  type(e).__name__ + " : " + str(e) )            
            print (e)



    def openAbout(self):
        """Signal handler for about menu """
        try:
            self.statusBar().showMessage("About Buzz")
            dialog = QtGui.QDialog(self)
            dialog.setWindowTitle("About")
            p = AboutDialog(dialog)
            p.show()
            dialog.exec_()
            self.statusBar().showMessage("")            
        except Exception as e:
            self.statusBar().showMessage("Exception: " +  type(e).__name__ + " : " + str(e) )            
            print (e)
            
    
    def openNewFolder(self):
        """Signal handler for new folder menu """
        try:
            self.statusBar().showMessage("New Folder")
            dialog = QtGui.QDialog(self)
            dialog.setWindowTitle("Add new Folder")
            p = NewFolderDialog(self.treeWidget.getParent() , dialog)
            p.show()
            dialog.exec_()
            self.statusBar().showMessage("")            
        except Exception as e:
            self.statusBar().showMessage("Exception: " +  type(e).__name__ + " : " + str(e) )            
            print (e)


    def openNewSubscription(self):
        """Signal handler for new Subscription menu """
        try:
            self.statusBar().showMessage("New Subscription")
            dialog = QtGui.QDialog(self)
            dialog.setWindowTitle("Add new Subscription")
            p = NewSubscriptionDialog(self.treeWidget.getParent() , dialog)
            p.show()
            dialog.exec_()
            self.statusBar().showMessage("")            
        except Exception as e:
            self.statusBar().showMessage("Exception: " +  type(e).__name__ + " : " + str(e) )            
            print (e)


    def openFind(self):
        """Signal handler for search menu """
        try:
            self.statusBar().showMessage("Search")
            dialog = QtGui.QDialog(self)
            dialog.setWindowTitle("Search")
            p = FindDialog(self.treeWidget ,dialog)
            p.show()
            dialog.exec_()
            self.statusBar().showMessage("")            
        except Exception as e:
            self.statusBar().showMessage("Exception: " +  type(e).__name__ + " : " + str(e) )            
            print (e)
    
    

def default_app():
    conn = sqlite3.connect('config/database.db')
    print ("Database created")
    conn.execute("CREATE TABLE settings (app_name text, update_startup int, update_interval int, items_per_feed int)")
    print ("Default settings created")
    res = conn.execute("INSERT INTO settings values (?, ?, ?, ?)", ["Buzz - Priyesh kumar", 1, 3600, 500])    
    conn.commit()
    conn.close()


def read_config():
    conn = sqlite3.connect('config/database.db')
    cursor = conn.cursor()
    try:
        res2 = conn.execute("SELECT * FROM settings LIMIT 1")
        for row in res2:
            print (row)
        
    except sqlite3.OperationalError as e:
        default_app()

    conn.commit()
    conn.close()


def parse_folder_dict(cursor, value,parent = 0):
    for k, v in value.items():
        if type(v) is dict:
            print (3, k, "folder")
            cursor.execute("INSERT INTO folders (title, type, parent) VALUES (?,?,?)", (k, 1, parent ))
            id = cursor.lastrowid            
            parse_folder_dict(cursor, v, parent=id)
        else:

            print (2,k,v)
            cursor.execute("INSERT INTO folders (title, type, parent, url) VALUES (?,?,?,?)", (k, 2, parent, v ))
            res = cursor.execute("""CREATE TABLE {}
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    updated TEXT NOT NULL,
                    link TEXT NOT NULL,
                    summary TEXT,
                    isread INTEGER,
                    raw TEXT
                );""".format(re.sub('[^0-9A-Za-z]+', "", k)) 
            )
            
            


def default_feeds():

    # Detault feed source
    feeds_source = {
        'India': {
            "NDTV":"http://feeds.feedburner.com/ndtvnews-latest?format=xml",
            "NDTV Startups": "http://tech.economictimes.indiatimes.com/rss/startups",
        },
        
        "News": {
            "Politics": "http://feeds.skynews.com/feeds/rss/politics.xml",
            "Bangalore": "http://timesofindia.indiatimes.com/rssfeeds/-2128833038.cms",
        },
    }

    conn = sqlite3.connect('config/database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS folders
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            type INTEGER,
            parent INTEGER,
            url TEXT
        );""")


    parse_folder_dict(cursor, feeds_source)
    conn.commit()
    conn.close()


if __name__ == "__main__":

    try:
        if not os.path.exists('config'):
            os.makedirs('config')
            default_app()
            default_feeds()


        read_config()
        
    except Exception as e:
        pass
        print (e)
    
    app = QtGui.QApplication(sys.argv)
    entry = MainApp()
    entry.show()
    app.exec_()
