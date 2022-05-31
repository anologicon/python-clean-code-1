import abc
from ..entity.item import Item


class ItemRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_id(id: int) -> Item or None:
        pass
