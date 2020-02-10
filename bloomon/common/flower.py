from typing import NamedTuple, Type, TypeVar, NewType
from enum import Enum
import string
import re
from .exceptions import ProcessFlowerException
from .constants import get_size, Size

# required for type annotation of @classmethod
FlowerType = TypeVar("FlowerType", bound="Flower")

# FlowerSpecie = Enum("FlowerName", zip(string.ascii_lowercase, string.ascii_lowercase))
FlowerSpecie = NewType("FlowerSpecie", str)

flower_pattern = re.compile("^([a-z])([SL])$")


class Flower(NamedTuple):
    """Class for Flower recipe
    Holds all info about parts of the Flower

    Since recipe is immutable it is implemented as tuple.
    For Python 3.7 it can be replaced with dataclass type
    (see BouquetDesign definition)
    """

    specie: FlowerSpecie
    size: Size

    @classmethod
    def parse(cls: Type[FlowerType], flower_definition: str) -> FlowerType:
        match = flower_pattern.match(flower_definition)
        if not match:
            raise ProcessFlowerException(f"'{flower_definition}' is not correct flower")
        specie, size = match.groups()
        return cls(FlowerSpecie(specie), get_size(size))

    def __str__(self):
        return f"{self.specie}{self.size.value}"

    def __repr__(self):
        return self.__str__()


#
#
# class FlowerItem(object):
#     specie: FlowerSpecie
#     num: int
#
#     def __init__(self, specie: str, num: int):
#         self.specie = specie
#         self.num = num
#
#     def __str__(self):
#         return f"{self.num}{self.specie.value}"
