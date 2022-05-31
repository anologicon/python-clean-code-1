from ....domain.repository.item_repository_interface import ItemRepositoryInterface
from ....domain.entity.item import Item


class ItemRepositoryMemory(ItemRepositoryInterface):
    def __init__(self):
        self.items = [
            Item(1, "Celular", 1900),
            Item(2, "Caneta", 2),
            Item(3, "Luvas", 20),
        ]

    def find_by_id(self, id: int) -> Item or None:
        for item in self.items:
            if item.id == id:
                return item
        return None
