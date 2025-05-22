class Cave:
    def __init__(self, name):
        self.name = name
        self.desc = None
        self.linked_caves = {}
    
    def get_description(self):
        return self.desc
    
    def set_description(self, desc):
        self.desc = desc
    
    def describe(self):
        print(self.desc)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
    
    def print_details(self):
        print(f"""
    Name: {self.name}
    Description: {self.desc}
        """)
        for cave, direction in self.linked_caves.items():
            print(f"Linked cave: {cave.get_name()} to the {direction}") # trying to do this but it aint work