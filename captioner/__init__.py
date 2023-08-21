import sys
from typing import NoReturn

from PySide6.QtWidgets import QApplication

from .constants import VERSION
from .main_window import MainWindow


def run() -> NoReturn:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
