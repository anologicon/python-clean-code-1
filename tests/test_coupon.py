from src.coupon import Coupon
import datetime
import pytest

class TestCoupon:

    def test_should_validate_coupon_expiration(self, mocker):
        mock_today = mocker.patch('src.coupon.datetime')
        mock_today.date.today.return_value = datetime.date(2019, 12, 10)

        coupon = Coupon('20 OFF', 20, datetime.date(2020, 1, 1))
        assert coupon.is_valid() == True
    
    def test_should_validate_coupon_expiration_should_be_false(self, mocker):
        mock_today = mocker.patch('src.coupon.datetime')
        mock_today.date.today.return_value = datetime.date(2021, 12, 10)
        coupon = Coupon('20 OFF', 20, datetime.date(2020, 1, 1))
        assert coupon.is_valid() == False