from PySide import QtGui, QtCore

# Import ui file
from view import preferences as preferencesUI

class PreferencesDialog(QtGui.QWidget, preferencesUI.Ui_Dialog):
    """ Preferences dialog"""
    def __init__(self, parent =None):
        super(PreferencesDialog, self).__init__(parent)
        self.setupUi(self)

