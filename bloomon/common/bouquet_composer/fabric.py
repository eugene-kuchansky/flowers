from collections import defaultdict
from typing import List, Type, Dict

from .abstract import Composer
from ..bouquet import BouquetDesign
from ..constants import Size
from ..storage import FlowerStorage


def create_size_specific(bouquet_designs: List[BouquetDesign], composer_class: Type[Composer]) -> Dict[Size, Composer]:
    """
    Fabric for creating size specific Bouquet composers
    """
    bouquet_design_by_size: Dict[Size, List[BouquetDesign]] = defaultdict(list)

    for bouquet_design in bouquet_designs:
        bouquet_design_by_size[bouquet_design.size].append(bouquet_design)

    composers: Dict[Size, Composer] = {}

    for size in Size:
        composers[size] = composer_class(size, bouquet_design_by_size[size], FlowerStorage())

    return composers
