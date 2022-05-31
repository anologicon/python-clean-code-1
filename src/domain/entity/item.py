class Item:
    def __init__(
        self,
        id: int,
        description: str,
        price: int,
        height: int = 0,
        width: int = 0,
        length: int = 0,
        weight: int = 0,
    ):
        self.id = id
        self.description = description
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    def calculate_volume(self) -> int:
        return round((self.height / 100) * (self.width / 100) * (self.length / 100), 6)

    def calculate_density(self) -> float:
        volume = self.calculate_volume()
        if volume == 0:
            return 0
        return self.weight / volume
