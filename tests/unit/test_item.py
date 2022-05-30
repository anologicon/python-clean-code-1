from src.domain.entity.item import Item

class TestItem:

    def test_should_calculate_item_volume(self):
        item = Item(1, "cubo", 100, 10, 10, 10, 1)
        assert item.calculate_volume() == 0.001
    
    def test_should_calculate_density(self):
        item = Item(1, "cubo", 100, 10, 10, 10, 1)
        assert item.calculate_density() == 1000