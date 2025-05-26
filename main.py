from cave import Cave

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

current_cave = cavern
while True:
    print('\n')
    current_cave.get_details()
    command = input('> ')
    current_cave = current_cave.move(command)