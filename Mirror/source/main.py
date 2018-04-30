import locale
import sys

from PyQt5.QtWidgets import QApplication

from source.UI.main_window import MainWindow

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'ru')
    print("Starting application...")

    APP = QApplication(sys.argv)
    WINDOW = MainWindow()
    sys.exit(APP.exec_())
