import sys
import time
from io import BytesIO

from PIL import Image, UnidentifiedImageError
from PySide6.QtCore import QBuffer, QRect, Qt
from PySide6.QtGui import (
    QColor,
    QFont,
    QImage,
    QPainter,
    QPixmap,
    QTextDocument,
    QTextOption,
)
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

import utils
from enums import Direction
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Define attributes
        self.base_image = None

        self.direction: Direction = Direction.RIGHT
        self.recompute_timer = None

        # Setup the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textColorPicker.selectedColor = QColor(0, 0, 0)
        self.ui.backgroundColorPicker.selectedColor = QColor(255, 255, 255)
        self._current_image = None

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
        ):
            signal.connect(self.recompute_image)

        self.ui.actionSave.triggered.connect(self.save_image)
        self.ui.actionOpen.triggered.connect(self.open_image)
        self.ui.directionComboBox.currentTextChanged.connect(self._update_direction)

    @property
    def current_image(self):
        return self._current_image

    @current_image.setter
    def current_image(self, image: Image.Image):
        self._current_image = image

        # We make a thumnnail of the image for the display
        thumb = image.copy()
        thumb.thumbnail((700, 350))

        # ImageQt doesn't work, so we instead pass via IO
        data = thumb.tobytes("raw", "BGRA")
        q_image = QImage(data, thumb.width, thumb.height, QImage.Format.Format_ARGB32)

        pix = QPixmap.fromImage(q_image)
        self.ui.imageLabel.setPixmap(pix)

    def _update_direction(self):
        self.direction = Direction(self.ui.directionComboBox.currentText().lower())
        self.recompute_image()

    def recompute_image(self):
        if self.base_image is None:
            return

        im = self.make_image()
        self.current_image = im

    # def _markdown_to_qtextdocument(self, text: str):
    #     html_text = mistune.markdown(text)
    #     document = QTextDocument()
    #     document.setHtml(html_text)
    #     return document

    def _make_text_image(self, size: tuple[int, int], margin: int, text: str) -> QImage:
        width, height = size

        rect_left_offset = (
            0 if self.direction in (Direction.UP, Direction.DOWN) else margin
        )
        rect_top_offset = (
            0 if self.direction in (Direction.LEFT, Direction.RIGHT) else margin
        )
        rect = QRect(
            rect_left_offset,
            rect_top_offset,
            width - rect_left_offset,
            height - rect_top_offset,
        )

        if self.ui.markdownModeCheckBox.isChecked():
            img = self._make_markdown_text_image(size, rect, text)
        else:
            img = self._make_plain_text_image(size, rect, text)

        # Convert QImage to PIL image
        buffer = QBuffer()
        buffer.open(QBuffer.OpenModeFlag.ReadWrite)
        img.save(buffer, "PNG", 100)
        pil_im = Image.open(BytesIO(buffer.data()))
        return pil_im

    def _make_plain_text_image(
        self, size: tuple[int, int], rect: QRect, text: str
    ) -> QImage:
        width, height = size

        # Create a new image
        image = QImage(width, height, QImage.Format.Format_ARGB32)
        image.fill(self.ui.backgroundColorPicker.selectedColor)

        painter = QPainter(image)

        # Set the font properties
        painter.setFont(self.font_obj)
        painter.setPen(self.ui.textColorPicker.selectedColor)

        # Draw the text on the image
        painter.drawText(
            rect,
            Qt.TextFlag.TextWordWrap,
            text,
        )
        painter.end()

        return image

    def _make_markdown_text_image(
        self, size: tuple[int, int], rect: QRect, text: str
    ) -> Image.Image:
        width, height = size

        # Create a new image
        image = QImage(width, height, QImage.Format.Format_ARGB32)
        image.fill(self.ui.backgroundColorPicker.selectedColor)

        painter = QPainter(image)

        # Renders the markdown using a QTextDocument
        doc = QTextDocument()
        doc.setDocumentMargin(0)
        opt = QTextOption()
        # Could also be opt.WrapMode.WordWrap
        opt.setWrapMode(opt.WrapMode.WrapAtWordBoundaryOrAnywhere)
        doc.setDefaultFont(self.font_obj)
        doc.setDefaultTextOption(opt)
        doc.setTextWidth(rect.width())
        # This is the only way i found to set text color
        doc.setDefaultStyleSheet(
            f"body {{color: {self.ui.textColorPicker.selectedColor.name(QColor.NameFormat.HexRgb)};}}"
        )

        doc.setMarkdown(text, QTextDocument.MarkdownFeature.MarkdownDialectGitHub)
        # This is needed, otherwise the style isn't applied
        doc.setHtml(doc.toHtml())
        # This is needed for the margin
        painter.translate(rect.topLeft())
        doc.drawContents(painter)

        return image

    def make_image(self) -> Image.Image:
        size = self.border_size
        margin = self.margin
        if size == 0:
            return self.base_image

        # Compute the image's size based on the chosen direction
        h_size = self.base_image.size[0]
        w_size = self.base_image.size[1]
        if self.direction in (Direction.LEFT, Direction.RIGHT):
            h_size += size
        else:
            w_size += size
        # Compute the paste offset
        x_offset = size if self.direction == Direction.LEFT else 0
        y_offset = size if self.direction == Direction.UP else 0

        # Create the image with margin
        im = Image.new(
            self.base_image.mode,
            (
                h_size,
                w_size,
            ),
            (0, 0, 0, 0),  # We use a fully transparent color just in
            # case _make_text_image also uses a transparent color
        )
        im.paste(self.base_image, (x_offset, y_offset))

        # Add the text image
        if self.direction in (Direction.LEFT, Direction.RIGHT):
            text_img_size = (size, im.size[1])
        else:
            text_img_size = (im.size[0], size)

        text_img = self._make_text_image(
            size=text_img_size,
            margin=margin,
            text=self.ui.captionEdit.toPlainText(),
        )
        text_x_offset = im.size[0] - size if self.direction == Direction.RIGHT else 0
        text_y_offset = im.size[1] - size if self.direction == Direction.DOWN else 0
        im.paste(text_img, (text_x_offset, text_y_offset))

        return im

    def load_image(self, new_image: Image.Image):
        """Replaces the current loaded image with a new one"""
        self.base_image = new_image
        self.border_size = utils.recommended_border_size(
            new_image.width, new_image.height, self.direction
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
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error opening image")
            error_dialog.setText("This file format is not supported.")
            error_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
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
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error saving image")
            error_dialog.setText("This file extension is not supported.")
            error_dialog.setDetailedText(str(e))
            error_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
            error_dialog.exec()
            return

    @property
    def font_obj(self) -> QFont:
        """The font used for captionning, computed from the UI"""
        font_family = self.ui.fontComboBox.currentFont()
        font_size = self.ui.fontSizeSpinBox.value()
        font_family.setPointSize(font_size)
        return font_family

    @property
    def border_size(self) -> int:
        return self.ui.sizeSpinBox.value()

    @border_size.setter
    def border_size(self, value: int):
        self.ui.sizeSpinBox.setValue(value)

    @property
    def margin(self) -> int:
        return self.ui.marginSpinBox.value()

    @margin.setter
    def margin(self, value: int):
        self.ui.marginSpinBox.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
