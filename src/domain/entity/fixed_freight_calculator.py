from .freight_calculator_interface import FreightCalculatorInterface
from .item import Item

class FixedFreightCalculator(FreightCalculatorInterface):

    MINIMUM_FREIGHT = 10

    def calculate(self, item: Item) -> float:
        return self.MINIMUM_FREIGHT
