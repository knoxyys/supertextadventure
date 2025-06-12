map = '''
·-----------·        ·----------·        ·--------------·
|  dungeon  |--------|  grotto  |--------|     den      |
·-----------·        ·----------·        ·--------------·
      |                   |                     |
      |              ·----------·               |
      |              |  cavern  |               |
      |              ·----------·               |
      |                   |                     |
·-----------·        ·----------·        ·--------------·
|  tunnels  |--------|  wumpus  |        |  tham luang  |
·-----------·        ·----------·        ·--------------·
'''

def getmap():
    print(map) # testing

def gpsmap(location):
# we know that location will be in map
    filler = '☒' * len(location.lower())
    modified_map = map.replace(location.lower(), filler)
    print(modified_map)