import pytest
from ..common.bouquet import BouquetDesign
from ..common.exceptions import ProcessBouquetException


def test_creating_bouquet():
    bouquet_recipe = "AS1a2b3c10"
    bouquet_design = BouquetDesign.parse(bouquet_recipe)
    assert bouquet_design.size.value == "S"
    assert bouquet_design.name == "A"
    assert bouquet_design.flowers == {"a": 1, "b": 2, "c": 3}
    assert bouquet_recipe == str(bouquet_design)


def test_creating_flower_fail():
    with pytest.raises(ProcessBouquetException):
        BouquetDesign.parse("1D")
