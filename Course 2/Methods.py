class Dog:
    info = "Balls"

    def __init__(self, name):
        print("Hi my name is john cena!")
        self.name = name
    
    def bark(self):
        print(f"Woof My name is {self.name}")

dog1 = Dog("Fido")
dog3 = Dog("JEFF")

dog1.bark()
dog3.bark()


class Square:
    sides = 4
    def like (self, DDD):
        print(f"I like {DDD}")
my_shape = Square()
my_shape.height = 10

