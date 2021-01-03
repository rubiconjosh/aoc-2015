input = open('day1-input.txt')
input = input.read()
floor = 0
positionEnteringBasement = 0
for position, instruction in enumerate(input):
    if instruction == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0 and positionEnteringBasement == 0:
        positionEnteringBasement = position + 1

print("Final floor: ", floor)
print("Position entering basement: ", positionEnteringBasement)
