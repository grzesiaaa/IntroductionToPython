from zad1 import Rocket
import random
import math

r1 = Rocket(0, 1, random.randint(-50,50), random.randint(-50,50))
r2 = Rocket(0, 2, random.randint(-50,50), random.randint(-50,50))
r3 = Rocket(0, 3, random.randint(-50,50), random.randint(-50,50))
r4 = Rocket(0, 4, random.randint(-50,50), random.randint(-50,50))
r5 = Rocket(0, 5, random.randint(-50,50), random.randint(-50,50))

flota = [r1,r2,r3,r4,r5]

def move_show(n):
    for i in range(n):
        print("Ruch",i+1)
        for r in flota:
            r.move(random.randint(1,20), random.randint(1,20))
            new_position = r.get_position()
            print("Poycja rakiety nr", r.number,": ", new_position)
        for i in flota:
            for j in flota:
                if i.number<j.number:
                    print("Odległośc między rakietami:" '(', i.number, j.number,')', 'to', i.get_distance(j))


print(move_show(5))