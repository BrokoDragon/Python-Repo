class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def price_with_vat(self, vat_rate = 1.21):
        return self.price * vat_rate
    def __str__(self):
        return f"Name: {self.name}\n, Price: {self.price}\n, Price with VAT: {self.price_with_vat()}"

class DiscountedProduct(Product):
    def __init__(self, discount, name, price):
        super().__init__(name, price)
        if 0 < discount <= 1:
            self.discount = discount
        else:
            self.discount = 0
    def price_with_vat(self, vat_rate = 1.21):
        return self.price * (1 - self.discount) * vat_rate

class ShoppingCart:
    def __init__(self):
        self.products = []
    def add_product(self, product: Product):
        self.products.append(product)
    def total(self):
        return sum(product.price_with_vat() for product in self.products)
    def display(self):
        for product in self.products:
            print(product)
        print(f"Total price + VAT: {self.total()}")




