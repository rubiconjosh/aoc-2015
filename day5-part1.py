import re

def vowelTest(word):
    return len(re.findall("[aeiou]", word, re.IGNORECASE)) > 2

def doubleLetter(word):
    pattern = re.compile(r"(.)\1")
    if pattern.search(word):
        return True
    else:
        return False

def nogoStrings(word):
    return 'ab' not in word and 'cd' not in word and 'pq' not in word and 'xy' not in word

infile = open('day5-input.txt')
infile = infile.read()
questionableStrings = infile.splitlines()

count = 0
for item in questionableStrings:
    if vowelTest(item) and doubleLetter(item) and nogoStrings(item):
        count += 1

print(count)
