def character_count(string):
    escaped_characters = 0
    for index, letter in enumerate(string):
        if letter == '\\':
            if string[index+1] == 'x' and string[index - 1] != '\\':
                escaped_characters += 3
            elif index != 0 and string[index - 1] != '\\':
                escaped_characters += 1

    return len(string) - escaped_characters - 2


rawInput = open('day8-input.txt').read().splitlines()
raw_length = 0
characters = 0
for line in rawInput:
    raw_length += len(line)
    characters += character_count(line)

print(raw_length - characters)
