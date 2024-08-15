class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"
    #changes the way the Student class is called!
    

students=[Student("Joe", 0.97), Student("Jim", 0.62), Student("Jane", 0.12), Student("Jamal", 0.53), Student("Kat", 0.32), Student("Bob",1)]

failing_students=[]
for student in students:
    if student.score < 0.7:
            failing_students.append(student)

filter_list=list(filter(lambda student:student.score < 0.7,students))
nmbrs=[1,2,3,4,5]
filter_number=list(filter(lambda nmbr:nmbr%2 == 0,nmbrs))
print(filter_number)

print(failing_students)