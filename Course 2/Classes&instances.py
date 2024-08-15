import random
#first you need to define the class, and then a dot(.) and after the dot you put the specific "Variable".
class Dog:
    info = "Jeff is a dog furry that kisses blocks"

    def __init__(self):
        print("I am alive")
        self.lucky_number = random.randint(1,10)
print(Dog.info)

Dog()

#this is an instance.
dog1 = Dog()
dog2 = Dog()

print(dog1.lucky_number)
print(dog2.lucky_number)

class Square:
    sides = 4

my_shape = Square()
my_shape.height = 10