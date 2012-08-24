from PySide import QtGui
from PySide.QtGui import QMainWindow, QWidget, QMessageBox, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PySide import QtCore
from PySide.QtCore import QSize
import os, sys
import regRegister

PROGID_NAME = "Foc.torrent.0.1"
WINDOWS_SIZE = QtCore.QSize(640, 480)

class FocWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Foc for windows")
        self.resize(WINDOWS_SIZE)
        self.exe_path = full_exe_path()
        self.progID = PROGID_NAME
        self.makeCentralWidget("Args displayed here")
        if len(sys.argv) > 1:
            self.computeArgs(sys.argv[1])
    @QtCore.Slot(str)
    def receiveArgs(self, args):
        self.bringToFront()
        self.showMessage("add " + args + " to FoC ?")
        self.computeArgs(args)
    @QtCore.Slot()
    def AssociateExtension(self):
        regRegister.associate_extension(self.progID, self.exe_path, '.torrent')
    @QtCore.Slot()
    def AssociateProtocol(self):
        regRegister.associate_protocol(self.exe_path, 'magnet')
    @QtCore.Slot()
    def bringToFront(self):
        self.showMinimized()
        self.setWindowState(QtCore.Qt.WindowActive)
        self.showNormal()
    @QtCore.Slot()
    def quit(self):
        QtGui.QApplication.instance().quit()
    def computeArgs(self, args):
        if args != "--show":
            self.label.setText(args)
    def makeCentralWidget(self, labelText):
        self.label = QLabel(labelText)
        mainLayout =  QVBoxLayout()
        mainLayout.addWidget(self.label)
        w = QWidget()
        w.setLayout(mainLayout)
        self.setCentralWidget(w)
    def showMessage(self, args):
        QMessageBox.information(self, self.tr("Received args from another instance"),args)

def full_exe_path():
    arg0 = sys.argv[0]
    fullPath = '"' + os.path.abspath(arg0) + '"'
    if arg0[-3:] == '.py':
        return 'python ' + fullPath
    elif arg0[-4:] == '.exe':
        return fullPath
    else:
        log('arg0[-4:] = ' + arg0[-4:] + '  assuming py2exe, assuming path is ' + fullPath)
        return fullPath
