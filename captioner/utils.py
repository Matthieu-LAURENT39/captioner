from io import BytesIO

from PIL import Image
from PySide6.QtCore import QBuffer
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QMessageBox

from .enums import Direction


def recommended_border_size(
    img_width: int, img_height: int, direction: Direction
) -> int:
    is_landscape = img_height < img_width

    if direction in (Direction.LEFT, Direction.RIGHT):
        if is_landscape:
            return img_width * (3 / 4)
        else:
            return img_width
    # Direction is UP or DOWN
    else:
        return img_height / 2


#! This function is really slow, and is a bottleneck. Needs optimizing
# The main culprit is the call to im.save
def qimage_to_pil(im: QImage, /) -> Image.Image:
    """Converts a QImage to a PIL image"""
    buffer = QBuffer()
    buffer.open(QBuffer.OpenModeFlag.ReadWrite)
    im.save(buffer, "PNG", 100)
    return Image.open(BytesIO(buffer.data()))


def pil_to_qimage(im: Image.Image, /) -> QImage:
    """Converts a PIL image to a QImage"""
    # ImageQt doesn't work, so we instead pass via IO
    data = im.tobytes("raw", "BGRA")
    return QImage(data, im.width, im.height, QImage.Format.Format_ARGB32)


def exception_to_msgbox(e: Exception, /, *, show_traceback=True) -> QMessageBox:
    """
    Convenience function to generate a msgbox from an exception
    You should use setWindowTitle and setText afterwards
    """
    msgbox = QMessageBox()
    msgbox.setWindowTitle("Error")
    msgbox.setIcon(QMessageBox.Icon.Critical)
    msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
    if show_traceback:
        msgbox.setDetailedText(str(e))
    return msgbox
