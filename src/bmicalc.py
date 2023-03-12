import sys
from PySide2.QtWidgets import QApplication
from mainWindow import MainWindow


if __name__ == '__main__':
    """Application Entry"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())