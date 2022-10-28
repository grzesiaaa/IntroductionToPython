

import matplotlib.pyplot as plt
import math
def policz(x):
    suma = 1
    for i in range(1,61):
        suma += x**i/(math.factorial(i))
    return suma

print(policz(10))
print(policz(2))
print(policz(-2))
print(policz(-10))

print('blad wzgledny')
a = (abs(math.exp(10)-policz(10)))/math.exp(10)
b = (abs(math.exp(2)-policz(2)))/math.exp(2)
c = (abs(math.exp(-2)-policz(-2)))/math.exp(-2)
d = (abs(math.exp(-10)-policz(-10)))/math.exp(-10)

print(a)
print(b)
print(c)
print(d)

listax = [10, 2, -2, -10]
listay = [a, b, c, d]
plt.plot(listax,listay, 'oy')
plt.xlabel("wartość x")
plt.ylabel('błąd względny')
plt.show()