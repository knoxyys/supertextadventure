from cave import Cave
from character import Enemy, Friend
from item import Item
from map import gpsmap

dead = False
bag = []

cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")
den = Cave("Den")
den.set_description("A dark and spooky den with a faint smell of cheese")
thai = Cave("Tham Luang Cave")
thai.set_description("There once was a soccer team here")
wumpus_room = Cave("Wumpus Room")
wumpus_room.set_description("This is quite self explanatory, isn't it?")
tunnels = Cave("Tunnels")
tunnels.set_description("A network of tunnels that connect two caves")


cavern.link_cave(grotto, "north")
grotto.link_cave(cavern, "south")
grotto.link_cave(dungeon, "west")
dungeon.link_cave(grotto, "east")
grotto.link_cave(den, "east")
den.link_cave(grotto, "west")
den.link_cave(thai, "south")
thai.link_cave(den, "north")
cavern.link_cave(wumpus_room, "south")
wumpus_room.link_cave(cavern, "north")
tunnels.link_cave(wumpus_room, "east")
wumpus_room.link_cave(tunnels, "west")
tunnels.link_cave(dungeon, "north")
dungeon.link_cave(tunnels, "south")



# characters

mark = Enemy("Mark", "A ginger Wumpus with a bad attitude")
dungeon.set_character(mark)
mark.set_conversation("I am Mark the Evil Wumpus.")
mark.set_weakness("Silver")

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

dwarf = Friend("Dwarf", "A friendly dwarf with a beard")
dwarf.set_conversation("I am a dwarf, and I'm digging a hole to get out of here!")
den.set_character(dwarf)

diver = Friend("Diver", "A diver who got lost in the cave")
diver.set_conversation("I was looking for the soccer team, but I got lost.")
thai.set_character(diver)



# items

beer = Item("Beer", 5, 1)
beer.set_desc("For legal reasons this is apple juice in a beer can.")
beer.set_usecase("You feel so much better.")
grotto.set_item(beer)

popsicle = Item("Popsicle", 2, 3)
popsicle.set_desc("A frozen treat on a stick.")
popsicle.set_usecase("Mmmm... you feel refreshed.")
cavern.set_item(popsicle)

silver_sword = Item("Silver Sword", 10, 1)
silver_sword.set_desc("A sword made of silver, hmm...")
wumpus_room.set_item(silver_sword)

foil = Item("Foil", 1, 5)
foil.set_desc("It looks like foil blankets used to keep warm.")
foil.set_usecase("You feel warm and cozy.")
thai.set_item(foil)



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
        for item in bag:
            print(item.get_name() + " (x" + str(item.get_quantity()) + ")")
        fight_with = input('> ')
        for bag_item in bag:
            if bag_item.get_name().lower() == fight_with.lower():
                if inhabitant.fight(fight_with) == True:
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True
                        break
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
        print("Your bag contains:")
        for item in bag:
            print(item.get_name() + " (x" + str(item.get_quantity()) + ")")
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
    
    elif command == 'use':
        print("You have no items in your bag to use.")
    
    elif command == 'run':
        print("You run back to the cavern.")
        print("You lose your items on the way...")
        bag == []
        current_cave = cavern
    
    elif command == 'map':
        print("You are in the " + current_cave.get_name() + ".")
        gpsmap(current_cave.get_name())
    
    else: current_cave = current_cave.move(command)



# commands are move(dir), fight, talk, pat, use, steal, take, bag, run, map