import numpy as np

def parseCommand(command):
    parts = command.split(' ')
    action = ''
    start = ''
    end = ''
    if parts[0] == 'toggle':
        action = parts[0]
        start = parts[1]
        end = parts[3]
    else:
        action = parts[1]
        start = parts[2]
        end = parts[4]

    start = tuple(int(el) for el in start.split(','))
    end = tuple(int(el) for el in end.split(','))
    return (action, start, end)


rawCommands = open('day6-input.txt').read().splitlines()
commands = []
for command in rawCommands:
    commands.append(parseCommand(command))

lightGrid = np.zeros((1000,1000))
for command in commands:
    subGrid = lightGrid[command[1][1]:command[2][1]+1,command[1][0]:command[2][0]+1]
    if command[0] == 'on':
        subGrid += 1
    elif command[0] == 'off':
        with np.nditer(subGrid, op_flags=['readwrite']) as it:
           for x in it:
               x[...] = x-1 if x>0 else 0
    else:
        subGrid += 2
print(lightGrid.sum())
