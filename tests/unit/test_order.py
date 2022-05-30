from src.domain.entity.order import Order
from src.domain.entity.cpf_value import Cpf
from src.domain.entity.item import Item
from src.domain.entity.coupon import Coupon
from src.domain.entity.default_freight_calculator import DefaultFreightCalculator
from src.domain.entity.fixed_freight_calculator import FixedFreightCalculator
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
        order.add_item(Item(1, 'Celular', 1900), 1)
        order.add_item(Item(2, 'Caneta', 2), 5)
        order.add_item(Item(3, 'Luvas', 1), 90)
        assert order.get_total_value() == 2000

    def test_should_apply_coupon_to_order(self):
        order = Order(Cpf("487.501.680-88"))
        order.add_item(Item(4, 'Celular', 1900), 1)
        order.add_item(Item(5, 'Caneta', 2), 5)
        order.add_item(Item(6, 'Luvas', 1), 90)
        order.add_coupon(Coupon('20 OFF', 20))
        assert order.get_total_value() == 1600
    
    def test_should_not_apply_expired_coupon_to_order(self, mocker):
        order = Order(Cpf("487.501.680-88"), datetime.date(2020, 2, 1))
        order.add_item(Item(8, 'Celular', 1900), 1)
        order.add_coupon(Coupon('20 OFF', 20, datetime.date(2020, 1, 31)))
        assert order.get_total_value() == 1900

    def test_should_create_order_with_3_items_and_default_freight(self):
        order = Order(Cpf("487.501.680-88"), datetime.date(2020, 2, 1), DefaultFreightCalculator())
        order.add_item(Item(9, 'Tela', 1900, 40, 100, 3, 5), 1)
        order.add_item(Item(10, 'Teclado', 300, 5, 30, 10, 2), 1)
        order.add_item(Item(11, 'Agua', 2, 2, 2, 3, 1), 3)
        assert order.get_freight() == 100
    
    def test_should_create_order_with_3_items_and_fixed_freight(self):
        order = Order(Cpf("487.501.680-88"), datetime.date(2020, 2, 1), FixedFreightCalculator())
        order.add_item(Item(9, 'Tela', 1900, 40, 100, 3, 5), 1)
        order.add_item(Item(10, 'Teclado', 300, 5, 30, 10, 2), 1)
        order.add_item(Item(11, 'Agua', 2, 2, 2, 3, 1), 3)
        assert order.get_freight() == 50