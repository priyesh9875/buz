from PySide import QtGui, QtCore

# Import ui file
from view import newSubscription as newSubscriptionUI

from urllib.parse import urlparse
from model.CustomTreeItem import CustomTreeItem


from helpers import dbhelper

class NewSubscriptionDialog(QtGui.QWidget, newSubscriptionUI.Ui_Dialog):
    """
    Dialog to take new subscription name and link as input and add it approprite position  
    """
    def __init__(self, tree_parent, parent =None):
        super(NewSubscriptionDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonClose.clicked.connect(self.close)
        self.buttonAdd.clicked.connect(self.handleButtonSubs)
        self.tree_parent = tree_parent

    def handleButtonSubs(self):
        url = self.lineUrl.text()
        name = self.lineName.text()
        try:
            print (self.tree_parent.id, self.tree_parent.parent_id)
            id = dbhelper.addSubscription(name,url, self.tree_parent.id)
            if id == -1 :

                msgBox = QtGui.QMessageBox()
                msgBox.setText("Error while adding")
                msgBox.setIcon(QtGui.QMessageBox.Critical)
                msgBox.setInformativeText("Subscription name already exist, please use different name")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok )
                msgBox.exec_()
                return

            item = CustomTreeItem(self.tree_parent, 2, name, url = url,style=self.tree_parent.style, id=id, parent_id = self.tree_parent.id )

            item.refreshFeeds()
            self.close()
        except Exception as e:
            print (e)


    def close(self):
        self.parent().close()
