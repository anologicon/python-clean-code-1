import abc
from ..entity.coupon import Coupon


class CouponRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_code(code: str) -> Coupon or None:
        pass
