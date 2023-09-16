from PyQt5.QtWidgets import QApplication
import sys
from src.main import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
