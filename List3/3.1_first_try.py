#poprawka do zadania 1, ale dalej niekompletna
def letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d


h = letters("ala ma kotakkkkk jabgjaudbnzzzdeqsr")


for i in h:
    print(i+" " + '*'*h[i]) #printuje gwiazdki ale dla wszystkich liter
for i in h:
    print(i,h[i]) #printuje ile razy wystepuje dana litera
    



x = sorted(h.items(), key=lambda x:(-x[1],x[0]))
#x to lista posortowana od litery ktora wystepuje najczesciej to litery wystepujacej najrzadziej
print(x[2][2])
print(x[0:11])
y = x[0:11]
for i in y:
    print('*'*d[i]) #nie wiem przez co pomnozyc




