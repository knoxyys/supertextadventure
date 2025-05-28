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
grotto.link_cave(dungeon, "left")
dungeon.link_cave(grotto, "east")

mark = Enemy("Mark", "A smelly Wumpus")
dungeon.set_character(mark)
mark.set_conversation("i smell like fart ghrrrr")
mark.set_weakness("shower")

current_cave = cavern
while True:
    print('\n')
    current_cave.get_details()
    current_cave.get_character() # fix this lolol
    command = input('> ').lower()
    current_cave = current_cave.move(command)