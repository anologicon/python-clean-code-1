from src.product import Product

class TestProduct:

    def test_should_calculate_product_volume(self):
        product = Product(10, 10, 10, 1)
        assert product.calculate_volume_meters() == 0.001
    
    def test_should_calculate_density(self):
        product = Product(10, 10, 10, 1)
        assert product.calculate_density() == 1000