from typing import NamedTuple, Type, TypeVar, Dict, List, Tuple, Mapping
from types import MappingProxyType
import re
from collections import OrderedDict, defaultdict
from .exceptions import ProcessBouquetException
from .constants import get_size, Size
from .flower import FlowerSpecie

# required for type annotation of @classmethod
BouquetDesignType = TypeVar("BouquetDesignType", bound="BouquetDesign")

FlowersInDesign = Mapping[FlowerSpecie, int]
FlowersInDesignMutable = Dict[FlowerSpecie, int]

bouquet_design_pattern = re.compile(r"^([A-Z])([SL])((?:\d+[a-z])+)(\d+)$")
flowers_pattern = re.compile(r"(\d+)([a-z])")


class BouquetDesign(NamedTuple):
    """Class for Bouquet Design
    Holds all info about parts of the Bouquet

    Since recipe is immutable it is implemented as tuple.
    For Python 3.7 it can be replaced with dataclass type
    (see FLower definition)
    """

    name: str
    size: Size
    flowers: FlowersInDesign
    extra_flowers_num: int
    total_size: int

    @classmethod
    def parse(cls: Type[BouquetDesignType], recipe: str) -> BouquetDesignType:
        """Creates new Design instance from text recipe

        Tuple type does not allow to override __init__ method.
        Solution is to use class method or __new__ to implement parsing as part of the class
        """
        bouquet_design = bouquet_design_pattern.match(recipe)
        if not bouquet_design:
            raise ProcessBouquetException(f"'{recipe}' is not correct bouquet recipe")

        name, size, raw_flowers, raw_total_size = bouquet_design.groups()
        total_size = int(raw_total_size)
        raw_flowers_list: List[Tuple[str, str]] = flowers_pattern.findall(raw_flowers)
        flowers_list: List[Tuple[FlowerSpecie, int]] = [
            (FlowerSpecie(flower), int(num)) for num, flower in raw_flowers_list
        ]

        flowers = OrderedDict((flower, num) for flower, num in sorted(flowers_list, key=lambda item: item[0]))

        extra_flowers_num = total_size - sum(flowers.values())
        return cls(name, get_size(size), MappingProxyType(flowers), extra_flowers_num, total_size)

    def __str__(self):
        flowers = "".join(f"{num}{flower}" for flower, num in self.flowers.items())
        return f"{self.name}{self.size.value}{flowers}{self.total_size}"

    def __repr__(self):
        return self.__str__()


class Bouquet(object):
    """Representation of Bouquet instance
    Consists of flowers instead on abstract numbers of recipe
    Includes template for displaying itself, see __str_ method
    """

    def __init__(self, bouquet_design: BouquetDesign):
        self._bouquet_design = bouquet_design
        self._flowers: FlowersInDesignMutable = defaultdict(int, bouquet_design.flowers)

    def add_flowers(self, flower: FlowerSpecie, num: int):
        """
        Add extra Flowers
        """
        self._flowers[flower] += num

    def __str__(self):
        flowers = "".join(f"{num}{flower}" for flower, num in sorted(self._flowers.items(), key=lambda item: item[0]))
        return f"{self._bouquet_design.name}{self._bouquet_design.size.value}{flowers}"
