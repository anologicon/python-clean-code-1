class Product:

    def __init__(self, height: int, width: int, length: int, weight: int):
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    def calculate_volume_meters(self) -> int:
        return (self.height * self.width * self.length) / (10**6)

    def calculate_density(self) -> float:
        return (self.weight / self.calculate_volume_meters())