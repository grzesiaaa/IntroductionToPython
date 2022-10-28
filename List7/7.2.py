from zad1 import Rocket
import random

r1 = Rocket(0,1)
print('Początkowa pozycja to:', r1.get_position())
def move_show(n):
    for i in range(n):
        r1.move(random.randint(1,20), random.randint(1,20))
        new_position = r1.get_position()
        print('Przesunięcie nr:', i+1)
        print('Nowa pozycja:', new_position)

print(move_show(10))
