from copy import copy
from dataclasses import dataclass

from PIL import Image
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QColor, QFont, QImage, QPainter, QTextDocument, QTextOption

import utils
from enums import Direction


@dataclass
class CaptionGeneratorConfig:
    base_image: Image.Image

    direction: Direction
    border_size: int
    margin: int

    caption: str
    font: QFont
    markdown_mode: bool

    background_color: QColor
    text_color: QColor


DEFAULT_CONFIG = CaptionGeneratorConfig(
    base_image=None,
    direction=Direction.RIGHT,
    border_size=0,
    margin=0,
    caption="",
    font=QFont(),
    markdown_mode=False,
    background_color=QColor(0, 0, 0),
    text_color=QColor(255, 255, 255),
)


class CaptionGenerator:
    def __init__(self, config: CaptionGeneratorConfig = None) -> None:
        if config is None:
            config = copy(DEFAULT_CONFIG)

        self.config = config
        self.markdown_mode = False

    def _make_text_image(self, size: tuple[int, int], margin: int, text: str) -> QImage:
        width, height = size

        rect_left_offset = (
            0 if self.config.direction in (Direction.UP, Direction.DOWN) else margin
        )
        rect_top_offset = (
            0 if self.config.direction in (Direction.LEFT, Direction.RIGHT) else margin
        )
        rect = QRect(
            rect_left_offset,
            rect_top_offset,
            width - rect_left_offset,
            height - rect_top_offset,
        )

        if self.config.markdown_mode:
            img = self._make_markdown_text_image(size, rect, text)
        else:
            img = self._make_plain_text_image(size, rect, text)

        return utils.qimage_to_pil(img)

    def _make_plain_text_image(
        self, size: tuple[int, int], rect: QRect, text: str
    ) -> QImage:
        width, height = size

        # Create a new image
        image = QImage(width, height, QImage.Format.Format_ARGB32)
        image.fill(self.config.background_color)

        painter = QPainter(image)

        # Set the font properties
        painter.setFont(self.config.font)
        painter.setPen(self.config.text_color)

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
        image.fill(self.config.background_color)

        painter = QPainter(image)

        # Renders the markdown using a QTextDocument
        doc = QTextDocument()
        doc.setDocumentMargin(0)
        opt = QTextOption()
        # Could also be opt.WrapMode.WordWrap
        opt.setWrapMode(opt.WrapMode.WrapAtWordBoundaryOrAnywhere)
        doc.setDefaultFont(self.config.font)
        doc.setDefaultTextOption(opt)
        doc.setTextWidth(rect.width())
        # This is the only way i found to set text color
        doc.setDefaultStyleSheet(
            f"body {{color: {self.config.text_color.name(QColor.NameFormat.HexRgb)};}}"
        )

        doc.setMarkdown(text, QTextDocument.MarkdownFeature.MarkdownDialectGitHub)
        # This is needed, otherwise the style isn't applied
        doc.setHtml(doc.toHtml())
        # This is needed for the margin
        painter.translate(rect.topLeft())
        doc.drawContents(painter)

        return image

    def make_image(self) -> Image.Image:
        size = self.config.border_size
        margin = self.config.margin
        if size == 0:
            return self.config.base_image

        # Compute the image's size based on the chosen direction
        h_size = self.config.base_image.size[0]
        w_size = self.config.base_image.size[1]
        if self.config.direction in (Direction.LEFT, Direction.RIGHT):
            h_size += size
        else:
            w_size += size
        # Compute the paste offset
        x_offset = size if self.config.direction == Direction.LEFT else 0
        y_offset = size if self.config.direction == Direction.UP else 0

        # Create the image with margin
        im = Image.new(
            self.config.base_image.mode,
            (
                h_size,
                w_size,
            ),
            (0, 0, 0, 0),  # We use a fully transparent color just in
            # case _make_text_image also uses a transparent color
        )
        im.paste(self.config.base_image, (x_offset, y_offset))

        # Add the text image
        if self.config.direction in (Direction.LEFT, Direction.RIGHT):
            text_img_size = (size, im.size[1])
        else:
            text_img_size = (im.size[0], size)

        text_img = self._make_text_image(
            size=text_img_size,
            margin=margin,
            text=self.config.caption,
        )
        text_x_offset = (
            im.size[0] - size if self.config.direction == Direction.RIGHT else 0
        )
        text_y_offset = (
            im.size[1] - size if self.config.direction == Direction.DOWN else 0
        )
        im.paste(text_img, (text_x_offset, text_y_offset))

        return im
