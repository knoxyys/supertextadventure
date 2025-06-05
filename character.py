class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation
    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def __str__(self):
        return f"{self.name} - {self.description}"
    
    def set_weakness(self, weakness):
        self.weakness = weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if self.weakness.lower() in combat_item.lower():
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " swallows you, little wimp")
            return False
    
    def steal(self):
        print(f"You steal from {self.name}")
        print(f"weakness {self.weakness} stolen!") # steals the weakness bc idk
    
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def pat(self):
        print(self.name + " pats you back!")
    # What other methods could your Friend class have?
