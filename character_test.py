from character import Enemy
mark = Enemy("Mark", "A smelly Wumpus", "Schoolwork")

mark.describe()
mark.set_conversation("Come closer. I can't see you")
mark.talk()

mark.set_weakness("Shower")
mark.get_weakness()

print("What will you fight with?")
weapon = input("> ")
mark.fight(weapon)