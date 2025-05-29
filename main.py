from cave import Cave
from character import Enemy

cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave ")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")

cavern.link_cave(grotto, "north")
grotto.link_cave(cavern, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")

mark = Enemy("Mark", "A ginger Wumpus with a bad attitude")
dungeon.set_character(mark)
mark.set_conversation("i smell like fart ghrrrr")
mark.set_weakness("shower")

current_cave = cavern
while True:
    print('\n')
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant.talk()
    else: print("There is no one here.")
    command = input('> ').lower()
    if command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Bravo,hero you won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the fight.") # fix this maybe
        else:
            print("There is no one here to fight with")

    current_cave = current_cave.move(command)