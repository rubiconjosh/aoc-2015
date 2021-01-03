input = open('day3-input.txt')
input = input.read()

current_x = 0
current_y = 0

homes_visited = []
homes_visited.append((current_x, current_y))

for direction in input:
    if direction == '^':
        current_y += 1
    elif direction == '>':
        current_x += 1
    elif direction == 'v':
        current_y -= 1
    else:
        current_x -= 1

    if (current_x, current_y) not in homes_visited:
        homes_visited.append((current_x, current_y))

print(len(homes_visited))
