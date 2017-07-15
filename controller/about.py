from PySide import QtGui, QtCore

# Import ui file
from view import about as aboutUI

class AboutDialog(QtGui.QWidget, aboutUI.Ui_Dialog):
    """ About dialog box"""
    def __init__(self, parent =None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)

