from common.bouquet_composer.fabric import create_size_specific as composer_fabric
from common.io_manager import Reader, read_bouquet_designs
from common.production_facility import ProductionFacility
from common.bouquet_composer.simple import SimpleComposer


def run():
    """
    Main function. Everything starts here
    """
    reader = Reader()

    bouquet_designs = read_bouquet_designs(reader)

    composers = composer_fabric(bouquet_designs, SimpleComposer)

    facility = ProductionFacility(composers, reader)

    for bouquet in facility.process():
        print(bouquet)


if __name__ == "__main__":
    run()
