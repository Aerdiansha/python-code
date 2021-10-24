class item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return self.price * self.quantity


item1 = item("phone", 100, 1)
item2 = item("laptop", 1000, 2)


print(item1.calculate_total_price())
print(item2.calculate_total_price())

