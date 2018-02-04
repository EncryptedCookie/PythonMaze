# coding=utf-8
from msvcrt import getch

levelOne = {'level': list('''█ █ █ █ █ █ █ █ █
█ ▓ █ ░ ░ ░ ░ ▒ █
█ ░ █ ░ █ █ █ █ █
█ ░ █ ░ ░ ░ ░ ░ █
█ ░ █ █ █ █ █ ░ █
█ ░ █ ░ ░ ░ █ ░ █
█ ░ █ ░ █ ░ █ ░ █
█ ░ ░ ░ █ ░ ░ ░ █
█ █ █ █ █ █ █ █ █
'''), 'playerIndex': 40, 'width': 36}

levelTwo = {'level': list('''█ █ █ █ █ █ █ █ █ █ █ █
█ ▓ ░ ░ ░ ░ █ ░ ░ ░ ░ █
█ █ █ █ █ ░ █ ░ █ █ ░ █
█ ░ ░ ░ ░ ░ █ █ █ ░ ░ █
█ ░ █ █ █ ░ █ ░ ░ ░ ░ █
█ ░ ░ █ ░ ░ █ ░ █ █ ░ █
█ █ ░ █ ░ █ █ ▒ █ ░ ░ █
█ ░ ░ █ ░ ░ █ █ █ ░ █ █
█ ░ █ █ █ █ █ ░ █ ░ ░ █
█ ░ ░ ░ █ ░ ░ ░ █ █ ░ █
█ ░ █ ░ ░ ░ █ ░ ░ ░ ░ █
█ █ █ █ █ █ █ █ █ █ █ █
'''), 'playerIndex': 52, 'width': 48}

levelThree = {'level': list('''█ █ █ █ █ █ █ █ █ █ █ █ █
█ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ █
█ ░ █ █ █ █ █ █ █ █ █ ░ █
█ ▓ █ ░ ░ ░ ░ ░ ░ ░ █ ░ █
█ █ █ ░ █ █ ░ █ █ █ █ ░ █
█ ░ ░ ░ █ ░ ░ ░ █ ░ █ ░ █
█ ░ █ ░ █ ░ ▒ ░ █ ░ ░ ░ █
█ ░ █ ░ █ ░ ░ ░ █ ░ █ ░ █
█ ░ █ ░ █ █ █ █ █ ░ █ ░ █
█ ░ █ ░ ░ █ ░ ░ ░ ░ █ ░ █
█ ░ █ █ █ █ ░ █ █ █ █ ░ █
█ ░ ░ ░ ░ ░ ░ ░ ░ █ ░ ░ █
█ █ █ █ █ █ █ █ █ █ █ █ █
'''), 'playerIndex': 160, 'width': 52}

levelFour = {'level': list('''█ █ █ █ █ █ █ █ █
█ ▓ ░ ░ ░ ░ ░ ▒ █
█ █ █ █ █ █ █ █ █
'''), 'playerIndex': 40, 'width': 36}

levelFive = {'level': list('''█ █ █ █ █ █ █ █ █
█ ▓ ░ ░ ░ ░ ░ ▒ █
█ █ █ █ █ █ █ █ █
'''), 'playerIndex': 40, 'width': 36}

currentMaze = {'level': '', 'playerIndex': 0, 'width': 0, 'number': 1}

def import_maze(mazeNumber):
    if mazeNumber == 1:
        currentMaze['level'] = levelOne['level']
        currentMaze['playerIndex'] = levelOne['playerIndex']
        currentMaze['width'] = levelOne['width']
    elif mazeNumber == 2:
        currentMaze['level'] = levelTwo['level']
        currentMaze['playerIndex'] = levelTwo['playerIndex']
        currentMaze['width'] = levelTwo['width']
    elif mazeNumber == 3:
        currentMaze['level'] = levelThree['level']
        currentMaze['playerIndex'] = levelThree['playerIndex']
        currentMaze['width'] = levelThree['width']
    elif mazeNumber == 4:
        currentMaze['level'] = levelFour['level']
        currentMaze['playerIndex'] = levelFour['playerIndex']
        currentMaze['width'] = levelFour['width']
    elif mazeNumber == 5:
        currentMaze['level'] = levelFive['level']
        currentMaze['playerIndex'] = levelFive['playerIndex']
        currentMaze['width'] = levelFive['width']


