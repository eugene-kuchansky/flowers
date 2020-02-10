import enum


class Size(enum.Enum):
    SMALL = "S"
    LARGE = "L"


sizes = {"S": Size.SMALL, "L": Size.LARGE}


def get_size(size: str) -> Size:
    return sizes[size]


READ_SEPARATOR = ""
