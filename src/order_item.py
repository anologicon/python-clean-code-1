class OrderItem:

    def __init__(self, id: str, price: float, quantity: int):
        self.id = id
        self.price = price
        self.quantity = quantity

    def get_total_value(self) -> float:
        return self.price * self.quantity