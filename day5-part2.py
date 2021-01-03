import re

def pairRepeats(word):
    for index, letter in enumerate(word[:-1]):
        pair = letter + word[index+1]
        for index2, letterPair in enumerate(word[index+2:-1]):
            current = letterPair + word[index+2+index2+1]
            if pair == current:
                return True
    return False

def letterRepeatsOneBetween(word):
    for index, letter in enumerate(word[:-2]):
        if letter == word[index+2]:
            return True
    return False

infile = open('day5-input.txt')
infile = infile.read()
questionableStrings = infile.splitlines()

count = 0
for item in questionableStrings:
    if pairRepeats(item) and letterRepeatsOneBetween(item):
        count += 1

print(count)
