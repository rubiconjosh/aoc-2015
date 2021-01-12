def character_count(string):
    escaped_characters = 0
    for index, letter in enumerate(string):
        if letter == '\\':
            if string[index+1] == 'x':
                escaped_characters += 3
            else:
                escaped_characters += 1

    return len(string) - escaped_characters - 2
