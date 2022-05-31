import datetime
from src.application.usecase.place_order import PlaceOrder
from src.infra.repository.memory.order_repository_memory import OrderRepositoryMemory
from src.infra.repository.memory.item_repository_memory import ItemRepositoryMemory
from src.infra.repository.memory.coupon_repository_memory import CouponRepositoryMemory
from src.application.usecase.place_order_input import PlaceOrderInput
import pytest

class TestPlaceOrder:

    def test_should_place_order(self):
        order_repository = OrderRepositoryMemory()
        item_repository = ItemRepositoryMemory()
        coupon_repository = CouponRepositoryMemory()

        place_order = PlaceOrder(
            item_repository, coupon_repository, order_repository)
        input = PlaceOrderInput(
            cpf='12345678901',
            date=datetime.datetime.now(),
            order_items=[
                {'idItem': 1, 'quantity': 1},
                {'idItem': 2, 'quantity': 1},
                {'idItem': 3, 'quantity': 1},
            ],
            coupon='COUPON1'
        )

        output = place_order.execute(input)
        assert output.total == 1729.8
