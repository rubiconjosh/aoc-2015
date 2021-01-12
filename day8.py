def character_count(string):
    escaped_characters = 0
    for letter in string:
        if letter == '\\':
            escaped_characters += 1
    return len(string) - escaped_characters - 2