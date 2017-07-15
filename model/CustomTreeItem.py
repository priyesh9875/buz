from PySide import QtGui, QtCore
from helpers import constants
from helpers import dbhelper
import threading
import feedparser

class CustomTreeItem( QtGui.QTreeWidgetItem ):
    '''
    Custom QTreeWidgetItem with Widgets
    '''

    def __init__( self, parent, item_type, name, feeds = [], url = "", style = None, parent_id = 0, id = 0 ):

        super( CustomTreeItem, self ).__init__( parent )

        self.setText( 0, name )
        self.item_type = item_type
        self.feeds = feeds
        self.url = url
        
        # Required to maintain folder hierercy
        self.parent_id = parent_id
        # Required to sync with database
        self.id = id

        # Required for context menu
        self.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled )

        self.countWidget = QtGui.QLabel("0")
        self.count = 0
        if item_type not in (constants.TREE_ITEM_ROOT, constants.TREE_ITEM_FOLDER):
            self.countWidget.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.treeWidget().setItemWidget( self, 1, self.countWidget )

        if style:
            if item_type is constants.TREE_ITEM_FOLDER:
                self.setIcon(0,style.standardIcon(QtGui.QStyle.SP_DirIcon))
            elif item_type is constants.TREE_ITEM_ELEMENT:
                self.setIcon(0,style.standardIcon(QtGui.QStyle.SP_FileIcon))

        self.style = style

    @property
    def name(self):
        '''
        Return name ( 1st column text )
        '''
        return self.text(0)


    @property
    def count(self):
        '''
        Return name ( 1st column text )
        '''
        return self.countWidget.text()

    @count.setter
    def count(self, value):
        '''
        Return name ( 1st column text )
        '''
        self.countWidget.setText(str(value))

    
    def update(self):
        """
        Read from database
        """
        self.feeds = dbhelper.readFeeds(self.id, self.name)
        self.count = len(self.feeds)
    

    def updateAllChild(self, node):
        """
        Recursively update all subscription
        """
        if not node:
            return
        if node.item_type == 2 :
            node.refreshFeeds()
        
        child_count = node.childCount()
        for i in range(child_count):
            child = node.child(i)
            child.updateAllChild(child)


    def refreshFeeds(self):
        """
        Spawn new thread so that main gui thread is not blocked 
        """
        try:
            threading.Thread(target=self.fetchFeeds).start()
        except Exception as e:
            print (self.url, e)
    
    def fetchFeeds(self):
        print ("Updating ", self.name)
        res = feedparser.parse(self.url)

        if len(self.feeds) == 0:
            # First time
            dbhelper.writeFeeds(self.name, res.entries)
            
        elif len(self.feeds) > 0 and len(res.entries) > 0:
            # Sync database
            last = self.feeds[0]

            for pos, feed in enumerate(res.entries):
                if feed['title'] == last['title'] and feed['link'] == last['link']:
                    print (pos)
                    res.entries = res.entries[:pos:]
                    break

            dbhelper.writeFeeds(self.name, res.entries)
            res.entries = dbhelper.readFeeds(self.id, self.name)

        self.feeds = res.entries
        self.count = len(self.feeds)
        
        print (self.name, self.url, self.count)

        
