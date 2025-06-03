class Item():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.desc = None
    
    def __str__(self):
        return f"{self.name} - ${self.price} (Quantity: {self.quantity})"
    
    def get_name(self):
        return self.name
    def get_desc(self):
        return self.desc
    def set_name(self, name):
        self.name = name
    def set_desc(self, desc):
        self.desc = desc
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    
    def use(self):
        print(f"You use the {self.name}.")
        print("It does nothing yet...")