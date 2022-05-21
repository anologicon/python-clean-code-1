from src.order import Order
from src.cpf_value import Cpf
from src.item import Item
from src.coupon import Coupon
import datetime
import pytest

class TestOrder:

    def test_new_valid_cpf_order(self):
        order = Order(Cpf("487.501.680-88"))
        assert order.get_total_value() == 0

    def test_should_throw_and_error_new_invalid_cpf_order(self):
        with pytest.raises(Exception, match='Cpf Invalido'):
            order = Order(Cpf("487.501"))

    def test_should_add_items_to_order(self):
        order = Order(Cpf("487.501.680-88"))
        order.add_item(Item('Celular', 1900, 1))
        order.add_item(Item('Caneta', 2, 5))
        order.add_item(Item('Luvas', 1, 90))
        assert order.get_total_value() == 2000

    def test_should_apply_coupon_to_order(self):
        order = Order(Cpf("487.501.680-88"))
        order.add_item(Item('Celular', 1900, 1))
        order.add_item(Item('Caneta', 2, 5))
        order.add_item(Item('Luvas', 1, 90))
        order.add_coupon(Coupon('20 OFF', 20))
        assert order.get_total_value() == 1600
    
    def test_should_not_apply_expired_coupon_to_order(self, mocker):
        order = Order(Cpf("487.501.680-88"), datetime.date(2020, 2, 1))
        order.add_item(Item('Celular', 1900, 1))
        order.add_coupon(Coupon('20 OFF', 20, datetime.date(2020, 1, 31)))
        assert order.get_total_value() == 1900
        