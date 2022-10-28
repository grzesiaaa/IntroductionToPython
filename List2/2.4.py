import time
A = time.time()

def count(word,letter):
    n=0
    for i in range(0, (len(word)-1)):
        if word[i] == letter:
            n += 1
    return n

print(count('pineapple', 'p'))

B = time.time() - A
print(B)
