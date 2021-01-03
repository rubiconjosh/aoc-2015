input = open('day1-input.txt')
input = input.read()
floor = 0
for instruction in input:
    if instruction == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
