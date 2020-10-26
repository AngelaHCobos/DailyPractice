''' from collections import defaultdict

def chainedWords(words):
    first = defaultdict(list)
    last = defaultdict(list)
    for word in words:
        first_char = word
        last_char = word[-1]
        first[first_char].append(word)
        last[last_char].append(word)
    for key, value in first.items():




print chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna'])
# True '''


first_char1 = ""
last_char1 = ""
first_char2 = ""
last_char2 = ""

def chainedWords(words):
    for word in words:
        first_char1 = word[0]
        last_char1 = word[-1]
        if  last_char1 == first_char1:
            


