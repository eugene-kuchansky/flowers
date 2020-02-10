from bisect import bisect_right
from .abstract import Composer
from ..bouquet import Bouquet
from ..exceptions import BouquetComposerException


class SimpleComposer(Composer):
    """
    Naive implementation
    Creates Bouquet once any first recipe matches number of its component flowers
    """

    def _post_init(self):
        self._bouquet_designs = sorted(self._bouquet_designs, key=lambda item: item.total_size)
        self._bouquets_total_sizes_sorted = [b.total_size for b in self._bouquet_designs]

    def _find_available_bouquets_by_total_size(self):
        """
        Find in sorted list index of the most right Bouquet Design
        with total Flowers number equal of less than number of all available Flowers
        Zero means nothing found
        """
        return bisect_right(self._bouquets_total_sizes_sorted, self._storage.total)

    def _create_bouquet(self):
        """
        Find all Bouquet Designs with total number of Flowers less or equal available number of Flowers in Storage
        Then check of the each found Bouquet Design if required number and species of Flowers are available
        If both conditions met then produce the first matched Bouquet Design
        """
        ind = self._find_available_bouquets_by_total_size()

        if not ind:
            return None

        for bouquet_design in self._bouquet_designs[:ind]:
            if self._storage.check_design_with_flowers(bouquet_design.flowers):
                return bouquet_design
        return None

    def _consume_flowers(self) -> Bouquet:
        """
        Take flowers from Storage and create Bouquet
        First consume required FLowers, then any kind of Flowers available in Storage to match total number in Bouquet
        """
        if not self._created_bouquet:
            raise BouquetComposerException("Bouquet must be created before consuming")

        bouquet = Bouquet(self._created_bouquet)

        for flower, num in self._created_bouquet.flowers.items():
            self._storage.consume_flowers(flower, num)

        extra_flowers_num = self._created_bouquet.extra_flowers_num

        while extra_flowers_num > 0:
            for flower, available_num in self._storage.flowers:
                if available_num >= extra_flowers_num:
                    self._storage.consume_flowers(flower, extra_flowers_num)
                    bouquet.add_flowers(flower, extra_flowers_num)
                    extra_flowers_num = 0

                    break
                elif available_num:
                    self._storage.consume_flowers(flower, available_num)
                    bouquet.add_flowers(flower, available_num)
                    extra_flowers_num = extra_flowers_num - available_num
            else:
                raise BouquetComposerException(
                    f"Cannot consume enough extra flowers to create bouquet {self._created_bouquet}"
                )
        return bouquet
