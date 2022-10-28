#zad 2

def find(word,letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('ananas', 'a'))
print(find('drukarka', 'd'))
print(find('drukarka', 'r'))
print(find('drukarka', 'a'))
