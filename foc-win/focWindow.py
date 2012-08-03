from PySide.QtGui import QMainWindow, QMessageBox, QLabel
from PySide import QtCore

class FocWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Foc for windows")
        labelText = "<b>dallagnese.fr recipe</b><br /><br />\
        Allows you to start your program only once.<br />\
        Parameters of later calls can be handled by this application."
        self.label = QLabel(labelText)
        self.setCentralWidget(self.label)
    @QtCore.Slot(str)
    def receiveArgs(self, args):
        self.showMessage(args)
    def showMessage(self, args):
        QMessageBox.information(self, self.tr("Received args from another instance"),args)
