"""This widget works, but i dropped using it as i find a regular combobox looks better"""

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame, QHBoxLayout, QPushButton

from enums import Direction

BUTTON_ICONS = {
    Direction.LEFT: "./resources/arrow-left-square.svg",
    Direction.RIGHT: "./resources/arrow-right-square.svg",
    Direction.UP: "./resources/arrow-up-square.svg",
    Direction.DOWN: "./resources/arrow-down-square.svg",
}

BUTTON_ICONS_SELECTED = {
    Direction.LEFT: "./resources/arrow-left-square-fill.svg",
    Direction.RIGHT: "./resources/arrow-right-square-fill.svg",
    Direction.UP: "./resources/arrow-up-square-fill.svg",
    Direction.DOWN: "./resources/arrow-down-square-fill.svg",
}


class DirectionPickerWidget(QFrame):
    """A widget that allows the user to pick a cardinal direction"""

    directionChanged = Signal(Direction)

    def __init__(self, parent=None, button_size: int = 25):
        super().__init__(parent)
        self.selectedDirection: Direction = Direction.RIGHT

        self.setupUi(button_size)

    def setupUi(self, button_size: int):
        # Create the layout for the widget
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Create the four square buttons
        self.buttons: list[QPushButton] = []
        for d in (Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN):
            button = QPushButton()
            self.buttons.append(button)
            button.setProperty("direction", d)
            button.clicked.connect(self.button_clicked)
            button.setFixedSize(button_size, button_size)
            layout.addWidget(button)

        self.setLayout(layout)
        self._update_buttons_icons()

    def _update_buttons_icons(self):
        for btn in self.buttons:
            btn_direction = btn.property("direction")
            if btn_direction == self.selectedDirection:
                icon_path = BUTTON_ICONS_SELECTED[btn_direction]
            else:
                icon_path = BUTTON_ICONS[btn_direction]
            qicon = QIcon(icon_path)
            btn.setIcon(qicon)

    def button_clicked(self):
        sender: QPushButton = self.sender()
        direction: Direction = sender.property("direction")
        self.selectedDirection = direction
        self._update_buttons_icons()
        self.directionChanged.emit(direction)
