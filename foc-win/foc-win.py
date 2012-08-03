from focWindow import FocWindow
from qSingleApplication import QSingleApplication
import sys

if __name__ == "__main__":
    app = QSingleApplication(sys.argv)
    app.setApplicationName("Foc for Windows")
    myWindow = FocWindow()
    app.singleStart(myWindow)
    app.getInstanceArgs.connect(myWindow.showMessage)
    sys.exit(app.exec_())
