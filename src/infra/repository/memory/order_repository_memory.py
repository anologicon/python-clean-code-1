from ....domain.repository.order_repository_interface import OrderRepositoryInterface
from ....domain.entity.order import Order


class OrderRepositoryMemory(OrderRepositoryInterface):
    def __init__(self):
        self.orders = []

    def save(self, order: Order):
        self.orders.append(order)
