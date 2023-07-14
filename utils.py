from enums import Direction


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
