from __future__ import annotations

import sys

from PIL import Image, UnidentifiedImageError
from PySide6.QtGui import QColor, QFont, QPixmap
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

import utils
from caption_generator import CaptionGenerator, CaptionGeneratorConfig
from enums import Direction
from ui.ui_mainwindow import Ui_MainWindow


class CaptionGeneratorConfigUI(CaptionGeneratorConfig):
    """Automatically generates the config based on the current UI"""

    def __init__(self, main_window: "MainWindow") -> None:
        self._window = main_window

    @property
    def base_image(self) -> Image.Image:
        return self._window.base_image

    @property
    def direction(self) -> Direction:
        return Direction(self._window.ui.directionComboBox.currentText().lower())

    @property
    def border_size(self) -> int:
        return self._window.ui.sizeSpinBox.value()

    @border_size.setter
    def border_size(self, value: int):
        self._window.ui.sizeSpinBox.setValue(value)

    @property
    def margin(self) -> int:
        return self._window.ui.marginSpinBox.value()

    @property
    def caption(self) -> str:
        return self._window.ui.captionEdit.toPlainText()

    @property
    def font(self) -> QFont:
        font_family = self._window.ui.fontComboBox.currentFont()
        font_size = self._window.ui.fontSizeSpinBox.value()
        font_family.setPointSize(font_size)
        return font_family

    @property
    def markdown_mode(self) -> bool:
        return self._window.ui.markdownModeCheckBox.isChecked()

    @property
    def background_color(self) -> QColor:
        return self._window.ui.backgroundColorPicker.selectedColor

    @property
    def text_color(self) -> QColor:
        return self._window.ui.textColorPicker.selectedColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textColorPicker.selectedColor = QColor(0, 0, 0)
        self.ui.backgroundColorPicker.selectedColor = QColor(255, 255, 255)
        self.base_image = None
        self._current_image = None

        # Setup the caption generator
        self.generator_config = CaptionGeneratorConfigUI(self)
        self.generator = CaptionGenerator(self.generator_config)

        # Connect signals
        for signal in (
            self.ui.sizeSpinBox.valueChanged,
            self.ui.marginSpinBox.valueChanged,
            self.ui.captionEdit.textChanged,
            self.ui.fontComboBox.currentFontChanged,
            self.ui.fontSizeSpinBox.valueChanged,
            self.ui.textColorPicker.colorChanged,
            self.ui.backgroundColorPicker.colorChanged,
            self.ui.markdownModeCheckBox.stateChanged,
            self.ui.directionComboBox.currentTextChanged,
        ):
            signal.connect(self.recompute_image)

        self.ui.actionSave.triggered.connect(self.save_image)
        self.ui.actionOpen.triggered.connect(self.open_image)

    @property
    def current_image(self):
        return self._current_image

    @current_image.setter
    def current_image(self, image: Image.Image):
        self._current_image = image

        # We make a thumnnail of the image for the display
        thumb = image.copy()
        thumb.thumbnail((700, 350))

        q_image = utils.pil_to_qimage(thumb)
        pix = QPixmap.fromImage(q_image)
        self.ui.imageLabel.setPixmap(pix)

    def recompute_image(self):
        if self.base_image is None:
            return

        im = self.generator.make_image()
        self.current_image = im

    def load_image(self, new_image: Image.Image):
        """Replaces the current loaded image with a new one"""
        self.base_image = new_image
        self.generator_config.border_size = utils.recommended_border_size(
            new_image.width, new_image.height, self.generator_config.direction
        )
        self.recompute_image()

    def open_image(self):
        """Prompts the user to load an image"""
        filename, filt = QFileDialog.getOpenFileName(
            parent=self,
            caption="Open image to caption",
            filter="Images (*.png *.jpg *.jpeg *.jpe *.bmp *.webp);;All files (*)",
        )
        if not filename:
            return

        try:
            img = Image.open(filename).convert("RGBA")
        except UnidentifiedImageError as e:
            # This is raised when PIL can't save to a specific format
            error_dialog = utils.exception_to_msgbox(e)
            error_dialog.setWindowTitle("Error opening image")
            error_dialog.setText("This file format is not supported.")
            error_dialog.exec()
            return

        self.load_image(img)

    def save_image(self):
        """Prompts the user to save the image"""
        if self.current_image is None:
            return

        filename, filt = QFileDialog.getSaveFileName(
            parent=self,
            caption="Save caption",
            dir="caption.png",
            filter="PNG (*.png);;JPEG (*.jpg *.jpeg *.jpe);;All files (*)",
        )
        if not filename:
            return

        try:
            self.current_image.save(filename)
        except ValueError as e:
            # This is raised when PIL can't save to a specific format
            error_dialog = utils.exception_to_msgbox(e, show_traceback=False)
            error_dialog.setWindowTitle("Error saving image")
            error_dialog.setText("This file extension is not supported.")
            error_dialog.exec()
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