def get_goal():
    if currentMaze['number'] != 5:
        currentMaze['number'] += 1
        import_maze(currentMaze['number'])
    elif currentMaze['number'] == 5:
        print "You win!"


def move_player(direction):
    if direction == "up" and currentMaze['level'][currentMaze['playerIndex'] - currentMaze['width']:currentMaze['playerIndex'] - currentMaze['width'] + 3] == ['\xe2','\x96','\x91']:
        currentMaze['level'][currentMaze['playerIndex'] - currentMaze['width']:currentMaze['playerIndex'] - currentMaze['width'] + 3] = '\xe2', '\x96', '\x93'  # Moves the player up
        currentMaze['level'][currentMaze['playerIndex']:currentMaze['playerIndex'] + 3] = '\xe2', '\x96', '\x91'  # Makes the old space empty
        currentMaze['playerIndex'] -= currentMaze['width']
        return ''.join(currentMaze['level'])
    elif direction == "up" and currentMaze['level'][currentMaze['playerIndex'] - currentMaze['width']:currentMaze['playerIndex'] - currentMaze['width'] + 3] == ['\xe2','\x96','\x92']:
        get_goal()
        return ''.join(currentMaze['level'])
    if direction == "down" and currentMaze['level'][currentMaze['playerIndex'] + currentMaze['width']:currentMaze['playerIndex'] + currentMaze['width'] + 3] == ['\xe2', '\x96', '\x91']:
        currentMaze['level'][currentMaze['playerIndex'] + currentMaze['width']:currentMaze['playerIndex'] + currentMaze['width'] + 3] = '\xe2', '\x96', '\x93'  # Moves the player down
        currentMaze['level'][currentMaze['playerIndex']:currentMaze['playerIndex'] + 3] = '\xe2', '\x96', '\x91'  # Makes the old space empty
        currentMaze['playerIndex'] += currentMaze['width']
        return ''.join(currentMaze['level'])
    elif direction == "down" and currentMaze['level'][currentMaze['playerIndex'] + currentMaze['width']:currentMaze['playerIndex'] + currentMaze['width'] + 3] == ['\xe2', '\x96', '\x92']:
        get_goal()
        return ''.join(currentMaze['level'])
    if direction == "left" and currentMaze['level'][currentMaze['playerIndex'] - 4:currentMaze['playerIndex'] - 1] == ['\xe2', '\x96','\x91']:
        currentMaze['level'][currentMaze['playerIndex'] - 4:currentMaze['playerIndex'] - 1] = '\xe2', '\x96', '\x93'  # Moves the player left
        currentMaze['level'][currentMaze['playerIndex']:currentMaze['playerIndex'] + 3] = '\xe2', '\x96', '\x91'  # Makes the old space empty
        currentMaze['playerIndex'] -= 4
        return ''.join(currentMaze['level'])
    elif direction == "left" and currentMaze['level'][currentMaze['playerIndex'] - 4:currentMaze['playerIndex'] - 1] == ['\xe2', '\x96','\x92']:
        get_goal()
        return ''.join(currentMaze['level'])
    if direction == "right" and currentMaze['level'][currentMaze['playerIndex'] + 4:currentMaze['playerIndex'] + 7] == ['\xe2', '\x96','\x91']:
        currentMaze['level'][currentMaze['playerIndex'] + 4:currentMaze['playerIndex'] + 7] = '\xe2', '\x96', '\x93'  # Moves the player right
        currentMaze['level'][currentMaze['playerIndex']:currentMaze['playerIndex'] + 3] = '\xe2', '\x96', '\x91'  # Makes the old space empty
        currentMaze['playerIndex'] += 4
        return ''.join(currentMaze['level'])
    elif direction == "right" and currentMaze['level'][currentMaze['playerIndex'] + 4:currentMaze['playerIndex'] + 7] == ['\xe2', '\x96','\x92']:
        get_goal()
        return ''.join(currentMaze['level'])


import_maze(1)
print(''.join(currentMaze['level']))
while True:
    key = ord(getch())
    if key == 72:
        print(move_player("up"))
    elif key == 80:
        print(move_player("down"))
    elif key == 75:
        print(move_player("left"))
    elif key == 77:
        print(move_player("right"))
