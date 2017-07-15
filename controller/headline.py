from PySide import QtGui, QtCore
import moment

# Import ui file
from view import headline as headlineUI

from helpers import dateparser
from helpers import dbhelper


class HeadlineForm(QtGui.QWidget, headlineUI.Ui_Form):
    """
    Headline for list section
    """
    def __init__(self, item,parent =None):
        super(HeadlineForm, self).__init__(parent)
        self.setupUi(self)

        # Setting up values 
        self.item = item
        self.isRead = item.get('isread', 0)
        
        self.labelHeadline.setText(item.get('title', "Unable to load title"))

        # date = dateparser.parseDate(item["updated"])
        self.labelDate.setText(item.get("updated", "Error in date"))

        myFont=QtGui.QFont()

        if not self.isRead:
            myFont.setBold(True)                
            self.labelHeadline.setFont(myFont)
        else:
            myFont.setBold(False)                
            self.labelHeadline.setFont(myFont)

    def markRead(self):
        if self.isRead == 0:
            dbhelper.markRead(self.item.get('table',None), self.item.get('id', None))
            self.isRead = 1
            myFont=QtGui.QFont()
            myFont.setBold(False)
            self.labelHeadline.setFont(myFont)