import pytest
from ..common.flower import Flower
from ..common.exceptions import ProcessFlowerException


def test_creating_flower():
    flower = Flower.parse("aS")
    assert flower.size.value == "S"
    assert flower.specie == "a"


def test_creating_flower_fail():
    with pytest.raises(ProcessFlowerException):
        Flower.parse("1D")
