inFile = open('day6-input.txt')
rawCommands = inFile.read().splitlines()

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

parsedCommands = []
for command in rawCommands:
    parsedCommands.append(parseCommand(command))

rows = 1000
cols = 1000
lightGrid = [False]*rows*cols
for command in parsedCommands:
    for row in range(rows):
        for col in range(cols):
            if row >= command[1][1] and row <= command[2][1] and col >= command[1][0] and col <= command[2][0]:
                if command[0] == 'on':
                    lightGrid[rows * row + col] = True
                elif command[0] == 'off':
                    lightGrid[rows * row + col] = False
                else:
                    lightGrid[rows * row + col] = not lightGrid[rows * row + col]

count = 0
for light in lightGrid:
    if light:
        count += 1

print(count)
