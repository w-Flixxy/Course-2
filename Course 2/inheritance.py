class Animal:
    info = "Jamal is a good boy"
    def __init__(self, name):
        print("ChunkyMonkey")
class Dog(Animal):
    info = "Monkey"
    def __init__(self,name):
        super().__init__(name) #YOU NEED TO PUT THIS HERE TO LET IT WORK
        print("Hi")
        self.fur = ""
    def cow(self, name):
        print(f"Hi my name is {name}!")


class Bulldog(Dog):
    pass

dog1 = Bulldog("Fido")