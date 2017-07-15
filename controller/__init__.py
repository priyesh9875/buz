import inspect
import os
# Append current path so that sub folders can access sibling packages
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.sys.path.append(currentdir)
