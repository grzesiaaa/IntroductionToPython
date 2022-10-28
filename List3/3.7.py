import math
def equation():
    a = int(input("Podaj wspolczynnik rowniania a: "))
    b = int(input("Podaj wspolczynnik rowniania b: "))
    c = int(input("Podaj wspolczynnik rowniania c: "))
 
    delta = (b**2)-(4*a*c)
 
    if a == 0:
        print("To nie jest równanie kwadratowe")
    elif delta > 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)    
        print ("x1 = ", x1)
        print ("x2 = ", x2) 
    elif delta == 0:
         x = -b/(2*a)
         print ("x = ", x)
    else:
        print ("brak rozwiazania")

print(equation())
