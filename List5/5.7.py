def posortuj(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]

def anagram(x,y):
    x = x.lower()
    y = y.lower()
    if len(x) != len(y):
        return False
    else:
        x1 = list(x)
        y1 = list(y)
        posortuj(x1)
        posortuj(y1)
        if x1 == y1:
            return True
        else:
            return False

print(anagram('banan', 'naanb'))
print(anagram('pomidor', 'maslo'))
print(anagram('BaNan', 'naanb'))
        
