class Product:


    def __init__(self, name, price):
        self.name = name
        self.price = price


    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getProduct(self):
        return f"Product: {self.name}, Price: {self.price}"