from abc import ABC, abstractmethod
from typing import List, Optional
from ..storage import FlowerStorage
from ..constants import Size
from ..exceptions import BouquetComposerException
from ..bouquet import BouquetDesign, Bouquet
from ..flower import Flower, FlowerSpecie


class Composer(ABC):
    """ Abstract class for Bouquet composers
    Holds interfaces and common operations
    """

    def __init__(self, size: Size, bouquet_designs: List[BouquetDesign], storage: FlowerStorage):
        self._size: Size = size
        self._bouquet_designs: List[BouquetDesign] = bouquet_designs
        self._created_bouquet: Optional[BouquetDesign] = None
        self._storage: FlowerStorage = storage
        self._last_flower: Optional[FlowerSpecie] = None
        self._post_init()

    @abstractmethod
    def _post_init(self):
        pass

    def add_flower(self, flower: Flower):
        """
        Consume new  Flower to Storage
        """
        if self._created_bouquet:
            raise BouquetComposerException("New flower cannot be processed until created bouquet is consumed")
        self._storage.add_flower(flower.specie)
        self._last_flower = flower.specie

    @property
    def is_created(self) -> bool:
        """
        Check if any Bouquet can be made wit existing flowers
        """
        self._created_bouquet = self._create_bouquet()
        return bool(self._created_bouquet)

    @abstractmethod
    def _create_bouquet(self) -> Optional[BouquetDesign]:
        pass

    def get_bouquet(self) -> Bouquet:
        """
        Create Bouquet from design, remove flowers from Storage
        """
        if not self._created_bouquet:
            raise BouquetComposerException("Bouquet must be created before consuming")
        bouquet = self._consume_flowers()
        self._created_bouquet = None
        return bouquet

    @abstractmethod
    def _consume_flowers(self):
        pass
