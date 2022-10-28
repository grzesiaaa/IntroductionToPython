import time
A = time.time()

def policz(word,letter):
    return word.count(letter)

print (policz('pineapple', 'p'))

B = time.time() - A
print(B)

