import math
import random

list=[]
for i in range(0,100):
    z = random.uniform(-14.5,14.5)
    t = random.uniform(-14.5,14.5)
    d = z+t*1j
    list.append(d)

for i in range(0,100):
    u=list[i].real
    z=list[i].imag
    print(i,u,z)

def modul(z):
    return math.sqrt((z.real)**2+(z.imag)**2)
  
def zwroc_kolidujace(): 
    for i in range(0,100):
        for j in range(0,100):
            if 0<modul(list[i]-list[j])<1:
                  print((i,j))
           
def rozsun():
    while zwroc_kolidujace():
        for i in range(0,100):
            for j in range(0,100):
                if 0<modul(list[i]-list[j])<1:
                    if list[j].real<13.5 and list[j].imag<13.5:
                        list[j] = list[j]+1+1j
                    else:
                         list[j]=list[j]-1-1j       
    for i in range(0,100):
        print(i,list[i].real,list[i].imag)

print(rozsun())
