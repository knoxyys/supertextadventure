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
beer.set_usecase("You feel so much better.")
grotto.set_item(beer) # set_item so it differs from character

popsicle = Item("Popsicle", 2, 3)
popsicle.set_desc("A frozen treat on a stick.")
popsicle.set_usecase("You now know Mark's weakness is silver somehow.")
cavern.set_item(popsicle)

silver_sword = Item("Silver Sword", 10, 1)
silver_sword.set_desc("A sword made of silver, hmm...")
dungeon.set_item(silver_sword)



# main loop
current_cave = cavern
while dead == False:

    print('\n')
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    item = current_cave.get_item()


    if item is not None:
        print(f"You see {str(item.get_quantity())} {item.get_name()} here: {item.get_desc()}")

    if inhabitant is not None:
        inhabitant.describe()
    else: print("There is no one here.")
    command = input('> ').lower()

    if command == 'fight' and isinstance(inhabitant, Enemy):
        print("What will you fight with?")
        fight_with = input('> ')
        for bag_item in bag:
            if bag_item.get_name().lower() == fight_with.lower():
                if inhabitant.fight(fight_with) == True:
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True
                    current_cave.get_details()
                    inhabitant = current_cave.get_character()
                    break
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
    
    elif command == 'take' and item is not None:
        print(f"You take the {item.get_name()} from the cave.")
        bag.append(item)
        current_cave.set_item(None)
    
    elif command == 'bag':
        for item in bag:
            print(item.get_name() + " (x" + str(item.get_quantity()) + ")")
        if len(bag) == 0:
            print("Your bag is empty.")
    
    elif command == 'use' and len(bag) > 0:
        print("What do you want to use?")
        use_item = input('> ')
        found = False
        for item in bag:
            if item.get_name().lower() == use_item.lower():
                item.use()
                item.set_quantity(item.get_quantity() - 1)
                if item.get_quantity() <= 0:
                    bag.remove(item)
                found = True
                break
        if not found:
            print("You don't have that item in your bag.")
    
    else: current_cave = current_cave.move(command)



# commands are move(dir), fight, talk, pat, use, steal, take, bag