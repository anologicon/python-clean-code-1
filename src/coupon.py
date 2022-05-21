import datetime
class Coupon:

    def __init__(self, code: str, percentage: float, date_expiration: datetime.date = None):
        self.code = code
        self.percentage = percentage
        self.date_expiration = date_expiration
    
    def is_valid(self) -> bool:
        if self.date_expiration is not None:
            today = datetime.date.today()
            if today > self.date_expiration:
                return False
        return True