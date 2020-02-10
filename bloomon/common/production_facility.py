from typing import Dict, Optional, Generator
from .bouquet import Bouquet
from .constants import Size
from .io_manager import Reader
from .flower import Flower
from .bouquet_composer.abstract import Composer


class ProductionFacility(object):
    """ Imitates Facility
    Facade implementation for consuming Flowers and producing Bouquets
    """

    def __init__(self, composers: Dict[Size, Composer], reader: Reader):
        self._reader = reader
        self._composers = composers
        self._total_flowers = 0
        self._total_flowers_in_bouquets = 0

    def _get_next_flower(self) -> Generator[Flower, None, None]:
        """
        Get next element from Reader or stop
        """
        while True:
            raw_flower = self._reader.read()
            if not raw_flower:
                break
            yield Flower.parse(raw_flower)

    def _process_flower(self, flower: Flower) -> Optional[Bouquet]:
        """
        Send flower to composer
        """
        self._composers[flower.size].add_flower(flower)
        if self._composers[flower.size].is_created:
            return self._composers[flower.size].get_bouquet()
        return None

    def process(self) -> Generator[Bouquet, None, None]:
        """
        Main loop
        Get a flower from Reader, process it. Return bouquet if available
        """
        for flower in self._get_next_flower():
            bouquet = self._process_flower(flower)
            if bouquet:
                yield bouquet
