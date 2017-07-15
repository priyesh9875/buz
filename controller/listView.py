from PySide import QtGui, QtCore

from  view import listView as listViewUI
from  controller.headline import HeadlineForm
import feedparser


# Import ui file
from view import listView as listViewUI


class ListWidget(QtGui.QWidget, listViewUI.Ui_Form):
    """
    List section to show headlines of selected subscription
    """
    def __init__(self, parent =None):
        super(ListWidget, self).__init__(parent)
        self.setupUi(self)
        
    
    def updateList(self, data):
        """
        Update list with given feeds
        asdsd
        """
        self.listWidget.clear()
        self.myQListWidget = self.listWidget

        # Append each feed item
        for d in data:

            item = HeadlineForm(d)
            
            # Create QListWidgetItem
            myQListWidgetItem = QtGui.QListWidgetItem(self.listWidget)
            
            # Set size hint, for paint method
            myQListWidgetItem.setSizeHint(item.sizeHint())

            self.listWidget.addItem(myQListWidgetItem)
            self.listWidget.setItemWidget(myQListWidgetItem, item)