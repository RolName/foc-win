from distutils.core import setup  
import py2exe  
  
setup(windows=['foc-win.py'],
      options={"py2exe": {"includes": ["sip", "PyQt4.QtGui"]}})