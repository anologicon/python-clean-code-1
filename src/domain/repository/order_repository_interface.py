import abc
from ..entity.order import Order

class OrderRepositoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save(order: Order) -> None:
        pass