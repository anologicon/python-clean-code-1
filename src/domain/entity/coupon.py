import datetime


class Coupon:
    def __init__(
        self, code: str, percentage: float, date_expiration: datetime.date = None
    ):
        self.code = code
        self.percentage = percentage
        self.date_expiration = date_expiration

    def is_valid(self, today: datetime.date = datetime.date.today()) -> bool:
        if self.date_expiration is None:
            return True
        return self.date_expiration >= today
