class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_out_of_stock(self):
        for p in self.products:
            if p.quantity == 0:
                self.products.remove(p)

    def update_quantity(self, product_id, amount):
        for p in self.products:
            if p.id == product_id:
                p.quantity += amount
                return True
        return False

    def calculate_total_value(self):
        total = 0
        for p in self.products:
            total += p.price * p.quantity
        return total

inv = Inventory()
inv.add_product(Product(1, "Camisa", 50.0, 10))
inv.add_product(Product(2, "Calça", 100.0, 0))
inv.add_product(Product(3, "Sapato", 150.0, 0))
inv.add_product(Product(4, "Meia", 15.0, 5))

inv.remove_out_of_stock()
print("Total no estoque:", inv.calculate_total_value())
