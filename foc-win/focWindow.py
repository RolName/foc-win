from PySide.QtGui import QMainWindow, QMessageBox, QLabel
from PySide import QtCore

class FocWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Foc for windows")
        labelText = "Args displayed here"
        self.label = QLabel(labelText)
        self.setCentralWidget(self.label)
    @QtCore.Slot(str)
    def receiveArgs(self, args):
        # bring window to front
        self.setWindowState(QtCore.Qt.WindowActive)
        self.activateWindow()

        self.label.setText(args)
    def showMessage(self, args):
        QMessageBox.information(self, self.tr("Received args from another instance"),args)
