from PySide.QtGui import QMainWindow, QWidget, QMessageBox, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PySide import QtCore
import os, sys
import regRegister

HANDLER_NAME = "Foc.torrent"
HANDLER_VERSION = "0.1"
PROGID_NAME = HANDLER_NAME + '.' + HANDLER_VERSION

class FocWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Foc for windows")
        self.exe_path = full_exe_path()
        self.progID = PROGID_NAME
        self.makeCentralWidget("Args displayed here")
        if len(sys.argv) > 1:
            self.receiveArgs(sys.argv[1])
    @QtCore.Slot(str)
    def receiveArgs(self, args):
        # bring window to front
        self.setWindowState(QtCore.Qt.WindowActive)
        self.activateWindow()
        
        if args != "--show":
            self.label.setText(args)
    @QtCore.Slot()
    def AssociateExtension(self):
        regRegister.associate_extension(self.progID, self.exe_path, '.torrent')
    @QtCore.Slot()
    def AssociateProtocol(self):
        regRegister.associate_protocol(self.exe_path, 'magnet')
    def makeCentralWidget(self, labelText):
        self.regExtBtn = QPushButton('register .torrent extension')
        self.regExtBtn.clicked.connect(self.AssociateExtension)
        self.regProtBtn = QPushButton('Register magnet:// protocol')
        self.regProtBtn.clicked.connect(self.AssociateProtocol)
        self.label = QLabel(labelText)
        
        hLayout =  QHBoxLayout()
        hLayout.addWidget(self.regExtBtn)
        hLayout.addWidget(self.regProtBtn)
        mainLayout =  QVBoxLayout()
        mainLayout.addWidget(self.label)
        mainLayout.addLayout(hLayout)
        
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
