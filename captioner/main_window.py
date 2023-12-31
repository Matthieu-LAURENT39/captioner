from __future__ import annotations

from PIL import Image, UnidentifiedImageError
from PySide6.QtCore import Slot, QSignalBlocker
from PySide6.QtGui import (
    QColor,
    QFont,
    QPixmap,
    QDesktopServices,
    QDragEnterEvent,
    QDropEvent,
)
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from . import constants, utils
from .caption_generator import CaptionGenerator, CaptionGeneratorConfig
from .enums import Direction, HorizontalAlignment, VerticalAlignment
from .thread import ImageGeneratorThread
from .ui.ui_mainwindow import Ui_MainWindow


class CaptionGeneratorConfigUI(CaptionGeneratorConfig):
    """Automatically generates the config based on the current UI"""

    def __init__(self, main_window: "MainWindow") -> None:
        self._window = main_window

    @property
    def base_image(self) -> Image.Image | None:
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
    def left_margin(self) -> int:
        return self._window.ui.leftMarginSpinBox.value()

    @property
    def right_margin(self) -> int:
        return self._window.ui.rightMarginSpinBox.value()

    @property
    def top_margin(self) -> int:
        return self._window.ui.topMarginSpinBox.value()

    @property
    def bottom_margin(self) -> int:
        return self._window.ui.bottomMarginSpinBox.value()

    @property
    def draw_margins(self) -> bool:
        return self._window.ui.actionDrawMargins.isChecked()

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
        return self._window.ui.actionMarkdownMode.isChecked()

    @property
    def background_color(self) -> QColor:
        return self._window.ui.backgroundColorPicker.selectedColor

    @property
    def text_color(self) -> QColor:
        return self._window.ui.textColorPicker.selectedColor

    @property
    def text_horizontal_alignment(self) -> HorizontalAlignment:
        return self._window.ui.textHAlignmentComboBox.currentData()

    @property
    def text_vertical_alignment(self) -> VerticalAlignment:
        return self._window.ui.textVAlignmentComboBox.currentData()


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
        self.setAcceptDrops(True)

        # Setup the comboboxes
        for h_align in (
            HorizontalAlignment.LEFT,
            HorizontalAlignment.CENTER,
            HorizontalAlignment.RIGHT,
        ):
            self.ui.textHAlignmentComboBox.addItem(h_align.value.capitalize(), h_align)
        for v_align in (
            VerticalAlignment.TOP,
            VerticalAlignment.CENTER,
            VerticalAlignment.BOTTOM,
        ):
            self.ui.textVAlignmentComboBox.addItem(v_align.value.capitalize(), v_align)

        # Setup the caption generator
        self.generator_config = CaptionGeneratorConfigUI(self)
        self.generator = CaptionGenerator(self.generator_config)

        self.image_thread = ImageGeneratorThread(self.generator)
        self.image_thread.imageGenerated.connect(self.image_generated)
        self.image_thread.start()

        # Connect signals
        for signal in (
            self.ui.sizeSpinBox.valueChanged,
            self.ui.leftMarginSpinBox.valueChanged,
            self.ui.rightMarginSpinBox.valueChanged,
            self.ui.topMarginSpinBox.valueChanged,
            self.ui.bottomMarginSpinBox.valueChanged,
            self.ui.captionEdit.textChanged,
            self.ui.fontComboBox.currentFontChanged,
            self.ui.fontSizeSpinBox.valueChanged,
            self.ui.textColorPicker.colorChanged,
            self.ui.backgroundColorPicker.colorChanged,
            self.ui.actionMarkdownMode.changed,
            self.ui.directionComboBox.currentIndexChanged,
            self.ui.actionDrawMargins.triggered,
            self.ui.textHAlignmentComboBox.currentIndexChanged,
            self.ui.textVAlignmentComboBox.currentIndexChanged,
        ):
            signal.connect(self._value_changed)

        # File menu
        self.ui.actionOpen.triggered.connect(self.open_image)
        self.ui.actionSave.triggered.connect(self.save_image)
        self.ui.actionCopyToClipboard.triggered.connect(self.copy_to_clipboard)
        # Edit menu
        self.ui.actionRender.triggered.connect(self.recompute_image)
        # Help menu
        self.ui.actionAbout.triggered.connect(self.showAboutDialog)
        self.ui.actionSourceCode.triggered.connect(
            lambda: QDesktopServices.openUrl(constants.SOURCE_CODE_URL)
        )

        # Linked margins
        self.ui.actionLinkMargins.changed.connect(self._linked_margin_changed)
        self.ui.leftMarginSpinBox.valueChanged.connect(
            self._left_margin_spinbox_updated
        )

        # Disable image-related controls
        self._toggle_image_controls(False)

    @property
    def current_image(self):
        return self._current_image

    @current_image.setter
    def current_image(self, image: Image.Image):
        self._current_image = image
        # Enable image-related controls
        self._toggle_image_controls(True)
        # Display the image
        self._display_image(image)

    def _display_image(self, image: Image.Image):
        # We make a thumnnail of the image for the display
        thumb = image.copy()
        thumb.thumbnail((700, 350))

        q_image = utils.pil_to_qimage(thumb)
        pix = QPixmap.fromImage(q_image)
        self.ui.imageLabel.setPixmap(pix)

    @Slot()
    def _value_changed(self) -> None:
        if not self.ui.actionAutoRender.isChecked():
            return
        self.recompute_image()

    def recompute_image(self):
        """Regenerates the displayed image"""
        if self.base_image is None:
            return

        # Queue a regeneration of the image
        self.image_thread.refresh_image()

    @Slot(Image.Image)
    def image_generated(self, im: Image.Image):
        """Signal called whenever a new image has been generated"""
        self.current_image = im

    def _toggle_image_controls(self, enable: bool):
        """Enable/disable controls that require an image to be present"""
        self.ui.actionSave.setEnabled(enable)
        self.ui.actionCopyToClipboard.setEnabled(enable)

    def _linked_margin_changed(self):
        """Toggles the linking of the 4 margins field"""
        linked = self.ui.actionLinkMargins.isChecked()
        for spinbox in (
            self.ui.topMarginSpinBox,
            self.ui.rightMarginSpinBox,
            self.ui.bottomMarginSpinBox,
        ):
            spinbox.setEnabled(not linked)

    def _left_margin_spinbox_updated(self):
        """Called when the left margin's value is changed"""
        # Do nothing special if margins linking isn't enabled
        if not self.ui.actionLinkMargins.isChecked():
            return

        value = self.ui.leftMarginSpinBox.value()
        for spinbox in (
            self.ui.topMarginSpinBox,
            self.ui.rightMarginSpinBox,
            self.ui.bottomMarginSpinBox,
        ):
            spinbox.setValue(value)

    def load_image(self, new_image: Image.Image):
        """Replaces the current loaded image with a new one"""
        # Remove whatever is on the label right now
        self.ui.imageLabel.setText("")
        self.ui.imageLabel.setStyleSheet("")

        self.base_image = new_image
        self.generator_config.border_size = utils.recommended_border_size(
            new_image.width, new_image.height, self.generator_config.direction
        )
        self.recompute_image()

    def load_image_from_file(self, filename: str):
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

    def open_image(self):
        """Prompts the user to load an image"""
        filename, filt = QFileDialog.getOpenFileName(
            parent=self,
            caption="Open image to caption",
            filter="Images (*.png *.jpg *.jpeg *.jpe *.bmp *.webp);;All files (*)",
        )
        if not filename:
            return

        self.load_image_from_file(filename)

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

    def copy_to_clipboard(self):
        """Copies the image to the clipboard"""
        if self.current_image is None:
            return

        QApplication.clipboard().setImage(utils.pil_to_qimage(self.current_image))

    def showAboutDialog(self):
        QMessageBox.about(
            self,
            "Captioner - About",
            f"""Captioner v{constants.VERSION}
{constants.COPYRIGHT}

This program is released under the GPL v3 (or later).
If you enjoy this program, please leave a star on github!""",
        )

    # We need to accept the QDragEnterEvent or the QDropEvent won't be fired
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasImage() or event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasImage():
            self.load_image(utils.qimage_to_pil(event.mimeData().imageData()))

        elif event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            image_path = urls[0].toLocalFile()
            self.load_image_from_file(image_path)
            event.acceptProposedAction()
