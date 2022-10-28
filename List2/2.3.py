#zad3

def findFrom(word,letter,pos):
    while pos < len(word):
        if word[pos] == letter:
            return pos
        pos+=1
    return -1

print(findFrom("ciezarowka", "r", 0))
print(findFrom("ciezarowka", "r", 6))
