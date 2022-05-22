from .freight_calculator_interface import FreightCalculatorInterface
from .item import Item

class DefaultFreightCalculator(FreightCalculatorInterface):

    MINIMUM_DISTANCE = 1000
    MINIMUM_FREIGHT = 10

    def calculate(self, item: Item) -> float:
        item_freight = self.MINIMUM_DISTANCE * \
            item.calculate_volume() * (item.calculate_density() / 100)
        return item_freight if item_freight > self.MINIMUM_FREIGHT else self.MINIMUM_FREIGHT
