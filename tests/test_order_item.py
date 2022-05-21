from src.order_item import OrderItem

class TestOrderItem:

    def test_should_calculate_total_value(self):
        order_item = OrderItem('Ef', 2, 5)
        assert order_item.get_total_value() == 10