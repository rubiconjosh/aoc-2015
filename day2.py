input = open("day2-input.txt")
input = input.read()

lines = input.splitlines()

total = 0
ribbon = 0

for line in lines:
    dimensions = line.split('x')
    dimensions = [int(x) for x in dimensions]
    dimensions.sort()
    total += 3 * dimensions[0] * dimensions[1]
    total += 2 * dimensions[0] * dimensions[2]
    total += 2 * dimensions[1] * dimensions[2]
    ribbon += dimensions[0] * dimensions[1] * dimensions[2]
    ribbon += 2 * dimensions[0] + 2 * dimensions[1]

print(total)
print(ribbon)
