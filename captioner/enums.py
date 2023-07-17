from enum import Enum, StrEnum


class Direction(StrEnum):
    """Represents a cardinal direction"""

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class HorizontalAlignment(Enum):
    """Represents a direction for horizontal text alignment"""

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class VerticalAlignment(Enum):
    """Represents a direction for vertical text alignment"""

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"
