from .item import Item
import abc

class FreightCalculatorInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def calculate(item: Item) -> float:
        pass