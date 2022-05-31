from ....domain.repository.coupon_repository_interface import CouponRepositoryInterface
from ....domain.entity.coupon import Coupon

class CouponRepositoryMemory(CouponRepositoryInterface):

    def __init__(self):
        self.coupons = [
            Coupon('COUPON1', 10),
        ]

    def find_by_code(self, code: str) -> Coupon or None:
        for coupon in self.coupons:
            if coupon.code == code:
                return coupon
        return None