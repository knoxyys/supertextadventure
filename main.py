from cave import Cave
from character import Enemy, Friend
from item import Item

dead = False
bag = []

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
mark.set_conversation("I am Mark the Evil Wumpus.")
mark.set_weakness("Silver")

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

beer = Item("Beer", 5, 1)
beer.set_desc("For legal reasons this is apple juice in a beer can.")
grotto.set_item(beer) # set_item so it differs from character


# main loop
current_cave = cavern
while dead == False:
    print('\n')
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    item = current_cave.get_item()

    if item is not None:
        print(f"You see a {item.get_name()} here: {item.get_desc()}")

    if inhabitant is not None:
        inhabitant.describe()
    else: print("There is no one here.")
    command = input('> ').lower()

    if command == 'fight' and isinstance(inhabitant, Enemy):
        print("What will you fight with?")
        fight_with = input('> ')
        if inhabitant.fight(fight_with) == True:
            print("Bravo hero, you won the fight!")
            current_cave.set_character(None)
            current_cave.get_details()
            inhabitant = current_cave.get_character()
        else:
            print("Scurry home, you lost the fight.\nGame end.")
            dead = True
    elif command == 'fight':
        print("There is no one to fight with here.")
    
    elif command == 'talk' and inhabitant is not None:
        inhabitant.talk()
    
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")
    
    elif command == 'steal' and isinstance(inhabitant, Enemy):
        inhabitant.steal()

    elif command == 'use' and item is not None:
        item.use()

    
    else: current_cave = current_cave.move(command)



# commands are move(dir), fight, talk, pat, use, steal