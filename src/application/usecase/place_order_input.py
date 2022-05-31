from dataclasses import dataclass
import datetime

@dataclass
class PlaceOrderInput:

    cpf: str
    order_items: list[{'idItem': int, 'quantity': int}]
    date: datetime.date
    coupon: str = None