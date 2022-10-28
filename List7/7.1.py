import math

class Rocket:

    def __init__(self,v: float, number: int = 0, a: int = 0, b: int = 0):
        self.a = a
        self.b = b
        self.number = number
        self.v = v

    def move(self,x: int,y: int):
        self.a += x
        self.b += y

    def get_position(self):
        return self.a, self.b

    def get_distance(self,Rocket2):
        return math.sqrt((Rocket2.a-self.a)**2+(Rocket2.b-self.b)**2)

    def fuel(self,t: float):
        if self.v*t>=100:
            return 'Ups. Koniec podrózy. Brak paliwa'
        else:
            return 'Juupi. Można lecieć dalej.'