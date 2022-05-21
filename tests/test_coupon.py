from src.coupon import Coupon
import datetime
import pytest

class TestCoupon:

    def test_should_validate_coupon_expiration(self, mocker):
        coupon = Coupon('20 OFF', 20, datetime.date(2020, 1, 1))
        assert coupon.is_valid(datetime.date(2019, 12, 10)) == True
    
    def test_should_validate_coupon_expiration_should_be_false(self, mocker):
        coupon = Coupon('20 OFF', 20, datetime.date(2020, 1, 1))
        assert coupon.is_valid(datetime.date(2021, 12, 10)) == False