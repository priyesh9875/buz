from PySide import QtGui, QtCore

import threading
import feedparser
import sqlite3

# Import ui file
from view import tree as treeUI

from helpers import dbhelper
from helpers import dateparser
from helpers import constants
from helpers.dbhelper import DATABASE

from model.CustomTreeItem import CustomTreeItem
from controller.newFolder import NewFolderDialog
from controller.newSubscription import NewSubscriptionDialog



# Example feed source
# feeds_source = {
#     'India': {
#         "NDTV":"http://feeds.feedburner.com/ndtvnews-latest?format=xml",
#         "NDTV Startups": "http://tech.economictimes.indiatimes.com/rss/startups",
#         # "NDTV Gadgets": "http://gadgets.ndtv.com/rss/india/feeds",
#     },
    
#     "News": {
#         "Politics": "http://feeds.skynews.com/feeds/rss/politics.xml",
#         "World news": "http://feeds.reuters.com/Reuters/worldNews?format=xml",
#          "Cricket": "http://www.espncricinfo.com/rss/content/story/feeds/0.xml",
#         "Bangalore": "http://timesofindia.indiatimes.com/rssfeeds/-2128833038.cms",
        
#     },

#     "Open Source": {
#         "Liferea Blog": "http://feeds.feedburner.com/LifereaBlog",
#         "Linux Journel": "http://feeds.feedburner.com/LinuxJournal-BreakingNews?format=xml",
#         "Ubuntu Geek": "http://feeds.feedburner.com/UbuntuGeek?format=xml",
#         "Planet GNOME": "http://planet.gnome.org/atom.xml"
#     }, 
#     "Music": {
#         "iTunes": "https://itunes.apple.com/WebObjects/MZStore.woa/wpa/MRSS/featuredalbums/sf=143441/limit=25/rss.xml",
#         "BBC": "http://www.bbc.co.uk/music/genres/world/reviews.rss" 
#     }   
# }

class TreeWidget(QtGui.QWidget, treeUI.Ui_Form):
    """ 
    Tree list to hold subscription list
    """
    def __init__(self, parent =None):
        super(TreeWidget, self).__init__(parent)
        self.setupUi(self)

        # Add headers, Subscription and Count
        HEADERS = ( "Subscription", "")
        self.treeWidget.setColumnCount( len(HEADERS) )
        self.treeWidget.setHeaderLabels( HEADERS )

        # Add content menu for Right click in each item
        self.buildContextMenu()

        # Add 2 roots. 1: Feeds. 2: Search
        style = self.style()
        self.root = CustomTreeItem( self.treeWidget, constants.TREE_ITEM_ROOT, "Feeds", style=style )
        self.root.setIcon(0,self.style().standardIcon(QtGui.QStyle.SP_DirIcon))
        self.root.setExpanded(True)

        self.search = CustomTreeItem( self.treeWidget, constants.TREE_ITEM_FOLDER, "Search Results", feeds=[],  style=style)
        self.search.setIcon(0,self.style().standardIcon(QtGui.QStyle.SP_MessageBoxInformation))

        # Dict to build hierarchy of nodes/folders 
        folders = {
            0: self.root
        }

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        res = cursor.execute("SELECT * FROM folders")

        for row in res:
            folder_id, folder_title, folder_type, folder_parent, file_url = row

            parent_node = folders.get(folder_parent, self.root)
            node = CustomTreeItem( parent_node, folder_type, folder_title , style=style, parent_id = folder_parent, id = folder_id, url=file_url)
            node.setExpanded(True)

            folders[folder_id] = node
            if folder_type == constants.TREE_ITEM_ELEMENT:
                # If node is subscription, update it
                node.update()
        conn.close()

        ## Set Columns Width to match content:
        for column in range( self.treeWidget.columnCount() ):
            self.treeWidget.resizeColumnToContents( column )

    def buildContextMenu(self):
        """
        Creates context menu for tree items
        """
        # Important
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        actionUpdate = QtGui.QAction("Update", self)
        actionUpdate.triggered.connect(self.updateItem)
        self.addAction(actionUpdate)

        actionDelete = QtGui.QAction("Remove", self)
        actionDelete.triggered.connect(self.deleteItem)
        self.addAction(actionDelete)

        actionNewFolder = QtGui.QAction("New Folder", self)
        actionNewFolder.triggered.connect(self.newFolder)
        self.addAction(actionNewFolder)

        actionNewSubscription = QtGui.QAction("New Subscription", self)
        actionNewSubscription.triggered.connect(self.newSubscription)
        self.addAction(actionNewSubscription)
        
    def newFolder(self):
        try:
            dialog = QtGui.QDialog(self)
            dialog.setWindowTitle("Add new Folder")
            p = NewFolderDialog(self.getParent() , dialog)
            p.show()
            dialog.exec_()
        except Exception as e:
            print (e)

    def newSubscription(self):
        try:
            dialog = QtGui.QDialog(self)
            dialog.setWindowTitle("Add new Subscription")
            p = NewSubscriptionDialog(self.getParent() , dialog)
            p.show()
            dialog.exec_()
        except Exception as e:
            print (e)


    def deleteItem(self):
        """
        Deletes a subscription/folder. Invoked from context menu
        """

        if self.treeWidget.currentItem().item_type in (0,):
            return

        msgBox = QtGui.QMessageBox()
        msgBox.setText("Remove subscription")
        msgBox.setIcon(QtGui.QMessageBox.Critical)
        msgBox.setInformativeText("Do you want to remove subscription/folder?")
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtGui.QMessageBox.Cancel)
        ret = msgBox.exec_()

        if ret == QtGui.QMessageBox.Ok:
            root = self.treeWidget.invisibleRootItem()

            for item in self.treeWidget.selectedItems():
                self.silentDelete(item)
                if item.item_type == constants.TREE_ITEM_FOLDER:
                    # Finally remove the folder
                    dbhelper.delete_folder(item.id)
                (item.parent() or root).removeChild(item)

    def silentDelete(self, item):
        """
        Deletes node without message box. Useful in deleting folders
        """
        if item.item_type == constants.TREE_ITEM_FOLDER:
            # Folder
            child_count = item.childCount()
            for i in range(child_count):
                child = item.child(i)
                self.silentDelete(child)

        elif item.item_type == constants.TREE_ITEM_ELEMENT:
            # Subscription
            dbhelper.deleteSubscription(item.id, item.name)


    def getParent(self):
        """
        Finds immediate parent of currently selected node
        """
        currentItem = self.treeWidget.currentItem()
        parent = self.root
        if currentItem:
            if currentItem.item_type in (constants.TREE_ITEM_ROOT, constants.TREE_ITEM_FOLDER):
                parent = currentItem
            else:
                parent = currentItem.parent()
        return parent

    def updateItem(self, node = None):
        """
        Update selected/whole subscription/subtree
        """
        item =  self.treeWidget.currentItem() or self.root
        if not item:
            return
        item.updateAllChild(item)
