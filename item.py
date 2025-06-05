class Item():
    def __init__(self, name, weight, quantity):
        self.name = name
        self.weight = weight
        self.quantity = quantity
        self.desc = None
        self.usecase = None
    
    def __str__(self):
        return f"{self.name} - ${self.weight} (Quantity: {self.quantity})"
    
    def get_name(self):
        return self.name
    def get_desc(self):
        return self.desc
    def set_name(self, name):
        self.name = name
    def set_desc(self, desc):
        self.desc = desc
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def set_usecase(self, usecase):
        self.usecase = usecase
    def get_usecase(self):
        return self.usecase
    
    def use(self):
        if self.usecase is None:
            print(f"You can't use {self.name} for anything right now.")
        else:
            print(f"You use the {self.name}.")
            print(self.usecase)