import sys
from typing import List
from .constants import READ_SEPARATOR
from .bouquet import BouquetDesign


class Reader(object):
    """Read data from any file-like object
    By default that is stdin. For testing can be replaced with in-memory file (StringIO form io library)
    """

    def __init__(self, input_stream=sys.stdin):
        self._input_stream = input_stream

    def read(self):
        try:
            return self._input_stream.readline().strip("\n")
        except StopIteration:
            return None


def read_bouquet_designs(reader: Reader) -> List[BouquetDesign]:
    """Reads lines from input until met empty line
    Empty line is a separator between Bouquet recipes and Flowers
    """
    bouquets = []
    while True:
        recipe = reader.read()
        if recipe == READ_SEPARATOR:
            break
        bouquets.append(BouquetDesign.parse(recipe))

    return bouquets
