input = open('day3-input.txt')
input = input.read()

homes_visited = []
homes_visited.append((0, 0))

instruction_sets = [input[::2], input[1::2]]

for instructions in instruction_sets:
    current_x = 0
    current_y = 0
    for direction in instructions:
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
