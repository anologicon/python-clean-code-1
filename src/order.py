from .cpf_value import Cpf
from .item import Item
from .order_item import OrderItem
from .coupon import Coupon
from functools import reduce

class Order:

    def __init__(self, cpf: Cpf):
        self.cpf = cpf
        self.order_items = []
        self.coupon = None

    def get_total_value(self):
        total = 0
        for order_item in self.order_items:
            total += order_item.get_total_value()
        return self.__apply_coupon(total)
    
    def add_coupon(self, coupon: Coupon):
        self.coupon = coupon

    def __apply_coupon(self, total):
        if not self.coupon:
            return total
        return total - ((total * self.coupon.percentage) / 100)

    def add_item(self, item: Item):
        self.order_items.append(OrderItem(item.description, item.price, item.quantity))