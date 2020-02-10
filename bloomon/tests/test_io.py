import io

from ..common.bouquet import BouquetDesign
from ..common.io_manager import Reader, read_bouquet_designs


def test_reading_bouquet_recipes():
    bouquet_recipe1 = "AS1a1b10"
    bouquet_recipe2 = "BL1c1d20"
    reader = Reader(io.StringIO(f"{bouquet_recipe1}\n{bouquet_recipe2}\n\n"))
    bouquets = read_bouquet_designs(reader)
    assert bouquets == [BouquetDesign.parse(bouquet_recipe1), BouquetDesign.parse(bouquet_recipe2)]
