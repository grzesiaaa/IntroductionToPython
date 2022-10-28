def nwd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

l = [4,8,12,100,5550]

num1=l[0]
num2=l[1]
nwd2=nwd(num1,num2)

for i in range(2,len(l)):
    nwd2 = nwd(nwd2,l[i])

print(nwd2)

