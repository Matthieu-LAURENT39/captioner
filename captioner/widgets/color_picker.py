from PySide6.QtCore import Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QColorDialog, QFrame


class ColorPickerWidget(QFrame):
    """A widget that allows the user to pick a QColor"""

    colorChanged = Signal(QColor)

    def __init__(self, parent=None, defaultColor: QColor = QColor(0, 0, 0)):
        super().__init__(parent)

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.mousePressEvent = lambda e: self.pick_color()

        self.selectedColor = defaultColor

    @property
    def selectedColor(self) -> QColor:
        return self._selected_color

    @selectedColor.setter
    def selectedColor(self, new_color: QColor):
        # if new_color == self._selected_color:
        #     return
        self._selected_color = new_color
        self.setStyleSheet(f"background-color: {self.selectedColor.name()};")

    def pick_color(self):
        """Prompts the user to pick a color"""
        dialog = QColorDialog(self.selectedColor)
        dialog.setOption(QColorDialog.ColorDialogOption.ShowAlphaChannel)
        if dialog.exec():
            self.selectedColor = dialog.selectedColor()
            self.colorChanged.emit(self.selectedColor)
