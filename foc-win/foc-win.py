from focWindow import FocWindow
from qSingleApplication import QSingleApplication
import sys

if __name__ == "__main__":
    app = QSingleApplication(sys.argv)
    app.setApplicationName("Foc for Windows")
    myWindow = FocWindow()
    app.singleStart(myWindow)
    sys.exit(app.exec_())
