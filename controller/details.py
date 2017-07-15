from PySide import QtGui, QtCore

# Import ui file
from view import details as detailsUI

class DetailsForm(QtGui.QWidget, detailsUI.Ui_Form):
    """
    Details form for feed details
    """
    def __init__(self, parent =None,):
        super(DetailsForm, self).__init__(parent)
        self.setupUi(self)

        self.item = {
            "link": "http://google.com",
        }

        self.toolButton.clicked.connect(self.openWebPage)
    
    def updateData(self, item):
        """
        Update details section with new data
        """
        
        self.item = item
        self.labelFeed.setText(item['title'])
        self.textBrowser.setHtml(item['summary'])
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.anchorClicked.connect(self.openWebPage)
 
    def openWebPage(self, url = None):
        """
        Call desktop service to open default browser
        TODO: Check for invalid/local url
        """
        try:
            if not url:
                QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.item["link"]))
            else:
                QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))
                
        except Exception as e:
            print (url[:50:], e)
            pass