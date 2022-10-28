import math
import random

a = c = 1
x = 10**7.4
y = 10**8.5

for i in range(0,100):
    b = random.uniform(x,y)


    x11 = (1/(2*a))*(-b+math.sqrt(b**2-4*a*c))
    x12 = (1/(2*a))*(-b-math.sqrt(b**2-4*a*c))
    print('x11=', x11)
    print('x12=', x12)

    x21 = (1/(2*a))*(-b-math.sqrt(b**2-4*a*c))
    x22 = c/(a*x21)
    print('x21=', x21)
    print('x22=', x22)

  
