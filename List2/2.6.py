#zad 6

def compare (z1, z2):
    if len(z1)==len(z2):
        for i in range(0,(len(z1)-1)):
            if z1[i] != z2[i]:
                return False
            else:
                return True
    else:
        return False


print(compare('ananas', 'banana'))
print(compare('ananas', 'ananas'))
print(compare('ananas', 'roza'))
