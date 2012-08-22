from distutils.core import setup  
import py2exe  
  
setup(
	windows = [
        {
            "script": "foc-win.py",
            "icon_resources": [(1, "foc-logo.ico")]
        }
    ],
    options={"py2exe": {"includes": ["PySide.QtGui"]}}
)
