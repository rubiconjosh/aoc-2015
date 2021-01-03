import hashlib

puzzle_input = 'iwrupvqb'

current = 0
done = False

while not done:
    combined_input = puzzle_input + str(current)
    solution = hashlib.md5(combined_input.encode())
    solution = str(solution.hexdigest())
    print(solution)
    if solution.startswith('000000'):
        done = True
        print(current)
    current += 1
