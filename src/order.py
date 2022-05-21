from .cpf_value import Cpf
from .item import Item
from .order_item import OrderItem
from .coupon import Coupon
from functools import reduce
import datetime

class Order:

    def __init__(self, cpf: Cpf, date: datetime.date = datetime.date.today()):
        self.cpf = cpf
        self.order_items = []
        self.coupon = None
        self.date = date

    def get_total_value(self):
        total = 0
        for order_item in self.order_items:
            total += order_item.get_total_value()
        total = self.__apply_coupon(total) 
        return total
    
    def add_coupon(self, coupon: Coupon):
        if coupon.is_valid(self.date):
            self.coupon = coupon

    def __apply_coupon(self, total):
        if not self.coupon:
            return total
        return total - ((total * self.coupon.percentage) / 100)

    def add_item(self, item: Item):
        self.order_items.append(OrderItem(item.description, item.price, item.quantity))