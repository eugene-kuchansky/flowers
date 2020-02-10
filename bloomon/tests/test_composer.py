from ..common.bouquet_composer.fabric import create_size_specific
from ..common.bouquet_composer.simple import SimpleComposer
from ..common.bouquet import BouquetDesign
from ..common.constants import Size
from ..common.flower import Flower
from ..common.storage import FlowerStorage


def test_simple_composer_one_bouquet():
    bouquet_recipe = "AS1a1b3"

    bouquet_designs = [BouquetDesign.parse(bouquet_recipe)]

    small_flowers = [
        "aS",
        "bS",
        "cS",
    ]
    composer = SimpleComposer(Size.SMALL, bouquet_designs, FlowerStorage())
    bouquets = []
    for flower in small_flowers:
        composer.add_flower(Flower.parse(flower))
        is_created = composer.is_created
        if is_created:
            bouquets.append(composer.get_bouquet())
    assert len(bouquets) == 1
    bouquet = bouquets[0]
    assert str(bouquet) == "AS1a1b1c"


def test_simple_composer_multi_bouquets():
    bouquet_recipes = [
        "AS1a2",
        "BS1b2",
        "CS1c2",
    ]
    bouquet_designs = [BouquetDesign.parse(recipe) for recipe in bouquet_recipes]
    small_flowers = [
        "aS",
        "xS",
        "bS",
        "xS",
        "cS",
        "xS",
    ]
    composer = SimpleComposer(Size.SMALL, bouquet_designs, FlowerStorage())
    bouquets = []
    for flower in small_flowers:
        composer.add_flower(Flower.parse(flower))
        is_created = composer.is_created
        if is_created:
            bouquets.append(composer.get_bouquet())
    assert len(bouquets) == 3

    results = [
        "AS1a1x",
        "BS1b1x",
        "CS1c1x",
    ]
    for expected, bouquet in zip(results, bouquets):
        assert str(bouquet) == expected
