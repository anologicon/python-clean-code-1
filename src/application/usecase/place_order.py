from .place_order_input import PlaceOrderInput
from .place_order_output import PlaceOrderOutput
from dataclasses import dataclass
from ...domain.entity.order import Order
from ...domain.repository.item_repository_interface import ItemRepositoryInterface
from ...domain.repository.coupon_repository_interface import CouponRepositoryInterface
from ...domain.repository.order_repository_interface import OrderRepositoryInterface


@dataclass
class PlaceOrder:

    item_repository: ItemRepositoryInterface
    coupon_repository: CouponRepositoryInterface
    order_repository: OrderRepositoryInterface

    def execute(self, input: PlaceOrderInput) -> PlaceOrderOutput:
        order = Order(input.cpf, input.date)
        for item in input.order_items:
            item_entity = self.item_repository.find_by_id(item["idItem"])
            if not item_entity:
                raise Exception("Item not found")
            order.add_item(item_entity, item["quantity"])
        if input.coupon:
            coupon_entity = self.coupon_repository.find_by_code(input.coupon)
            if coupon_entity:
                order.add_coupon(coupon_entity)
        self.order_repository.save(order)
        return PlaceOrderOutput(order.get_total_value())
