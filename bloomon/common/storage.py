from collections import defaultdict
from typing import Dict, List, Tuple
from .flower import FlowerSpecie
from .bouquet import FlowersInDesign
from .exceptions import StorageException


class FlowerStorage(object):
    """Keeps all Flowers before they are consumed
    Extract flowers for bouquet
    """

    def __init__(self):
        self._flowers: Dict[FlowerSpecie, int] = defaultdict(int)
        self._total: int = 0

    def add_flower(self, flower: FlowerSpecie):
        """
        Add new flower to storage
        """
        self._flowers[flower] += 1
        self._total += 1

    @property
    def flowers(self) -> List[Tuple[FlowerSpecie, int]]:
        return list(self._flowers.items())

    @property
    def total(self) -> int:
        return self._total

    def check_design_with_flowers(self, required_flowers: FlowersInDesign):
        """
        Verify if number of flowers in storage is sufficient for Design mandatory flowers
        """
        for flower, required_num in required_flowers.items():
            if self._flowers[flower] < required_num:
                return False
        return True

    def consume_flowers(self, flower: FlowerSpecie, num: int):
        if self._flowers[flower] < num:
            raise StorageException(
                f"Not enough '{flower}' flowers. Available in Storage: {self._flowers[flower]}. " f"Requested: {num}"
            )
        self._flowers[flower] -= num
        self._total -= num

    def __str__(self):
        flowers = ",".join(f"{num}{flower}" for flower, num in sorted(self._flowers.items(), key=lambda item: item[0]))
        return f"[{flowers}]"
