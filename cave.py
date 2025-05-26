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
        print(self.desc) # same thing as get_description but prints it out
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction] # 'cave' is the full cave object (e.g. printing will output the memory address)
            print(f"The {cave.get_name()} is {direction}.")
    
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way.")
            return self