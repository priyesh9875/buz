from PySide import QtGui, QtCore
import re

# Import ui file
from view import find as findUI

from helpers import constants

class FindDialog(QtGui.QWidget, findUI.Ui_Dialog):
    """
    Find dialog for taking search text
    """
    def __init__(self, tree_root, parent =None):
        super(FindDialog, self).__init__(parent)
        self.setupUi(self)

        # Connect required signals  
        self.buttonClose.clicked.connect(self.close)
        self.buttonFind.clicked.connect(self.handleButtonFind)
        
        # Tree reference is require for adding tree item under search
        self.treeWidget = tree_root

    def handleButtonFind(self):
        """
        Handles input from user, searching and updating tree/subscription list
        """

        name = self.lineEdit.text()
        result__feeds = []
        
        # Clear previous result
        self.treeWidget.search.feeds = []
        self.treeWidget.search.count = 0
        print (name)
        
        try:
            # Iterate over all subscription feeds
            it = QtGui.QTreeWidgetItemIterator(self.treeWidget.treeWidget)
            while it.value():
                try:
                    if it.value().item_type == constants.TREE_ITEM_ELEMENT:
                        node  = it.value()
                        for feed in node.feeds:
                            # Search in title and summary
                            res = re.search(name, feed['title'], re.I)
                            if not res:
                                res = re.search(name, feed['summary'], re.I)
                                if not res:
                                    continue

                                # Found in summary
                                else:
                                    result__feeds.append(feed)
                            # Found in title    
                            else:
                                result__feeds.append(feed)
                                

                except Exception as e:
                    print (e)
                    pass
                it +=1

            # Update result
            self.treeWidget.search.feeds = result__feeds
            self.treeWidget.search.count = len(result__feeds)
            print ("{} search result for {}".format(self.treeWidget.search.count, name))
            # Finally close fing dialog
            self.close()
        except Exception as e:
            print (e)


    def close(self):
        self.parent().close()