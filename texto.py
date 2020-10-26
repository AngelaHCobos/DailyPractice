from collections import defaultdict

names = set()
lock = Mutex()

def countName(text):
    dicc = defaultdict(int)
    count = 0
    for word in text.split(" "):
        dicc[word] += 1
    for word, c in dicc.items():
        lock
        condicion = word not in names
        unlock
        if condicion:
            if isName(word):
                lock
                names.add(word)
                unlock
                count += c
    return count



def isName(word):
    return True
        