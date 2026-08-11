class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid price")

product = Product("Keyboard", 2000)

print(product.name)
print(product.price)

product.price = 2500
print(product.price)

product.price = -100
print(product.price)
        