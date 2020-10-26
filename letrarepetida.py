LETRAS = "Abcdefcghijklmnopqrstuvwz" #FALSE
SENTENCE = "The quick brown fox jumps over the lazy dog" #TRUE

def search(letras):
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    letras = letras.lower()
    test = set()
    for x in letras:
        if x in alphabeth:
            test.add(x)
    if len(test) == len(alphabeth):
        return True    
    return False

print(search(SENTENCE))