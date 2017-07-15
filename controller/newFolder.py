from PySide import QtGui, QtCore

# Import ui file
from view import newFolder as NewFolderUI

import sqlite3

from model.CustomTreeItem import CustomTreeItem

from helpers.dbhelper import DATABASE

class NewFolderDialog(QtGui.QWidget, NewFolderUI.Ui_Dialog):
    """
    Dialog to take new folder name as input and add folder approprite position  
    """
    def __init__(self, tree_parent, parent =None):
        super(NewFolderDialog, self).__init__(parent)
        self.setupUi(self)

        self.buttonClose.clicked.connect(self.close)
        self.buttonAdd.clicked.connect(self.handleButtonAdd)
        self.tree_parent = tree_parent

    def handleButtonAdd(self):
        name = self.lineEdit.text()
        try:
 
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()

            row = cursor.execute("INSERT INTO folders (title, type, parent ) values (?,?,?) ", (name, 1, self.tree_parent.id))

 
            folder = CustomTreeItem(self.tree_parent, 1, name, style=self.tree_parent.style, parent_id = self.tree_parent.id, id=cursor.lastrowid )
            folder.setExpanded(True)

            conn.commit()
            conn.close()

            self.close()
        except Exception as e:
            print (e)


    def close(self):
        self.parent().close()
